# Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval

- Source: OpenReview
- Venue: ICLR 2026 Poster
- Paper ID: openreview:f7p0F2X6XN
- Published: 2026-01-26
- Updated: 2026-04-11
- Authors: Yingyi Zhang, Junyi Li, Wenlin Zhang, Pengyue Jia, Xianneng Li, Yichao Wang, Derong Xu, Yi Wen, Huifeng Guo, Yong Liu, Xiangyu Zhao
- Tags: benchmark, context, episodic, retrieval
- Categories: ICLR.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=f7p0F2X6XN

## One-Sentence Summary
Personalized large language models (LLMs) rely on memory retrieval to incorporate user-specific histories, preferences, and contexts.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, episodic, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Personalized large language models (LLMs) rely on memory retrieval to incorporate user-specific histories, preferences, and contexts.

进一步看，论文的核心做法或实验重点可以概括为：Existing approaches either overload the LLM by feeding all the user's past memory into the prompt, which is costly and unscalable, or simplify retrieval into a one-shot similarity search, which captures only surface...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Poster
- 高亮主题命中：benchmark, context, episodic, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：ICLR.cc/2026/Conference/-/Submission

## Abstract Snapshot
Personalized large language models (LLMs) rely on memory retrieval to incorporate user-specific histories, preferences, and contexts. Existing approaches either overload the LLM by feeding all the user's past memory into the prompt, which is costly and unscalable, or simplify retrieval into a one-shot similarity search, which captures only surface matches. Cognitive science, however, shows that human memory operates through a dual process: Familiarity, offering fast but coarse recognition, and Recollection, enabling deliberate, chain-like reconstruction for deeply recovering episodic content. Current systems lack both the ability to perform recollection retrieval and mechanisms to adaptively switch between the dual retrieval paths, leading to either insufficient recall or the inclusion of noise. To address this, we propose RF-Mem (Recollection–Familiarity Memory Retrieval), a familiarity uncertainty-guided dual-path memory retriever. RF-Mem measures the familiarity signal through the mean score and entropy. High familiarity leads to the direct top-$K$ Familiarity retrieval path, while low familiarity activates the Recollection path. In the Recollection path, the system clusters candidate memories and applies $\alpha$-mix with the query to iteratively expand evidence in embedding space, simulating deliberate contextual reconstruction. This design embeds human-like dual-process recognition into the retriever, avoiding full-context overhead and enabling scalable, adaptive personalization. Experiments across three benchmarks and corpus scales demonstrate that RF-Mem consistently outperforms both one-shot retrieval and full-context reasoning under fixed budget and latency constraints. Our code can be found in the Reproducibility Statement.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
