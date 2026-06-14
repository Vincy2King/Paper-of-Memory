# Renormalization Phenomenology in LLM Agent Memory Compression: Scaling Laws, Fixed Points, and Anomalous Summarization

- Source: OpenReview
- Venue: PAI 2026 Conference Submission
- Paper ID: openreview:YVXmOLdILi
- Published: 2026-06-14
- Updated: 2026-06-14
- Authors: Unknown
- Tags: agent, benchmark, compression, long-term
- Categories: PAI/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=YVXmOLdILi

## One-Sentence Summary
Agent memory compression is typically treated as a heuristic problem: truncate, drop, or summarize.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `PAI 2026 Conference Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Agent memory compression is typically treated as a heuristic problem: truncate, drop, or summarize.

进一步看，论文的核心做法或实验重点可以概括为：We instead ask whether agent memory exhibits the phenomenology of a statistical physical system under coarse-graining—scaling laws, fixed points, and universality classes.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：PAI 2026 Conference Submission
- 高亮主题命中：agent, benchmark, compression, long-term
- 检索关键词命中：agent memory, memory compression
- 来源分类信息：PAI/2026/Conference/-/Submission

## Abstract Snapshot
Agent memory compression is typically treated as a heuristic problem: truncate, drop, or summarize. We instead ask whether agent memory exhibits the phenomenology of a statistical physical system under coarse-graining—scaling laws, fixed points, and universality classes. Motivated by the proven equivalence between Information Bottleneck and the Renormalization Group, we measure the compression-retention trade-off for three families of compression operators on the LoCoMo long-term dialogue benchmark. We find: (i) geometric truncation exhibits a clean monotonic decline consistent with a power-law scaling form; (ii) LLM-based summarization exhibits anomalous, non-monotonic behavior, violating naive scaling expectations; and (iii) iterated summarization converges to semantic fixed points within approximately 5 iterations, with representations stabilizing at approximately 40 words independent of initial length. These results suggest that principled, information-theoretically grounded compression operators—rather than the ad-hoc LLM summarization dominant in current agent memory systems—are needed to obtain the clean renormalization behavior that physical theories predict.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
