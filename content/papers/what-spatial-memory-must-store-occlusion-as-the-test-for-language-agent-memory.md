# What Spatial Memory Must Store: Occlusion as the Test for Language-Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.10299v1
- Published: 2026-06-09
- Updated: 2026-06-09
- Authors: Doeon Kwon, Junho Bang
- Tags: agent
- Categories: cs.AI, cs.CV, cs.MA
- URL: http://arxiv.org/abs/2606.10299v1

## One-Sentence Summary
Language-agent "memory palace" systems anchor each memory to a world coordinate, on the intuition that geometry adds something text cannot.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language-agent "memory palace" systems anchor each memory to a world coordinate, on the intuition that geometry adds something text cannot.

进一步看，论文的核心做法或实验重点可以概括为：We make that intuition testable and report three results.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.CV, cs.MA

## Abstract Snapshot
Language-agent "memory palace" systems anchor each memory to a world coordinate, on the intuition that geometry adds something text cannot. We make that intuition testable and report three results. First, the memory-palace default of folding spatial proximity into a linear blend beside recency and importance does not help and can hurt: in a pre-registered recall experiment the shipped blend fails its own frozen test (mean Delta-Hit@5 -0.0375, Wilcoxon p=0.306), sitting at a position-blind baseline, while a geometry-led weighting wins decisively (+0.3208, p<10^-15): geometry must lead recall when the query regime is spatial. Second, memory recall and visibility must be separated: recall is occlusion-blind by design (you correctly remember the next room behind a wall), while visibility is a perception predicate over stored geometry that the live system never computed. A one-line ray-versus-voxel digital differential analyzer (DDA), re-pointed from the gaze ray the agent already casts, supplies it: text and the live FoV cone both score 0.000 on 849 behind-wall targets while cone-plus-DDA reaches 0.982 (exact McNemar p<10^-6); coordinate recall separately resolves near-duplicate locations a cosine null cannot (1.000 vs 0.533, n=150). Third, the visibility predicate is confirmed live under a git-committed pre-registration (SPMEM-OCC-LIVE-v1: eight scripted worlds, automated oracle scoring, 96 behind-wall targets, false-visible 1.000->0.000, pooled exact McNemar p=2.5x10^-29), a run that surfaced and fixed a real relay anchor defect. We concede that occlusion-needs-geometry is near-tautological; the contribution is the measurement and isolation, separating what spatial memory must store from how it is read. These pilots power a frozen confirmatory study (SPMEM-ZERO-REAL-PREREG-v1); the full human-authored multi-world study with blind raters remains future work.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
