# Memory as Code: Declarative Retrieval over Codified Long-Term Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.27700v1
- Published: 2026-10-20
- Updated: 2026-10-20
- Authors: Aoting Zeng, Yuxin Du, Jianwei Wang, Yizhang He, Shan Jiang, Xuemin Lin, Kai Wang
- Tags: agent, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.27700v1

## One-Sentence Summary
In long-term memory systems, memories are constructed from interaction histories and retrieved in response to queries, enhancing the reasoning ability of LLM agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In long-term memory systems, memories are constructed from interaction histories and retrieved in response to queries, enhancing the reasoning ability of LLM agents.

进一步看，论文的核心做法或实验重点可以概括为：In complex scenarios, facts are scattered across sessions and their relationships evolve over time, making it difficult for existing memory systems to compose them to adapt to diverse queries.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
In long-term memory systems, memories are constructed from interaction histories and retrieved in response to queries, enhancing the reasoning ability of LLM agents. In complex scenarios, facts are scattered across sessions and their relationships evolve over time, making it difficult for existing memory systems to compose them to adapt to diverse queries. Motivated by the modularity and composability of code, we propose Memory as Code (MaC), a unified memory framework that jointly designs memory construction and retrieval through a shared code abstraction. MaC couples codified construction, which establishes executable memory abstractions, with declarative retrieval, which translates queries into structured retrieval programs. Specifically, codified construction builds a three-layer executable memory structure that progresses from an atomic function layer, through a relational layer, to a modular composition layer. Declarative retrieval recasts retrieval from relevance-based fact selection into declarative query processing over memory. Experiments on LoCoMo and LongMemEval show relative gains of up to 15.91% in overall LLM-judge accuracy over the strongest baseline in each setting, while substantially reducing token consumption, highlighting the effectiveness of memory as code for long-horizon memory tasks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
