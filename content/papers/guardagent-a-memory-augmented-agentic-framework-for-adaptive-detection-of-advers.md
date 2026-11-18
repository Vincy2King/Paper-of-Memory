# GuardAgent: A Memory-Augmented Agentic Framework for Adaptive Detection of Adversarial Promotions in LLM-Based Recommendation

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.22274v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Shiyi Yang, Xinshu Li, Chen Wang, Xiwei Xu, Liming Zhu, Lina Yao
- Tags: agent
- Categories: cs.IR, cs.CR
- URL: http://arxiv.org/abs/2611.22274v1

## One-Sentence Summary
In traditional recommender systems (RSs), textual information typically serves as auxiliary signals for representation learning.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In traditional recommender systems (RSs), textual information typically serves as auxiliary signals for representation learning.

进一步看，论文的核心做法或实验重点可以概括为：In contrast, in LLM-based RSs, textual information becomes the primary medium for recommendation generation through semantic understanding and reasoning.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.IR, cs.CR

## Abstract Snapshot
In traditional recommender systems (RSs), textual information typically serves as auxiliary signals for representation learning. In contrast, in LLM-based RSs, textual information becomes the primary medium for recommendation generation through semantic understanding and reasoning. This shift fundamentally changes the attack surface, making promotion-driven manipulations more feasible, effective, and harder to detect. However, effectively detecting such attacks remains largely unexplored. To fill this gap, we present the first systematic study on detecting promotion-driven attacks against LLM-based RSs, aiming to safeguard next-generation recommendation platforms. Specifically, we propose GuardAgent, a novel LLM-powered agentic detection framework that operates through a loop of Perception, Action, Reflection and Memory. In contrast to conventional LLM-based detectors that function in a static, one-off, and opaque fashion, GuardAgent continually learns and self-evolves to adapt to unseen threat patterns while generating explainable reasoning traces and outcomes. Extensive experiments on real-world datasets demonstrate that GuardAgent achieves state-of-the-art generalization performance, laying the foundation for robust and trustworthy recommendation in practical settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
