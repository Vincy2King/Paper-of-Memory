# XMind: Thinking Twice via Cross-Memory Reasoning for LLM-Based Autonomous Driving

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.32209v1
- Published: 2026-11-24
- Updated: 2026-11-24
- Authors: Zuyi Guo, Xianjie Dai, Lei Yang, Xiaocong Zhao, Jingguang Li, Kitae Jang, Heye Huang
- Tags: agent, context, episodic, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.32209v1

## One-Sentence Summary
Memory-augmented large language model (LLM) driving agents can reuse past experience, yet previously learned corrections often fail to transfer when traffic conditions change.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented large language model (LLM) driving agents can reuse past experience, yet previously learned corrections often fail to transfer when traffic conditions change.

进一步看，论文的核心做法或实验重点可以概括为：A key limitation is that existing memories mainly record observed outcomes, providing little evidence about alternative actions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, retrieval
- 检索关键词命中：episodic memory, memory augmented, memory reasoning, memory-augmented, working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Memory-augmented large language model (LLM) driving agents can reuse past experience, yet previously learned corrections often fail to transfer when traffic conditions change. A key limitation is that existing memories mainly record observed outcomes, providing little evidence about alternative actions. We introduce XMind, a training-free framework that enables LLM-based driving to "Think Twice" through cross-memory reasoning. XMind integrates working memory of recent traffic states with episodic memory of critical risk events. The agent first makes an initial decision from the current context and then cross-checks it against retrieved historical experience. If a conflict arises, it makes a second decision guided by the retrieved evidence. To construct reliable episodic memory, XMind evaluates alternative actions through counterfactual rollouts under perturbed traffic conditions and stores the verified outcomes as structured risk capsules. These capsules are retrieved by jointly matching spatial risk patterns and scenario semantics. Across closed-loop highway simulations, XMind achieves success rates of 83.3-93.3%, exceeding the strong baseline by 6.6 percentage points on average. Evaluation on K-Risk further demonstrates lower decision risk on unseen real-world high-risk interactions. Ablation studies confirm the complementary benefits of working memory, risk-text retrieval, and counterfactual verification. Code is available at https://github.com/xiangxiangliuwo/XMind

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
