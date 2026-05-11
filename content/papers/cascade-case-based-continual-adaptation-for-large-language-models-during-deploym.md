# CASCADE: Case-Based Continual Adaptation for Large Language Models During Deployment

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.06702v1
- Published: 2026-05-05
- Updated: 2026-05-05
- Authors: Siyuan Guo, Yali Du, Hechang Chen, Yi Chang, Jun Wang
- Tags: agent, context, episodic, long-term
- Categories: cs.AI, cs.CL, cs.LG
- URL: http://arxiv.org/abs/2605.06702v1

## One-Sentence Summary
Large language models (LLMs) have become a central foundation of modern artificial intelligence, yet their lifecycle remains constrained by a rigid separation between training...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) have become a central foundation of modern artificial intelligence, yet their lifecycle remains constrained by a rigid separation between training and deployment, after which learning...

进一步看，论文的核心做法或实验重点可以概括为：This limitation contrasts with natural intelligence, which continually adapts through interaction with its environment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, long-term
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.CL, cs.LG

## Abstract Snapshot
Large language models (LLMs) have become a central foundation of modern artificial intelligence, yet their lifecycle remains constrained by a rigid separation between training and deployment, after which learning effectively ceases. This limitation contrasts with natural intelligence, which continually adapts through interaction with its environment. In this paper, we formalise deployment-time learning (DTL) as the third stage in the LLM lifecycle that enables LLM agents to improve from experience during deployment without modifying model parameters. We present CASCADE (CASe-based Continual Adaptation during DEployment), a general and principled framework that equips LLM agents with an explicit, evolving episodic memory. CASCADE formulates experience reuse as a contextual bandit problem, enabling principled exploration-exploitation trade-offs and establishing no-regret guarantees over long-term interactions. This design allows agents to accumulate, select, and refine task-relevant cases, transforming past experience into actionable knowledge. Across 16 diverse tasks spanning medical diagnosis, legal analysis, code generation, web search, tool use, and embodied interaction, CASCADE improves macro-averaged success rate by 20.9% over zero-shot prompting while consistently outperforming gradient-based and memory-based baselines. By reframing deployment as an adaptive learning process, this work establishes a foundation for continually improving AI systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
