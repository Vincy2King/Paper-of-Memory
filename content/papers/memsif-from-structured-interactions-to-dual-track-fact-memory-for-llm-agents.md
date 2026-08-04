# MemSIF: From Structured Interactions to Dual-Track Fact Memory for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01742v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: YuFei Luo, Xiucheng Xu, Zhen Yang
- Tags: agent, long-term
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2608.01742v1

## One-Sentence Summary
Long-term memory is critical for LLM agents operating over long-horizon interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is critical for LLM agents operating over long-horizon interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, several persistent limitations of existing memory systems can be traced to two recurring misalignment patterns in long-term interaction settings: Temporal-Structural Misalignment (TSM) and Delayed Utility...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Long-term memory is critical for LLM agents operating over long-horizon interactions. However, several persistent limitations of existing memory systems can be traced to two recurring misalignment patterns in long-term interaction settings: Temporal-Structural Misalignment (TSM) and Delayed Utility Manifestation (DUM). TSM arises when temporal proximity does not reliably align with topical or event-level relatedness, whereas DUM arises when write-time salience does not reliably predict future query utility. To mitigate these misalignment patterns, we propose MemSIF (Memory with Structured Interactions and Facts), a structured interaction-to-fact memory framework. Structured Interaction Memory organizes raw interactions into Topical Segments that preserve local topical coherence and Event Trajectories that maintain cross-time event continuity. Dual-Track Fact Memory uses two complementary tracks: CoreFact memory consolidates stable, schema-guided information at write time, whereas ActiveFact memory forms facts on demand and promotes those supported by multiple historical sources and recurring query demand for reuse. Experiments on LoCoMo and LongMemEval-S across five backbone LLMs show that MemSIF achieves the highest Total ACC in all settings, outperforming the strongest baseline by 2.29%-8.79% on LoCoMo and 2.87%-6.15% on LongMemEval-S. These results support the effectiveness of combining Structured Interaction Memory with Dual-Track Fact Memory to mitigate TSM and DUM. Code is available at https://github.com/luoyufeihaha/MemSIF.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
