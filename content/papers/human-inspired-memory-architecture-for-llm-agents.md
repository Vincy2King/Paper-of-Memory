# Human-Inspired Memory Architecture for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.08538v1
- Published: 2026-05-08
- Updated: 2026-05-08
- Authors: Doga Kerestecioglu, Alexei Robsky, Clemens Vasters, Anshul Sharma, Yitzhak Kesselman
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI, cs.CL, cs.IR, cs.LG
- URL: http://arxiv.org/abs/2605.08538v1

## One-Sentence Summary
Current LLM agents lack principled mechanisms for managing persistent memory across long interaction horizons.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Current LLM agents lack principled mechanisms for managing persistent memory across long interaction horizons.

进一步看，论文的核心做法或实验重点可以概括为：We present a biologically-grounded memory architecture comprising six cognitive mechanisms: (1) sleep-phase consolidation, (2) interference-based forgetting, (3) engram maturation, (4) reconsolidation upon retrieval,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.CL, cs.IR, cs.LG

## Abstract Snapshot
Current LLM agents lack principled mechanisms for managing persistent memory across long interaction horizons. We present a biologically-grounded memory architecture comprising six cognitive mechanisms: (1) sleep-phase consolidation, (2) interference-based forgetting, (3) engram maturation, (4) reconsolidation upon retrieval, (5) entity knowledge graphs, and (6) hybrid multi-cue retrieval. Each mechanism addresses a specific failure mode of naive memory accumulation. We introduce a synthetic calibration methodology that derives all pipeline thresholds without benchmark data exposure, eliminating a common source of evaluation leakage. We evaluate on two benchmarks. First, a VSCode issue-tracking dataset (13K issues, 120K events) where deduplication-based consolidation achieves 97.2% retention precision with 58% store reduction (+21.8 pp over baseline). Second, the LongMemEval personal-chat benchmark where we conduct the first streaming M-tier evaluation (475 sessions, ~540K unique turns). At a 200K-token context budget, our pipeline matches raw retrieval accuracy (70.1% vs. 71.2%, overlapping 95% CI) while exposing a tunable accuracy/store-size operating curve. At S-tier scale (50 sessions), dedup-based consolidation yields a +13.3 pp improvement in preference recall.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
