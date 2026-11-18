# RegimeCouncil: Paired-Evidence Routing For Memory Conflict Governance In LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.22113v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Qingcan Kang, Mingyang Liu, Shixiong Kai, Tao Zhong, Mingxuan Yuan
- Tags: agent, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.22113v1

## One-Sentence Summary
Language agents rely on long-term memory to personalize responses across extended interactions, yet stored facts quietly go stale as the world changes, and an agent often learns...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language agents rely on long-term memory to personalize responses across extended interactions, yet stored facts quietly go stale as the world changes, and an agent often learns that using memory hurt only through...

进一步看，论文的核心做法或实验重点可以概括为：Before the memory store is updated, how far should that negative feedback propagate: should it suppress memory use only on future queries for that same fact (a local policy), or also across other stored facts (a...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Language agents rely on long-term memory to personalize responses across extended interactions, yet stored facts quietly go stale as the world changes, and an agent often learns that using memory hurt only through delayed feedback after acting on an outdated record. Before the memory store is updated, how far should that negative feedback propagate: should it suppress memory use only on future queries for that same fact (a local policy), or also across other stored facts (a global policy)? Existing memory systems implicitly fix one of these two sharing scopes at design time. We formulate this online scope choice under hidden validity and delayed feedback as memory conflict governance, and prove that neither fixed policy is sufficient on its own. We then propose RegimeCouncil, a lightweight paired-evidence router that retains both scopes as advisors and arbitrates between them online without retraining the LLM. Using revealed comparisons between answering with memory and answering without memory (the no-memory anchor), a Local Advisor tracks the latest outcome on the queried fact alone, while a Global Advisor pools recent outcomes across all stored facts. A Meta Governor follows the Local Advisor by default to avoid cross-fact interference and switches to the Global Advisor only when global pooling accumulates a strictly positive recent utility margin, guaranteeing finite-time switching under delayed feedback. Across LongMemEval update streams and real-world historical drift on TempLAMA and TAQA with Qwen3-30B-A3B and GPT-4o, RegimeCouncil outperforms the better fixed-scope policy by 5.2-7.3 points on primary disagreement episodes and across all 30 held-out settings, while ablations show that removing any of its three modules reduces accuracy by 2-7 points.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
