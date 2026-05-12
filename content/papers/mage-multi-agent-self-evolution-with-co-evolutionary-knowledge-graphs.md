# MAGE: Multi-Agent Self-Evolution with Co-Evolutionary Knowledge Graphs

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.10064v1
- Published: 2026-05-11
- Updated: 2026-05-11
- Authors: Ruiyi Yang, Zechen Li, Hao Xue, Imran Razzak, Flora D. Salim
- Tags: agent, benchmark, episodic, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.10064v1

## One-Sentence Summary
Self-evolving language-model agents must decide what to learn next and how to preserve what they have learned across iterations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Self-evolving language-model agents must decide what to learn next and how to preserve what they have learned across iterations.

进一步看，论文的核心做法或实验重点可以概括为：Existing systems typically carry this cross-iteration knowledge as natural-language feedback, flat episodic memory, or implicit reinforcement signals, none of which cleanly supports a frozen weak backbone at inference...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Self-evolving language-model agents must decide what to learn next and how to preserve what they have learned across iterations. Existing systems typically carry this cross-iteration knowledge as natural-language feedback, flat episodic memory, or implicit reinforcement signals, none of which cleanly supports a frozen weak backbone at inference time. This paper introduces MAGE (Multi-Agent Graph-guided Evolution), a framework that externalizes self-knowledge into a four-subgraph co-evolutionary knowledge graph. Its experience subgraph stores both teacher-written failure corrections and the learner's own past correct reasoning traces, which are retrieved as task-conditioned guidance for a frozen execution model. During evolution, the graph, a task-level search bandit, and a skill-level routing bandit are updated from the same reward stream, while the learner's backbone remains unchanged. We further provide structural analysis showing how append-only memory growth, bounded curriculum coverage, and task-filtered retrieval together support stable improvement of the retrieval substrate for frozen-learner evolution. Across nine benchmarks spanning mathematical reasoning, multi-hop and open-domain question answering, spatio-temporal analysis, financial numerical reasoning, medical multiple-choice, an open-world survival game, and web navigation, MAGE achieves strong performance against prompt-based frozen-backbone baselines. Ablations show that self-harvested success traces and teacher-written corrections are complementary, with success memories contributing most on reasoning-template-heavy tasks and corrective memories supporting harder composition and interaction settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
