# Memory Echo in Single-Agent Long-Term Memory: Lifecycle Evaluation and Provenance-Guided Mitigation

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.17763v1
- Published: 2026-10-13
- Updated: 2026-10-13
- Authors: Yufeng Li, Sheng Yao, Peng Zeng, Dezhang Kong, Shi Lin, Changting Lin, Xun Wang, Meng Han
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.17763v1

## One-Sentence Summary
Long-term memory supports agents across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory supports agents across sessions.

进一步看，论文的核心做法或实验重点可以概括为：Repeated retrieval and write-back can let one historical claim occupy multiple retrieval positions and influence current answers without independent evidence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory supports agents across sessions. Repeated retrieval and write-back can let one historical claim occupy multiple retrieval positions and influence current answers without independent evidence. Existing work examines retrieval, updating, and question answering, leaving same-source record accumulation and post-correction persistence underexplored. Motivated by research in social cognition and memory psychology on repeated exposure, retrieval, and revision, we define \emph{Memory Echo} as the excess retrieval exposure gained by historical information from the same source without additional independent evidence, and introduce MEchoBench to evaluate its emergence, correction resistance, persistence, and effect on answers. To address this phenomenon, we introduce the Family--Provenance--Authority framework (FPA). Specifically, FPA selects one representative per source family, conditions the eligibility of old records for the answer context on verified corrections, and constrains final answers with authoritative evidence. In paired replay on 190 fixed questions across four memory frameworks, FPA raises accuracy from 0.825 to 0.920 with DeepSeek V4 Flash and from 0.782 to 0.916 with Kimi K2.6; mean Decision Contamination Effect falls from 0.106 to 0.030 and from 0.109 to 0.038, respectively. These results show that agent memory can preserve traceable history without allowing repeated historical information to govern current decisions. The code is available at https://github.com/OrcasSam/memory-echo-benchmark.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
