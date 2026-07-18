"""Regenerate DenoiseOpt paper/v3 via klaut-research-gateway scientific workflow."""

from __future__ import annotations

import asyncio
import json
import shutil
import sys
from pathlib import Path

# Gateway on PYTHONPATH
GATEWAY = Path(r"C:\Users\Julian\Documents\Programming\github\klaut-pro\klaut-research-gateway")
META = Path(r"C:\Users\Julian\Documents\Programming\github\reeldemo\denoise-opt-meta")
sys.path.insert(0, str(GATEWAY))

from app.config import Settings
from app.services import paper_writer
from app.services.paper_writer.store import load_meta, save_meta, version_dir
from app.services.latex_export import compile_pdf, resolve_latex_engine

OUT_V3 = META / "paper" / "v3"
ART = META / "artifacts"


def build_results_blob(meta_json: dict) -> dict:
    matrix = meta_json["benchmark_matrix_5"]
    naive = next(r for r in matrix if r["algo"] == "naive_dual_cosine")
    top1 = next(r for r in matrix if r["algo"] == "meta_top1")
    return {
        "primary_metric": round(top1["residual"], 4),
        "baseline_residual": round(naive["residual"], 4),
        "naive_residual": round(naive["residual"], 4),
        "delta_residual": round(top1["residual"] - naive["residual"], 4),
        "delta": round(top1["residual"] - naive["residual"], 4),
        "champion": {
            "trial_name": top1["trial_name"],
            "residual": top1["residual"],
            "prior": top1["prior"],
            "shape": top1["shape"],
            "loss_opt_sweeps": meta_json["champion"]["hyper"]["loss_opt_sweeps"],
        },
        "champion_name": top1["trial_name"],
        "meta_top_band": "0.821--0.823",
        "n_trials": meta_json["n_trials"],
        "trial_budget": meta_json["n_trials"],
        "val_n": 2000,
        "fast_val_n": 400,
        "refine_top_k": 12,
        "tile_n": 16,
        "theta_dim": 12,
        "runtime_s": meta_json.get("runtime_seconds") or meta_json.get("elapsed_s") or 141,
        "inner_fit_count": meta_json.get("inner_fit_count", 48),
        "prior_families": [
            "evo_explore",
            "bilevel_loss",
            "pbt_exploit",
            "bayes_local",
            "racing_mid",
            "mo_shape",
            "aggressive",
        ],
        "benchmark_matrix_5": matrix,
        "table_rows": [
            {
                "algo": r["algo"],
                "prior": r.get("prior") or r.get("kind"),
                "residual": round(r["residual"], 4),
                "shape": round(r["shape"], 4),
                "quality": round(r["quality"], 4),
            }
            for r in matrix
        ],
        "residual_definition": (
            "R = clamp(1 - residual_rms / max(ideal_rms, 1e-6), 0, 1), "
            "comparing tiled N=16 engine bake vs ideal no-cliff sibling"
        ),
        "loss_definition": "L = (1-D) + lambda(1-S); inner coordinate descent; outer maximize R",
        "honest_note": (
            "All twenty Pareto-fast residual elites were evo_explore (inner sweeps = 0). "
            "Bi-level / PBT / Bayes loss-opt priors were evaluated but did not win on residual. "
            "Inner L-minimization remains part of the search design as a nested regularizer; "
            "under prolonged residual, lighter evolutionary mutations currently dominate."
        ),
        "literature_used": [
            "VA / BLEP discontinuity control (Valimaki, Esqueda)",
            "Differentiable wavetable / DDSP context (Shan et al.)",
            "Noise2Noise label-free restoration philosophy (Lehtinen et al.)",
            "Bayesian HPO (Snoek et al.; Bischl survey)",
            "PBT-style exploit/mutate",
            "irace racing (Lopez-Ibanez et al.)",
            "MOEA/D multi-objective cues (Zhang & Li)",
        ],
        "literature_screened": [
            "Medical imaging / federated / prompting surveys (off-domain)",
            "Adam as ambient optimizer only",
            "MAML (Finn et al.) — inspirational mechanism, not used (no task-gradient through a deep net)",
        ],
        "limitations": [
            "Residual uses a procedural ideal (no-cliff sibling), not a perceptual MOS.",
            "Bake metrics are not listening tests.",
            "Nested loss budgets are small (48 seeds) by design for 1500-trial throughput.",
            "Results are tied to the reported seed protocol and validation sizes.",
        ],
        "meta_objective": meta_json.get("meta_objective", ""),
        "metrics": {
            "residual": top1["residual"],
            "baseline": naive["residual"],
            "shape": top1["shape"],
        },
    }


LITERATURE = [
    {
        "cite_key": "valimaki2006va",
        "title": "Oscillator and Filter Algorithms for Virtual Analog Synthesis",
        "authors": ["V. Valimaki", "A. Huovilainen"],
        "year": 2006,
        "venue": "Computer Music Journal, 30(2)",
    },
    {
        "cite_key": "esqueda2016aliasing",
        "title": "Aliasing Reduction in Clipped Signals",
        "authors": ["F. Esqueda", "S. Bilbao", "V. Valimaki"],
        "year": 2016,
        "venue": "IEEE Trans. Signal Processing",
    },
    {
        "cite_key": "esqueda2016blamp",
        "title": "Rounding corners with BLAMP",
        "authors": ["F. Esqueda", "V. Valimaki", "S. Bilbao"],
        "year": 2016,
        "venue": "Proc. DAFx",
    },
    {
        "cite_key": "shan2021dwt",
        "title": "Differentiable Wavetable Synthesis",
        "authors": ["S. Shan et al."],
        "year": 2021,
        "venue": "arXiv:2111.10003",
    },
    {
        "cite_key": "lehtinen2018n2n",
        "title": "Noise2Noise: Learning Image Restoration without Clean Data",
        "authors": ["J. Lehtinen et al."],
        "year": 2018,
        "venue": "ICML",
    },
    {
        "cite_key": "snoek2012bo",
        "title": "Practical Bayesian Optimization of Machine Learning Algorithms",
        "authors": ["J. Snoek", "H. Larochelle", "R. P. Adams"],
        "year": 2012,
        "venue": "NeurIPS",
    },
    {
        "cite_key": "bischl2023hpo",
        "title": "Hyperparameter optimization: Foundations, algorithms, best practices",
        "authors": ["B. Bischl et al."],
        "year": 2023,
    },
    {
        "cite_key": "lopez2016irace",
        "title": "The irace package: Iterated racing for automatic algorithm configuration",
        "authors": ["M. Lopez-Ibanez et al."],
        "year": 2016,
        "venue": "Operations Research Perspectives",
    },
    {
        "cite_key": "zhang2007moead",
        "title": "MOEA/D: A Multiobjective Evolutionary Algorithm Based on Decomposition",
        "authors": ["Q. Zhang", "H. Li"],
        "year": 2007,
        "venue": "IEEE Trans. Evolutionary Computation",
    },
    {
        "cite_key": "finn2017maml",
        "title": "Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks",
        "authors": ["C. Finn", "P. Abbeel", "S. Levine"],
        "year": 2017,
        "venue": "ICML",
        "screened": True,
    },
]


ABSTRACT = (
    r"Open wrap seams in periodic wavetable cycles inject audible crackle under cyclic "
    r"playback. DenoiseOpt is a seam-local bake stack $f_\theta$, $\theta\in[0,1]^{12}$, "
    r"scored without paired clean labels. We replace wrap-energy quality $Q$ as the outer "
    r"meta objective with a prolonged residual score $R\in[0,1]$ (1~=~best): the engine's "
    r"tiled DenoiseOpt cycle is compared to an ideal multi-period reference from the same "
    r"seed with open-wrap cliffs withheld ($N{=}16$). The outer loop also nests an inner "
    r"unsupervised loss fit $L=(1-\mathcal{D})+\lambda(1-\mathcal{S})$. Across 1500 "
    r"literature-informed trials, Meta Top~1 \texttt{evo\_explore\_515} reaches residual "
    r"$\approx 0.824$ vs naive DualCosine $\approx 0.698$ on held-out validation "
    r"($N{=}2000$)---a clear $+0.126$ margin---while keeping $\mathcal{S}\approx 1.0$. "
    r"Nested loss-opt priors were searched but did not dominate the residual elite set; "
    r"wide evolutionary mutation did."
)


async def main() -> None:
    papers_dir = META / "artifacts" / "gateway_papers"
    papers_dir.mkdir(parents=True, exist_ok=True)
    settings = Settings(RESEARCH_PAPERS_DIR=str(papers_dir))

    meta_json = json.loads((ART / "denoise_opt_meta_1500.json").read_text(encoding="utf-8"))
    results = build_results_blob(meta_json)

    started = paper_writer.start_paper(
        title="DenoiseOpt: Residual Scoring and Bi-Level Meta-Learning for Wavetable Wrap Crackle",
        authors=[
            {
                "name": "Julian M. Kleber",
                "orcid": "https://orcid.org/0000-0001-5518-0932",
                "email": "julian.m.kleber@gmail.com",
            }
        ],
        abstract_sketch=ABSTRACT,
        repo_links=[
            "https://github.com/reeldemo/reelsynth",
            "https://github.com/reeldemo/denoise-opt-meta",
        ],
        user_needs=(
            "Short technical paper. Honest about evo_explore winning over nested loss opt "
            "under residual. Cite used vs screened literature. Include equation for residual. "
            "Primary numbers: 0.824 vs 0.698 (delta +0.126). Paper version v3 via scientific workflow."
        ),
        settings=settings,
    )
    paper_id = started["paper_id"]
    print("paper_id", paper_id)

    planned = await paper_writer.plan_paper_workflow(
        paper_id,
        results_blob=results,
        literature=LITERATURE,
        use_llm=False,
        settings=settings,
    )
    print("plan", planned["plan_path"], "gaps", planned["open_data_gaps"])

    # Prefer publication figures: copy artifact PNGs under canonical names and
    # point meta.figures paths at those names so results embeds clean paths.
    fig_dir = version_dir(paper_id, load_meta(paper_id, settings).current_version, settings) / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    meta = load_meta(paper_id, settings)
    meta.figures = []
    save_meta(meta, settings)
    for src_name, caption, section in [
        (
            "fig_benchmark_matrix.png",
            "Naive DualCosine vs Meta Top 1--4 under residual (primary), denoise D, and shape S.",
            "results",
        ),
        (
            "fig_pareto_1500.png",
            "Elite residual versus unsupervised-loss proxy after 1500 trials.",
            "results",
        ),
        (
            "fig_prior_families.png",
            "Prior families among residual elites (top-20 / top-4).",
            "results",
        ),
    ]:
        src = ART / src_name
        if not src.is_file():
            continue
        dest = fig_dir / src_name
        shutil.copy2(src, dest)
        from app.services.paper_writer.models import FigureMeta

        meta = load_meta(paper_id, settings)
        meta.figures.append(
            FigureMeta(
                figure_id=src_name.replace(".png", ""),
                path=str(dest),
                plot_type="bar",
                caption=caption,
                section_id=section,
            )
        )
        save_meta(meta, settings)
        print("figure", src_name)

    sections = [
        "abstract",
        "introduction",
        "related_work",
        "methods",
        "experiments",
        "results",
        "discussion",
        "limitations",
        "conclusion",
    ]
    for sid in sections:
        out = await paper_writer.write_paper_subsection(
            paper_id,
            sid,
            literature_refs=LITERATURE,
            use_llm=False,
            settings=settings,
        )
        print("write", sid, out.get("status"), out.get("chars"), out.get("source"))

    revised = await paper_writer.revise_paper_workflow(
        paper_id, use_llm=False, settings=settings
    )
    print("revise", revised["notes_path"])

    exported = paper_writer.compile_paper(
        paper_id, compile_pdf_flag=False, settings=settings
    )
    tex_src = Path(exported["tex_path"])
    vdir = tex_src.parent
    print("exported", tex_src)

    # Ship to paper/v3 with publication figures and polished includes
    OUT_V3.mkdir(parents=True, exist_ok=True)
    for child in list(OUT_V3.iterdir()):
        try:
            if child.is_dir():
                shutil.rmtree(child, ignore_errors=True)
            else:
                child.unlink(missing_ok=True)
        except OSError:
            pass
    (OUT_V3 / "figures").mkdir(exist_ok=True)
    for name in (
        "fig_benchmark_matrix.png",
        "fig_pareto_1500.png",
        "fig_prior_families.png",
    ):
        shutil.copy2(ART / name, OUT_V3 / "figures" / name)

    # Copy workflow artifacts for audit trail
    for name in ("plan.md", "plan.json", "revision_notes.md", "meta.json", "changelog.jsonl"):
        src = vdir / name
        if src.is_file():
            shutil.copy2(src, OUT_V3 / name)
    shutil.copytree(vdir / "subsections", OUT_V3 / "subsections")
    if (vdir / "drafts").is_dir():
        shutil.copytree(vdir / "drafts", OUT_V3 / "drafts")

    # Polish main.tex: strip duplicate figure blocks; keep canonical names only
    tex = tex_src.read_text(encoding="utf-8")
    # Remove any leftover UUID figure includes if canonical ones exist
    import re

    tex = re.sub(
        r"\\begin\{figure\}\[htbp\]\s*\\centering\s*\\includegraphics\[width=0\.88\\textwidth\]\{figures/fig_[0-9a-f]{8}\.png\}.*?\\end\{figure\}",
        "",
        tex,
        flags=re.S,
    )
    if "fig_benchmark_matrix.png" not in tex:
        fig_block = r"""
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.92\textwidth]{figures/fig_benchmark_matrix.png}
  \caption{Naive DualCosine vs Meta Top~1--4 under residual (primary), $\mathcal{D}$, and $\mathcal{S}$.}
  \label{fig:matrix}
\end{figure}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.88\textwidth]{figures/fig_pareto_1500.png}
  \caption{Elite residual vs unsupervised-loss proxy after 1500 trials.}
  \label{fig:pareto}
\end{figure}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.82\textwidth]{figures/fig_prior_families.png}
  \caption{Prior families among residual elites (top-20 / top-4).}
  \label{fig:priors}
\end{figure}
"""
        if r"\section{Discussion}" in tex:
            tex = tex.replace(r"\section{Discussion}", fig_block + "\n" + r"\section{Discussion}")
        else:
            tex += "\n" + fig_block

    # Prefer pdflatex-friendly preamble on Windows if xelatex fonts missing
    if r"\usepackage{fontspec}" in tex:
        tex = tex.replace(
            r"\usepackage{fontspec}" + "\n" + r"\usepackage{unicode-math}" + "\n",
            r"\usepackage[T1]{fontenc}" + "\n"
            + r"\usepackage[utf8]{inputenc}" + "\n"
            + r"\usepackage{lmodern}" + "\n",
        )

    # Author block readability
    tex = tex.replace(
        r"\author{Julian M. Kleber\\ORCID: https://orcid.org/0000-0001-5518-0932; julian.m.kleber@gmail.com}",
        r"\author{Julian~M.~Kleber\\ORCID: \href{https://orcid.org/0000-0001-5518-0932}{0000-0001-5518-0932}\\Email: \href{mailto:julian.m.kleber@gmail.com}{julian.m.kleber@gmail.com}}",
    )

    # Version note under title date
    if r"\date{\today}" in tex:
        tex = tex.replace(
            r"\date{\today}",
            r"\date{18 July 2026 \\ \small Paper version \texttt{v3} (scientific writing workflow)}",
        )

    (OUT_V3 / "main.tex").write_text(tex, encoding="utf-8")

    # Compile PDF with system pdflatex (gateway helper may miss PATH)
    import subprocess

    for _ in range(2):
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "main.tex"],
            cwd=OUT_V3,
            check=False,
            capture_output=True,
        )
    pdf_path = OUT_V3 / "main.pdf"
    print("pdf", pdf_path if pdf_path.is_file() else None, "exists", pdf_path.is_file())

    # Pointer
    (META / "paper" / "main.tex").write_text(
        "% Latest paper version lives in paper/v3/\n"
        "% Compile: cd paper/v3 && pdflatex main.tex\n",
        encoding="utf-8",
    )
    print("DONE", OUT_V3)


if __name__ == "__main__":
    asyncio.run(main())
