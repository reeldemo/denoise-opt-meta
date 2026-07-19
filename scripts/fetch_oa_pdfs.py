#!/usr/bin/env python3
"""Download open-access PDFs for paper references; flag non-OA.

Writes:
  artifacts/literature_oa/pdfs/*.pdf
  artifacts/literature_oa/oa_status.json
  artifacts/literature_oa/REFERENCES_OA.md
"""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT / "paper" / "v4" / "curated_literature.json"
MAIN_TEX = ROOT / "paper" / "v4" / "main.tex"
OUT = ROOT / "artifacts" / "literature_oa"
PDF_DIR = OUT / "pdfs"


def arxiv_id_from_url(url: str) -> str | None:
    m = re.search(r"arxiv\.org/(?:pdf|abs)/([0-9]+\.[0-9]+)(v\d+)?", url)
    return m.group(1) if m else None


def arxiv_id_from_doi(doi: str) -> str | None:
    m = re.search(r"arXiv\.([0-9]+\.[0-9]+)", doi, re.I)
    if m:
        return m.group(1)
    m = re.search(r"10\.48550/arXiv\.([0-9]+\.[0-9]+)", doi, re.I)
    return m.group(1) if m else None


def bib_entries() -> list[dict]:
    text = MAIN_TEX.read_text(encoding="utf-8")
    entries = []
    for m in re.finditer(
        r"\\bibitem\{([^}]+)\}(.*?)(?=\\bibitem\{|\\end\{thebibliography\})",
        text,
        re.S,
    ):
        key = m.group(1)
        body = m.group(2)
        arxiv = None
        href = re.search(r"arxiv\.org/abs/([0-9]+\.[0-9]+)", body)
        if href:
            arxiv = href.group(1)
        title = ""
        tm = re.search(r"\\newblock\s+([^\n\\]+)", body)
        if tm:
            title = re.sub(r"[{}\\]", "", tm.group(1)).strip().rstrip(".")
        screened = "Screened" in body
        entries.append(
            {
                "cite_key": key,
                "title_guess": title[:120],
                "arxiv_id": arxiv,
                "screened": screened,
                "has_arxiv_link": arxiv is not None,
            }
        )
    return entries


def download(url: str, dest: Path, timeout: int = 60) -> tuple[bool, str]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 1000:
        return True, "cached"
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "denoise-opt-meta-oa-fetch/1.0 (research; mailto:julian.m.kleber@gmail.com)"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        if len(data) < 1000 or not data[:5].startswith(b"%PDF"):
            return False, f"not_pdf_or_tiny len={len(data)}"
        dest.write_bytes(data)
        return True, "downloaded"
    except Exception as e:  # noqa: BLE001
        return False, str(e)


def main() -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    curated = json.loads(CURATED.read_text(encoding="utf-8"))
    records = []
    for role in ("used", "screened"):
        for item in curated.get(role, []):
            rec = {
                "source": "curated",
                "role": item.get("role", role),
                "title": item.get("title"),
                "doi": item.get("doi"),
                "oa_url": item.get("oa_url"),
                "arxiv_id": None,
                "oa": False,
                "pdf_path": None,
                "status": "pending",
            }
            if item.get("oa_url"):
                rec["arxiv_id"] = arxiv_id_from_url(item["oa_url"])
            if not rec["arxiv_id"] and item.get("doi"):
                rec["arxiv_id"] = arxiv_id_from_doi(item["doi"])
            records.append(rec)

    # Merge bib keys
    for b in bib_entries():
        match = None
        if b["arxiv_id"]:
            for r in records:
                if r.get("arxiv_id") == b["arxiv_id"]:
                    match = r
                    break
        if match is None:
            records.append(
                {
                    "source": "bibliography",
                    "role": "screened" if b["screened"] else "used",
                    "title": b["title_guess"],
                    "doi": None,
                    "oa_url": f"https://arxiv.org/pdf/{b['arxiv_id']}" if b["arxiv_id"] else None,
                    "arxiv_id": b["arxiv_id"],
                    "cite_key": b["cite_key"],
                    "oa": False,
                    "pdf_path": None,
                    "status": "pending",
                }
            )
        else:
            match["cite_key"] = b["cite_key"]

    # Dedup by arxiv_id / title
    seen = set()
    uniq = []
    for r in records:
        key = r.get("arxiv_id") or r.get("title")
        if key in seen:
            continue
        seen.add(key)
        uniq.append(r)
    records = uniq

    for r in records:
        aid = r.get("arxiv_id")
        url = r.get("oa_url")
        if aid:
            url = f"https://arxiv.org/pdf/{aid}.pdf"
            r["oa_url"] = url
            dest = PDF_DIR / f"{aid}.pdf"
            ok, msg = download(url, dest)
            r["status"] = msg
            r["oa"] = ok
            r["pdf_path"] = str(dest.relative_to(ROOT)) if ok else None
        else:
            r["oa"] = False
            r["status"] = "no_oa_url_flagged_paywalled_or_unknown"
            r["access"] = "non_oa"

    oa_n = sum(1 for r in records if r["oa"])
    non = [r for r in records if not r["oa"]]
    status = {
        "n_total": len(records),
        "n_oa_downloaded": oa_n,
        "n_non_oa_flagged": len(non),
        "records": records,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "oa_status.json").write_text(json.dumps(status, indent=2), encoding="utf-8")

    lines = [
        "# Reference OA status",
        "",
        f"- Total tracked: **{len(records)}**",
        f"- OA PDFs downloaded/cached: **{oa_n}** → `artifacts/literature_oa/pdfs/`",
        f"- Non-OA / no PDF flagged: **{len(non)}**",
        "",
        "## Open access (PDF on disk)",
        "",
    ]
    for r in sorted([x for x in records if x["oa"]], key=lambda z: z.get("title") or ""):
        lines.append(
            f"- [OA] {r.get('title') or r.get('cite_key')} — `{r.get('arxiv_id')}` — {r.get('pdf_path')}"
        )
    lines += ["", "## Non-OA / unavailable (flagged)", ""]
    for r in sorted(non, key=lambda z: z.get("title") or ""):
        lines.append(
            f"- [NON-OA] {r.get('title') or r.get('cite_key')} — doi=`{r.get('doi')}` — {r.get('status')}"
        )
    (OUT / "REFERENCES_OA.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"OA={oa_n} non_OA={len(non)} -> {OUT}")


if __name__ == "__main__":
    main()
