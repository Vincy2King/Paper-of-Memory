# VitaBench: Memory Lifecycles Beyond Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.14731v1
- Published: 2026-10-10
- Updated: 2026-10-10
- Authors: Muquan Yu, Dihan Hu
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2610.14731v1

## One-Sentence Summary
Long-term memory benchmarks for language agents primarily evaluate whether information from earlier interactions can be retrieved and used when relevant.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory benchmarks for language agents primarily evaluate whether information from earlier interactions can be retrieved and used when relevant.

进一步看，论文的核心做法或实验重点可以概括为：Persistent memory systems face an additional problem before future use is known: deciding whether a memory should remain exact, be compressed, consolidated, or deleted.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks, persistent memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Long-term memory benchmarks for language agents primarily evaluate whether information from earlier interactions can be retrieved and used when relevant. Persistent memory systems face an additional problem before future use is known: deciding whether a memory should remain exact, be compressed, consolidated, or deleted. Existing benchmarks capture long-range retrieval, temporal reasoning, evidence reuse, and incremental interaction, but do not directly evaluate these earlier representation decisions. We formalize memory lifecycle evaluation and introduce VitaBench, a benchmark that makes lifecycle decisions measurable through repeated memory reviews and full-horizon counterfactual evaluation. VitaBench contains a controlled Diagnostic tier that isolates future-use patterns and a Naturalistic tier that composes them into generated customer-service-style interaction streams. We characterize lifecycle decision structure with three diagnostics: lifecycle headroom, measuring the advantage of adaptive choices over the best fixed strategy; horizon reversal, measuring when short-horizon decisions change under delayed consequences; and optimal-action diversity, measuring whether different memory states favor different lifecycle operations. Across both tiers, VitaBench exhibits substantial lifecycle structure: lifecycle headroom is 1.364 in Diagnostic and 1.405 in Naturalistic, and 60.2% and 56.5% of states, respectively, change their preferred action between short and full horizons. A learned delayed lifecycle policy further improves over the best fixed strategy on VitaBench-Naturalistic, reaching 101.5 versus 83.4 joint utility. These results show that retrieving past information and deciding how it should persist are distinct evaluation problems, and that lifecycle management requires evaluation of the delayed consequences of representation decisions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
