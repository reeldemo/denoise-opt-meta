"""Paper layout/protocol cleanup for v14 (one-shot)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUB = ROOT / "subsections"


def replace_all(path: Path, pairs: list[tuple[str, str]]) -> None:
    t = path.read_text(encoding="utf-8")
    orig = t
    for a, b in pairs:
        if a not in t:
            print(f"WARN missing in {path.name}: {a[:60]!r}...")
            continue
        t = t.replace(a, b)
    if t != orig:
        path.write_text(t, encoding="utf-8", newline="\n")
        print("updated", path.relative_to(ROOT))


def main() -> None:
    # --- results.tex: drop REPRO; shrink/move figures ---
    replace_all(
        SUB / "results.tex",
        [
            (
                "Commands live in \\texttt{REPRO.md}.\n",
                "The evaluation protocol is stated in Section~\\ref{sec:experiments}.\n",
            ),
            (
                "Figures~\\ref{fig:sota-heatmap}--\\ref{fig:sota-method-bars} plot the same ranking.\n",
                "Appendix Figures~\\ref{fig:sota-heatmap}--\\ref{fig:sota-method-bars} plot the same ranking.\n",
            ),
            (
                r"""\begin{figure*}[htbp]
  \centering
  \includegraphics[width=0.92\textwidth]{figures/fig_sota_heatmap.png}
  \caption{Colorblind-safe (\texttt{cividis}) heatmap of mean $R_{\mathrm{blend}}$ for selected methods $\times$ generative families (2 seeds each). Higher is better.}
  \label{fig:sota-heatmap}
\end{figure*}

\begin{figure*}[htbp]
  \centering
  \includegraphics[width=0.92\textwidth]{figures/fig_sota_method_bars.png}
  \caption{Multi-family mean $R_{\mathrm{blend}}$ by method (same $20$-waveform board as Table~\ref{tab:sota-main}).}
  \label{fig:sota-method-bars}
\end{figure*}
""",
                "",
            ),
            (
                r"""\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{figures/fig_search_learning_curve.png}
  \caption{Hybrid search learning curves under $R_{\mathrm{blend}}$ (seed \texttt{1902771841}).
    Left: short FitCell ($1{,}200$ evaluations; champ.\ ${\approx}0.9695$).
    Right: FitCell-to-plateau ($750$ evaluations; champ.\ ${\approx}0.9912$).
    Dual Cosine and the frozen Noise2Noise gate are marked on both panels.}
  \label{fig:search-learning-curve}
\end{figure*}
""",
                r"""\begin{figure}[t]
  \centering
  \includegraphics[width=\columnwidth]{figures/fig_search_learning_curve.png}
  \caption{Hybrid search learning curves under $R_{\mathrm{blend}}$ (seed \texttt{1902771841}).
    Left: short FitCell ($1{,}200$ evaluations; champ.\ ${\approx}0.9695$).
    Right: FitCell-to-plateau ($750$ evaluations; champ.\ ${\approx}0.9912$).}
  \label{fig:search-learning-curve}
\end{figure}
""",
            ),
            (
                r"""\begin{figure*}[htbp]
  \centering
  \includegraphics[width=0.85\textwidth]{figures/fig_n2n_vs_ours_bars.png}
  \caption{Canonical holdout $R_{\mathrm{blend}}$: N2N and seq baselines vs Ours (locked hybrid).
""",
                r"""\begin{figure}[t]
  \centering
  \includegraphics[width=\columnwidth]{figures/fig_n2n_vs_ours_bars.png}
  \caption{Canonical holdout $R_{\mathrm{blend}}$: N2N and seq baselines vs Ours (locked hybrid).
""",
            ),
            (
                "\\label{fig:n2n-vs-ours}\n\\end{figure*}",
                "\\label{fig:n2n-vs-ours}\n\\end{figure}",
            ),
            (
                r"""\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{figures/fig_va_seam_techniques.png}
  \caption{Classical VA seam techniques on one cracked sine{+}cliff tile (seed~\texttt{20260719}, tile~46, $|wrap|{=}2.283$, $L{=}256$, three tiled periods). Yellow band marks the first seam neighborhood. Panel tile $R_{\mathrm{blend}}$ (1~=~best): (a)~ideal (unscored sibling). (b)~cracked engine $0.897$. (c)~BLIT/BLEP $0.385$. (d)~PolyBLEP $0.726$. (e)~BLAMP $0.897$ (near no-bake on value cliffs). (f)~DualCosine $0.300$. Colorblind-safe hues with distinct linestyles for B\&W print. Batch means appear in Table~\ref{tab:va-seam-blep}. Accessibility: six-panel comparison of ideal, cracked, BLIT/BLEP, PolyBLEP, BLAMP, and DualCosine.}
  \label{fig:va-seam-techniques}
\end{figure*}
""",
                r"""\begin{figure}[t]
  \centering
  \includegraphics[width=\columnwidth]{figures/fig_va_seam_techniques.png}
  \caption{Classical VA seam techniques on one cracked sine{+}cliff tile
  (seed~\texttt{20260719}, tile~46).
  (a)~ideal; (b)~cracked engine; (c)~BLIT/BLEP; (d)~PolyBLEP; (e)~BLAMP; (f)~DualCosine.
  Batch means: Table~\ref{tab:va-seam-blep}.}
  \label{fig:va-seam-techniques}
\end{figure}
""",
            ),
            # Move end-of-results inference/classical figures block note — leave but shrink
            (
                "\\includegraphics[width=0.96\\columnwidth]{figures/fig_inference_vs_residual.png}",
                "\\includegraphics[width=0.85\\columnwidth]{figures/fig_inference_vs_residual.png}",
            ),
            (
                "\\includegraphics[width=0.96\\columnwidth]{figures/fig_inference_latency_bars.png}",
                "\\includegraphics[width=0.85\\columnwidth]{figures/fig_inference_latency_bars.png}",
            ),
            (
                "\\includegraphics[width=0.96\\columnwidth]{figures/fig_classical_vs_ai_scatter.png}",
                "\\includegraphics[width=0.85\\columnwidth]{figures/fig_classical_vs_ai_scatter.png}",
            ),
            (
                "\\includegraphics[width=0.96\\columnwidth]{figures/fig_classical_vs_ai_bars.png}",
                "\\includegraphics[width=0.85\\columnwidth]{figures/fig_classical_vs_ai_bars.png}",
            ),
        ],
    )

    # Append moved SOTA figs into appendix_supplement
    app = SUB / "appendix_supplement.tex"
    at = app.read_text(encoding="utf-8")
    insert = r"""
\subsection{Multi-family ranking plots}
\label{sec:app-sota-plots}

\begin{figure}[t]
  \centering
  \includegraphics[width=\columnwidth]{figures/fig_sota_method_bars.png}
  \caption{Multi-family mean $R_{\mathrm{blend}}$ by method
  (same $20$-waveform board as Table~\ref{tab:sota-main}).}
  \label{fig:sota-method-bars}
\end{figure}

\begin{figure*}[t]
  \centering
  \includegraphics[width=0.92\textwidth]{figures/fig_sota_heatmap.png}
  \caption{Colorblind-safe (\texttt{cividis}) heatmap of mean $R_{\mathrm{blend}}$
  for selected methods $\times$ generative families (2 seeds each). Higher is better.}
  \label{fig:sota-heatmap}
\end{figure*}

"""
    if "fig:sota-method-bars" not in at:
        # insert after first subsection or at top after section header
        marker = "\\subsection{Matched outer-loop bake-off}"
        if marker in at:
            at = at.replace(marker, insert + marker, 1)
        else:
            at = insert + at
        app.write_text(at, encoding="utf-8", newline="\n")
        print("updated appendix_supplement.tex (sota figs)")

    # --- introduction ---
    replace_all(
        SUB / "introduction.tex",
        [
            (
                "and released code/artifacts (\\texttt{REPRO.md}).",
                "and released code/artifacts (Section~\\ref{sec:ethics}).",
            ),
            (
                "\\includegraphics[width=\\textwidth]{figures/fig_intro_sine_problem.png}",
                "\\includegraphics[width=0.95\\textwidth]{figures/fig_intro_sine_problem.png}",
            ),
        ],
    )

    # --- ethics: no REPRO.md; point to paper repo ---
    replace_all(
        SUB / "ethics.tex",
        [
            (
                """Exact command templates live in this paper folder's \\texttt{REPRO.md} and in
\\href{https://github.com/reeldemo/reelsynth/blob/main/docs/superpowers/specs/2026-07-31-fitcell-converge-meta-search-design.md}{the v14 converge design note}.
Frozen numbers live under
\\href{https://github.com/reeldemo/reelsynth/tree/main/brand/artifacts}{brand/artifacts}
(e.g.\\
\\href{https://github.com/reeldemo/reelsynth/blob/main/brand/artifacts/sota_matrix.json}{\\texttt{sota\\_matrix.json}},
\\href{https://github.com/reeldemo/reelsynth/tree/main/brand/artifacts/meta_approach_compare_v13_rblend}{\\texttt{meta\\_approach\\_compare\\_v13\\_rblend/}},
\\href{https://github.com/reeldemo/reelsynth/tree/main/brand/artifacts/meta_approach_compare_v14_converge}{\\texttt{meta\\_approach\\_compare\\_v14\\_converge/}},
\\href{https://github.com/reeldemo/reelsynth/blob/main/brand/artifacts/holdout_multiseed_v13/multiseed_summary.json}{\\texttt{multiseed\\_summary.json}}).
""",
                """Frozen score matrices and search histories ship with the paper repository
\\url{https://github.com/reeldemo/denoiseopt-paper}
(and mirrored experimental runners under \\url{https://github.com/reeldemo/reelsynth}).
""",
            ),
            (
                """Primary code lives at \\url{https://github.com/reeldemo/reelsynth}
(search runner:
\\href{https://github.com/reeldemo/reelsynth/blob/main/scripts/overnight_gpu_rl_arch.py}{\\texttt{overnight\\_gpu\\_rl\\_arch.py}},
matched-$5$k bake-off:
\\href{https://github.com/reeldemo/reelsynth/blob/main/scripts/bench_meta_approaches_5k.py}{\\texttt{bench\\_meta\\_approaches\\_5k.py}},
hybrid-only FitCell-to-convergence launcher:
\\href{https://github.com/reeldemo/reelsynth/blob/main/scripts/launch_v14_converge_search.ps1}{\\texttt{launch\\_v14\\_converge\\_search.ps1}},
SOTA bench:
\\href{https://github.com/reeldemo/reelsynth/blob/main/scripts/bench_sota_matrix.py}{\\texttt{bench\\_sota\\_matrix.py}},
VA seam:
\\href{https://github.com/reeldemo/reelsynth/blob/main/scripts/baselines/va_seam_blep.py}{\\texttt{va\\_seam\\_blep.py}}),
with paper companion at \\url{https://github.com/reeldemo/denoise-opt-meta}.
CUDA benches need Python~3.12, PyTorch~$2.6$+CUDA~12.4, and NumPy/matplotlib; Rust/\\texttt{cargo} builds the separate engine hardness probe.
""",
                """Paper sources, frozen figure JSONs, and build scripts live at
\\url{https://github.com/reeldemo/denoiseopt-paper}.
Experimental search runners remain at \\url{https://github.com/reeldemo/reelsynth}.
CUDA benches need Python~3.12, PyTorch~$2.6$+CUDA~12.4, and NumPy/matplotlib.
""",
            ),
            (
                """Frozen evaluation artifacts (JSON matrices, search histories, fitted champions) are published with the companion repositories:
\\url{https://github.com/reeldemo/reelsynth}
(\\href{https://github.com/reeldemo/reelsynth/tree/main/brand/artifacts}{brand/artifacts})
and
\\url{https://github.com/reeldemo/denoise-opt-meta}
(this paper folder's \\texttt{figures/} plus aggregate JSONs).
Tables regenerate from those files via the named bench scripts;
figures regenerate with
\\href{https://github.com/reeldemo/reelsynth/blob/main/scripts/bench_meta_approaches_5k.py}{\\texttt{bench\\_meta\\_approaches\\_5k.py --aggregate-only}}
and
\\href{https://github.com/reeldemo/reelsynth/blob/main/scripts/plot_paper_dataset_and_comparison_figures.py}{\\texttt{plot\\_paper\\_dataset\\_and\\_comparison\\_figures.py}};
the PDF rebuilds with \\texttt{build.ps1} in this folder.
No private studio recordings were used.
""",
                """Frozen evaluation artifacts (JSON matrices, search histories, fitted champions)
are published at \\url{https://github.com/reeldemo/denoiseopt-paper}
under \\texttt{figures/}.
The PDF rebuilds with \\texttt{build.ps1} in that repository.
No private studio recordings were used.
""",
            ),
        ],
    )

    # --- conclusion ---
    replace_all(
        SUB / "conclusion.tex",
        [
            (
                "Code: \\url{https://github.com/reeldemo/reelsynth}, \\url{https://github.com/reeldemo/denoise-opt-meta}.",
                "Paper repository: \\url{https://github.com/reeldemo/denoiseopt-paper}.",
            ),
        ],
    )

    # --- main.tex footer link ---
    replace_all(
        ROOT / "main.tex",
        [
            (
                "\\url{https://github.com/reeldemo/reelsynth},",
                "\\url{https://github.com/reeldemo/denoiseopt-paper},",
            ),
        ],
    )

    # --- listening / transfer: shrink figure* ---
    for rel, pairs in [
        (
            "results_eval_listening.tex",
            [
                (
                    "\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{figures/fig_vibrato_spectrogram.png}",
                    "\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{figures/fig_vibrato_spectrogram.png}",
                ),
                ("\\label{fig:vibrato-spectrogram}\n\\end{figure*}", "\\label{fig:vibrato-spectrogram}\n\\end{figure}"),
                (
                    "\\begin{figure*}[htbp]\n  \\centering\n  \\includegraphics[width=\\textwidth]{figures/fig_hear_samples_panel.png}",
                    "\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{figures/fig_hear_samples_panel.png}",
                ),
                ("\\label{fig:hear-samples-panel}\n\\end{figure*}", "\\label{fig:hear-samples-panel}\n\\end{figure}"),
                (
                    "\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{figures/fig_wt_diversity_gallery.png}",
                    "\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{figures/fig_wt_diversity_gallery.png}",
                ),
                ("\\label{fig:wt-diversity-gallery}\n\\end{figure*}", "\\label{fig:wt-diversity-gallery}\n\\end{figure}"),
            ],
        ),
        (
            "results_transfer.tex",
            [
                (
                    "\\includegraphics[width=\\textwidth,height=0.38\\textheight,keepaspectratio]{figures/fig_signal_heal_transfer.png}",
                    "\\includegraphics[width=0.95\\textwidth]{figures/fig_signal_heal_transfer.png}",
                ),
            ],
        ),
        (
            "results_transfer_latency.tex",
            [
                (
                    "\\includegraphics[width=\\textwidth,height=0.36\\textheight,keepaspectratio]{figures/fig_signal_heal_transfer_latency.png}",
                    "\\includegraphics[width=0.95\\textwidth]{figures/fig_signal_heal_transfer_latency.png}",
                ),
            ],
        ),
        (
            "appendix_supplement.tex",
            [
                (
                    "\\includegraphics[width=\\textwidth,height=0.36\\textheight,keepaspectratio]{figures/fig_signal_heal_transfer_latency.png}",
                    "\\includegraphics[width=0.92\\textwidth]{figures/fig_signal_heal_transfer_latency.png}",
                ),
                (
                    "\\includegraphics[width=\\textwidth]{figures/search_panel.png}",
                    "\\includegraphics[width=0.92\\textwidth]{figures/search_panel.png}",
                ),
            ],
        ),
    ]:
        replace_all(SUB / rel, pairs)

    print("done layout scrub")


if __name__ == "__main__":
    main()
