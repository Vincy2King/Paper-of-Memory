# Efficient Allocation of Working Memory Resource for Utility Maximization in Humans and Recurrent Neural Networks

- Source: OpenReview
- Venue: NeurIPS 2025 poster
- Paper ID: openreview:eYVFs6TfQ0
- Published: 2025-09-18
- Updated: 2026-04-21
- Authors: Qingqing Yang, Hsin-Hung Li
- Tags: context
- Categories: NeurIPS.cc/2025/Conference/-/Submission
- URL: https://openreview.net/forum?id=eYVFs6TfQ0

## One-Sentence Summary
Working memory (WM) supports the temporary retention of task-relevant information.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `NeurIPS 2025 poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：Working memory (WM) supports the temporary retention of task-relevant information.

进一步看，论文的核心做法或实验重点可以概括为：It is limited in capacity and inherently noisy.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：NeurIPS 2025 poster
- 高亮主题命中：context
- 检索关键词命中：working memory
- 来源分类信息：NeurIPS.cc/2025/Conference/-/Submission

## Abstract Snapshot
Working memory (WM) supports the temporary retention of task-relevant information. It is limited in capacity and inherently noisy. The ability to flexibly allocate WM resource is a hallmark of adaptive behavior. While it is well established that WM resource can be prioritized via selective attention, whether they can be allocated based on reward incentive alone remains under debate—raising open questions about whether humans can efficiently allocate WM resource based on utility. To address this, we conducted behavioral experiments using orientations as stimuli. Participants first learned stimulus–reward associations and then performed a delayed estimate WM task. We found that WM precision, indexed by the variability of memory reports, reflected both natural stimulus priors and utility-based allocation. The effects from reward and prior on memory variability both grew over time, indicating their effects in stabilizing memory representations. In contrast, memory bias was largely unaffected by time or reward. To interpret these findings, we extended efficient coding theory by incorporating time and reformulating the objective from minimizing estimation loss to maximizing expected utility. We showed that the behavioral results were consistent with an observer that efficiently allocates WM resource over time to maximize utility. Lastly, we trained recurrent neural networks (RNNs) to perform the same WM task under a 2×2 design: prior (uniform vs. natural) × reward policy (baseline vs. reward context). Human-like behaviors emerged in RNNs: memory was more stable (lower variability) for stimuli associated with higher probability or rewards, and these effects increased over time. Transfer learning showed that recurrent dynamics were crucial for adapting to different priors and reward policies. Together, these results provide converging behavioral and computational evidence that WM resource allocation is shaped by environmental statistics and rewards, offering insight into how intelligent systems can dynamically optimize memory for utility under resource constraints.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
