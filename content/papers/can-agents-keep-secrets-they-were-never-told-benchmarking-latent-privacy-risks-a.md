# Can Agents Keep Secrets They Were Never Told? Benchmarking Latent Privacy Risks Across Sessions with MemJoin

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.24359v1
- Published: 2026-10-17
- Updated: 2026-10-17
- Authors: Qishun Yang, Shu Yang, Difei Xu, Di Wang, Meng Ding
- Tags: agent, benchmark, context, long-term
- Categories: cs.CR, cs.LG
- URL: http://arxiv.org/abs/2610.24359v1

## One-Sentence Summary
To support sustained interactions and personalized assistance, agents use long-term memory to retain and combine user information across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：To support sustained interactions and personalized assistance, agents use long-term memory to retain and combine user information across sessions.

进一步看，论文的核心做法或实验重点可以概括为：Reusing such memories can lead an agent to state a sensitive relation while completing an ordinary task that does not require it.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CR, cs.LG

## Abstract Snapshot
To support sustained interactions and personalized assistance, agents use long-term memory to retain and combine user information across sessions. Reusing such memories can lead an agent to state a sensitive relation while completing an ordinary task that does not require it. The relation to protect and the combination of clues that reveal it may remain hidden at memory write time, when later records and tasks are still unknown. In this paper, we introduce MemJoin, a privacy benchmark of 288 synthetic analysis cases in which the complete history entails a sensitive relation, but every individual session is insufficient. We evaluate six memory systems with the same answer-generating model, alongside full-history and no-history controls. Each system writes and updates memories in session order and later retrieves context for an ordinary task, while target annotations remain with the evaluator. We separately check which target attribute values appear in stored records and retrieved context, and whether the final answer states the complete, person-linked relation. In a separate paired test on a prespecified subset, removing shared identifiers and other connecting clues can change complete-relation output while all checked target attribute values remain visible. These findings show why checking attribute visibility alone is insufficient to evaluate what records from different sessions reveal together.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
