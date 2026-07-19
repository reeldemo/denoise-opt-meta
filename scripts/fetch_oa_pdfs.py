#!/usr/bin/env python3
"""Download OA PDFs for every bibliography cite. Fail loudly on missing PDFs.

Reads:
  artifacts/literature_oa/oa_catalog.json
  paper/v4/main.tex (\\bibitem keys)

Writes:
  artifacts/literature_oa/pdfs/<local_name>
  artifacts/literature_oa/oa_status.json
  artifacts/literature_oa/REFERENCES_OA.md
  artifacts/literature_oa/cite_to_pdf.json

Exit code 2 if any in-bib cite lacks a successful OA PDF download.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "artifacts" / "literature_oa" / "oa_catalog.json"
MAIN_TEX = ROOT / "paper" / "v4" / "main.tex"
OUT = ROOT / "artifacts" / "literature_oa"
PDF_DIR = OUT / "pdfs"


def bib_keys(tex: str) -> list[str]:
    return re.findall(r"\\bibitem\{([^}]+)\}", tex)


def download(url: str, dest: Path, timeout: int = 90) -> tuple[bool, str]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 1000:
        head = dest.read_bytes()[:5]
        if head.startswith(b"%PDF"):
            return True, "cached"
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "denoise-opt-meta-oa-fetch/2.0 (research; mailto:julian.m.kleber@gmail.com)"
            },
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        if len(data) < 1000 or not data[:5].startswith(b"%PDF"):
            return False, f"not_pdf_or_tiny len={len(data)}"
        dest.write_bytes(data)
        return True, "downloaded"
    except Exception as e:  # noqa: BLE001
        return False, str(e)


def main() -> int:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    entries = {e["cite_key"]: e for e in catalog["entries"]}
    # Prefer unique local files; allow shared PDF only if same local_name intentional
    tex = MAIN_TEX.read_text(encoding="utf-8")
    keys = bib_keys(tex)
    missing_in_catalog = [k for k in keys if k not in entries]
    if missing_in_catalog:
        print("FAIL: bib keys missing from oa_catalog.json:", missing_in_catalog, flush=True)
        return 2

    PDF_DIR.mkdir(parents=True, exist_ok=True)
    records = []
    cite_to_pdf = {}
    failures = []

    for key in keys:
        e = entries[key]
        dest = PDF_DIR / e["local_name"]
        ok, msg = download(e["oa_pdf_url"], dest)
        rec = {
            "cite_key": key,
            "title": e.get("title"),
            "role": e.get("role"),
            "oa_pdf_url": e["oa_pdf_url"],
            "local_name": e["local_name"],
            "status": msg,
            "oa": ok,
            "pdf_path": str(dest.relative_to(ROOT)) if ok else None,
            "borderline": e.get("borderline"),
            "arxiv": e.get("arxiv"),
        }
        records.append(rec)
        if ok:
            cite_to_pdf[key] = rec["pdf_path"]
        else:
            failures.append(f"{key}: {msg} url={e['oa_pdf_url']}")

    # Also download catalog entries not yet in bib (inventory completeness)
    for key, e in entries.items():
        if key in cite_to_pdf:
            continue
        dest = PDF_DIR / e["local_name"]
        ok, msg = download(e["oa_pdf_url"], dest)
        records.append(
            {
                "cite_key": key,
                "title": e.get("title"),
                "role": e.get("role"),
                "in_bib": False,
                "oa_pdf_url": e["oa_pdf_url"],
                "local_name": e["local_name"],
                "status": msg,
                "oa": ok,
                "pdf_path": str(dest.relative_to(ROOT)) if ok else None,
            }
        )

    oa_bib = sum(1 for r in records if r.get("oa") and r["cite_key"] in keys)
    status = {
        "policy": "OA-only",
        "n_bib_cites": len(keys),
        "n_bib_oa_pdfs": oa_bib,
        "n_failures": len(failures),
        "failures": failures,
        "dropped_non_oa": catalog.get("dropped_non_oa", []),
        "records": records,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "oa_status.json").write_text(json.dumps(status, indent=2), encoding="utf-8")
    (OUT / "cite_to_pdf.json").write_text(json.dumps(cite_to_pdf, indent=2), encoding="utf-8")

    lines = [
        "# Reference OA status (OA-only policy)",
        "",
        f"- Bibliography cites: **{len(keys)}**",
        f"- OA PDFs on disk for bib cites: **{oa_bib}**",
        f"- Failures: **{len(failures)}**",
        "",
        "## Cite → local PDF",
        "",
    ]
    for k in keys:
        p = cite_to_pdf.get(k, "MISSING")
        lines.append(f"- `{k}` → `{p}`")
    if failures:
        lines += ["", "## FAILURES (must not remain in bib)", ""]
        lines.extend(f"- {f}" for f in failures)
    borderline = [r for r in records if r.get("borderline") and r["cite_key"] in keys]
    if borderline:
        lines += ["", "## Borderline OA (author-hosted of publisher articles)", ""]
        for r in borderline:
            lines.append(f"- `{r['cite_key']}`: {r['borderline']}")
    lines += ["", "## Dropped non-OA (replaced)", ""]
    for d in catalog.get("dropped_non_oa", []):
        lines.append(
            f"- `{d['old_key']}` ({d['reason']}) → {', '.join(d.get('replaced_by', []))}"
        )
    (OUT / "REFERENCES_OA.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"bib={len(keys)} oa_ok={oa_bib} fail={len(failures)} -> {OUT}", flush=True)
    if failures:
        print("FAILED DOWNLOADS:", flush=True)
        for f in failures:
            print(" ", f, flush=True)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
