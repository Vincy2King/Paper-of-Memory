# D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.16417v1
- Published: 2026-08-17
- Updated: 2026-08-17
- Authors: Hao Zhang, Longrong Yang, Lunhao Duan, Ziyang Wang, Qing-Guo Chen, Shanshan Zhao
- Tags: agent, benchmark, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.16417v1

## One-Sentence Summary
Multi-modal retrieval-augmented generation (RAG) is a key technique for visually rich long document understanding.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-modal retrieval-augmented generation (RAG) is a key technique for visually rich long document understanding.

进一步看，论文的核心做法或实验重点可以概括为：Existing multi-modal RAG methods are progressively advancing toward multi-agent systems: they first retrieve relevant pages based on a query, and then iteratively understand information within those pages.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Multi-modal retrieval-augmented generation (RAG) is a key technique for visually rich long document understanding. Existing multi-modal RAG methods are progressively advancing toward multi-agent systems: they first retrieve relevant pages based on a query, and then iteratively understand information within those pages. However, these methods typically rely on fixed workflows and lack the ability to dynamically scale computation at test time, often leading to insufficient evidence. To address this, we propose D2-ScaleAgent, an agentic framework that introduces a dual-dimensional scaling paradigm for retrieval and reasoning. The core of D2-ScaleAgent is a Verifier agent-driven dynamic routing loop based on the intrinsic difficulty of the query, centered around a continuously updated evidence bank that serves as the agent's dynamic working memory: when retrieval needs to be expanded, the agent routes outward (retrieval scaling), decomposing the query into attributes and performing parallel page retrieval, followed by adaptive pruning to ensure comprehensive evidence coverage. When fine-grained reasoning is required, the agent routes inward (reasoning scaling), dynamically selecting sub-agents with varying granularity and count to extract evidence from pages. Finally, D2-ScaleAgent achieves logical closure over the evidence chain. Extensive experiments demonstrate that D2-ScaleAgent is effective on long and visually rich document benchmarks like MMLongBench-Doc, LongDocURL, etc.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
