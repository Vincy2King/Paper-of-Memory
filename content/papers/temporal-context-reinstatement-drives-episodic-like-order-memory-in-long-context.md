# Temporal Context Reinstatement Drives Episodic-Like Order Memory in Long-Context Language Models

- Source: OpenReview
- Venue: ICML 2026 regular
- Paper ID: openreview:sycSMgogxM
- Published: 2026-04-30
- Updated: 2026-07-23
- Authors: Mathis Pink, Vy A. Vo, Qinyuan Wu, Jianing Mu, Javier S. Turek, Uri Hasson, Kenneth A. Norman, Sebastian Michelmann, Alexander Huth, Mariya Toneva
- Tags: context, episodic, long-term, retrieval
- Categories: ICML.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=sycSMgogxM

## One-Sentence Summary
Human episodic memory supports the retrieval of experiences that unfold over extended timescales, yet the computational mechanisms underlying this ability remain debated due to...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic, long-term, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICML 2026 regular` 这个 venue 相关。

从摘要来看，作者主要关注的是：Human episodic memory supports the retrieval of experiences that unfold over extended timescales, yet the computational mechanisms underlying this ability remain debated due to the limited mechanistic accessibility in...

进一步看，论文的核心做法或实验重点可以概括为：Long-context LLMs may offer promising ways to reveal plausible computational mechanisms that drive this type of retrieval.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICML 2026 regular
- 高亮主题命中：context, episodic, long-term, retrieval
- 检索关键词命中：episodic memory, long-term memory
- 来源分类信息：ICML.cc/2026/Conference/-/Submission

## Abstract Snapshot
Human episodic memory supports the retrieval of experiences that unfold over extended timescales, yet the computational mechanisms underlying this ability remain debated due to the limited mechanistic accessibility in long-term memory experiments in humans. Long-context LLMs may offer promising ways to reveal plausible computational mechanisms that drive this type of retrieval. Here, we investigate whether and how LLMs capture the core behavioral signatures of episodic memory via a temporal order memory task. Using a new dataset of human behavior based on memory of a full-length novel, we show that models exhibit the same characteristic distance effect observed in humans on this task. We next apply long-context mechanistic interpretability analyses to uncover how models solve this task, and find that model performance relies on a one-dimensional temporal code that is reinstated during retrieval by a single time-reinstatement attention head. These findings support temporal context reinstatement as an important mechanism for episodic-like temporal-order memory in LLMs, offering new insights into how temporal aspects of long-term episodic memory may be instantiated in both artificial and biological systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
