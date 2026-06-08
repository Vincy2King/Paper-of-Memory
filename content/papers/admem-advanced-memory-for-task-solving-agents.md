# AdMem: Advanced Memory for Task-solving Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.06787v1
- Published: 2026-06-05
- Updated: 2026-06-05
- Authors: Runzhe Wang, Huilin Lu, Shengjie Liu, Li Dong, Jason Zhu
- Tags: agent, episodic, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.06787v1

## One-Sentence Summary
Large Language Models (LLMs) show promise as tool-using agents but remain limited in long-horizon tasks that require remembering, organizing, and reusing knowledge.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) show promise as tool-using agents but remain limited in long-horizon tasks that require remembering, organizing, and reusing knowledge.

进一步看，论文的核心做法或实验重点可以概括为：Prior memory approaches aim to resolve the situation, but mainly focus on storing factual information.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large Language Models (LLMs) show promise as tool-using agents but remain limited in long-horizon tasks that require remembering, organizing, and reusing knowledge. Prior memory approaches aim to resolve the situation, but mainly focus on storing factual information. Recent work on procedural memory improves task reuse, yet often reduces to replaying past successes without addressing failure cases or online scalability. We introduce a unified and automatic memory framework that integrates semantic, episodic, and procedural memory in a bi-level design combining short-term and long-term stores. A multi-agent architecture with actor, memory, and critic agents enables automatic memory generation, reward annotation, and adaptive retrieval. Long-term memory is managed through reward-based evaluation, merging, and pruning, ensuring scalability and continual improvement. Experiments across various environments show that our approach improves robustness and success on long multi-turn tasks compared to existing baselines. This work highlights the importance of comprehensive, adaptive memory for advancing LLM-based agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
