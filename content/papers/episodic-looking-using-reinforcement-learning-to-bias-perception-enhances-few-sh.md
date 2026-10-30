# Episodic looking - using reinforcement learning to bias perception enhances few-shot and continual learning with protection from forgetting

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.38577v1
- Published: 2026-10-28
- Updated: 2026-10-28
- Authors: David Rawlinson, Gideon Kowadlo
- Tags: context, episodic, long-term
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2610.38577v1

## One-Sentence Summary
There is a fundamental contradiction between the desire for models that can generalize, and models that can continuously adapt to recent input with changing statistics.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：There is a fundamental contradiction between the desire for models that can generalize, and models that can continuously adapt to recent input with changing statistics.

进一步看，论文的核心做法或实验重点可以概括为：These conditions, captured in few-shot and continual learning settings, can bias or disrupt learned representations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, episodic, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
There is a fundamental contradiction between the desire for models that can generalize, and models that can continuously adapt to recent input with changing statistics. These conditions, captured in few-shot and continual learning settings, can bias or disrupt learned representations. This harms generalization to a broader context, leaving the model unable to overcome input variance. This paper proposes a solution based on the Complementary Learning System architecture (CLS), in which a Short-Term Memory (STM) delegates generalization to a slow, statistical Long-Term Memory (LTM). Delegation is achieved by working in a space of robust, generalized perceptions produced by the LTM. With this separation, the STM can focus on memorizing recent input and avoiding interference between memories. We show that on an image classification task, the resulting CLS model is more resistant to forgetting in a domain-incremental continual learning setting than a baseline ResNet LTM, and generalizes more effectively in a few-shot setting than other continual learners. In the continual setting, overall accuracy is slightly worse than existing continual learning models, but with a different mix of performance characteristics. Results analysis suggests that the model is limited by the representations and representational plasticity of the LTM. In future work, we will seek to address this by replaying STM memories to the LTM.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
