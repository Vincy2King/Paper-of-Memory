# Variance Restoration over Covariance Rank: Memory-Budgeted Analytic Continual Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.23040v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Elena Voss, Pixel Nomand, Marcus Hale, Sofia Reyes
- Tags: benchmark
- Categories: cs.LG
- URL: http://arxiv.org/abs/2611.23040v1

## One-Sentence Summary
Analytic continual learning replaces iterative gradient updates with closed-form ridge regression over frozen pre-trained representations, summarizing all past sessions in two...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Analytic continual learning replaces iterative gradient updates with closed-form ridge regression over frozen pre-trained representations, summarizing all past sessions in two running sufficient statistics: the...

进一步看，论文的核心做法或实验重点可以概括为：Lifting backbone features into a wide random code of dimension $M \gg D$ substantially improves linear separability across tasks, but forces $Σ_t$ to grow quadratically as $\mathcal{O}(M^2)$.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Analytic continual learning replaces iterative gradient updates with closed-form ridge regression over frozen pre-trained representations, summarizing all past sessions in two running sufficient statistics: the feature autocorrelation matrix $Σ_t$ and the class cross-correlation matrix $Γ_t$. Lifting backbone features into a wide random code of dimension $M \gg D$ substantially improves linear separability across tasks, but forces $Σ_t$ to grow quadratically as $\mathcal{O}(M^2)$. Under a fixed persistent memory envelope $\Bcal$, a learner faces a fundamental structural trade-off: store exact pairwise co-activations inside a narrower feature code, or expand to a wide code while compressing cross-coordinate interactions. We observe that the coordinate self-variances $v_t = \diag(Σ_t)$ and class statistics $Γ_t$ grow only linearly with $M$, whereas off-diagonal interactions dominate memory. We introduce \method (\textbf{Co}ordinate-\textbf{Re}stored \textbf{A}nalytic \textbf{C}ontinual \textbf{L}earning), which retains $(v_t, Γ_t)$ exactly, maintains off-diagonal co-activations through a streaming rank-$q$ factor $F_t$, restores exact diagonal variances via $\Sighat_t = F_t^\top F_t + \Diag(v_t - \diag(F_t^\top F_t))$, and solves the full $M\times C$ normal equations via the Woodbury identity. Across five class-incremental benchmarks on frozen ViT-B/16, \method matches dense full-covariance readouts within $0.09$ points while cutting persistent state by $90.7\%$ ($35.9$ vs.\ $385.3$ MiB). Under equal memory envelopes of $16$--$80$ MiB, prioritizing expansion width $M$ over covariance rank $q$ outperforms exact narrow readouts in $17$ of $18$ configurations by up to $+2.19$ points.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
