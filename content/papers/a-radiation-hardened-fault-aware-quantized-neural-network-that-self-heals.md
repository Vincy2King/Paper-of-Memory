# A Radiation-Hardened, Fault-Aware Quantized Neural Network That Self-Heals

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.27621v1
- Published: 2026-10-20
- Updated: 2026-10-20
- Authors: Peter Xiangyuan Ma, Joshua S. Bloom
- Tags: benchmark
- Categories: astro-ph.IM, cs.LG, hep-ex, nucl-ex, physics.ins-det
- URL: http://arxiv.org/abs/2610.27621v1

## One-Sentence Summary
Deep learning (DL) models are increasingly being deployed into radiation-challenging environments in spacecraft, particle accelerators, and, soon, space-based data centers.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Deep learning (DL) models are increasingly being deployed into radiation-challenging environments in spacecraft, particle accelerators, and, soon, space-based data centers.

进一步看，论文的核心做法或实验重点可以概括为：Instantiated as a learned orchestration of numbers stored in persistent memory, models are susceptible to continual degradation as high-energy particles corrupt data.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：astro-ph.IM, cs.LG, hep-ex, nucl-ex

## Abstract Snapshot
Deep learning (DL) models are increasingly being deployed into radiation-challenging environments in spacecraft, particle accelerators, and, soon, space-based data centers. Instantiated as a learned orchestration of numbers stored in persistent memory, models are susceptible to continual degradation as high-energy particles corrupt data. At inference time, new data passed through the network fundamentally break the off-line assumptions and guarantees of a static model determined during training. To preserve the quality and efficacy of the models, fault tolerance against bit flips is a clear objective. In this work we developed a runtime method for repairing the quantized weights of neural networks (NNs) after bit flips on commodity, commercial off-the-shelf (COTS) hardware, without storing extra replicas. Our work extends the well-established Fault-Aware Training (FAT) paradigm by adding an alignment penalty to concentrate undamaged activations and weights into a low-rank subspace, and we then reconstruct flagged corrupted coordinates from the uncorrupted survivors. We call this method {\it Projection Healing} and apply it to six regression benchmarks on quantized NNs. Holding a FAT checkpoint fixed and toggling only the runtime heal gives a further ${\sim}23\%$ reduction in the native-unit excess integral. Across those datasets the method extends the operational scrub interval by a median of $2.04\times$ at a $+5\%$ RMSE degradation and $1.96\times$ at $+50\%$, compared with $1.62\times$ and $1.07\times$ for classical Single Error Correction, Double Error Detection (SECDED). This introduces a new path towards designing resilient data-driven models, complementing established hardware redundancy, ECC, and FAT-based techniques.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
