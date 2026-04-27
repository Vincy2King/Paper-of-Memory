# Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.22085v1
- Published: 2026-04-23
- Updated: 2026-04-23
- Authors: Seyed Moein Abtahi, Rasa Rahnema, Hetkumar Patel, Neel Patel, Majid Fekri, Tara Khani
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2604.22085v1

## One-Sentence Summary
The transition from stateless language model inference to persistent, multi session autonomous agents has revealed memory to be a primary architectural bottleneck in the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The transition from stateless language model inference to persistent, multi session autonomous agents has revealed memory to be a primary architectural bottleneck in the deployment of production grade agentic systems.

进一步看，论文的核心做法或实验重点可以概括为：Existing methodologies largely depend on hybrid semantic graph architectures, which impose substantial computational overhead during both ingestion and retrieval.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
The transition from stateless language model inference to persistent, multi session autonomous agents has revealed memory to be a primary architectural bottleneck in the deployment of production grade agentic systems. Existing methodologies largely depend on hybrid semantic graph architectures, which impose substantial computational overhead during both ingestion and retrieval. These systems typically require large language model mediated entity extraction, explicit graph schema maintenance, and multi query retrieval pipelines. This paper introduces Memanto, a universal memory layer for agentic artificial intelligence that challenges the prevailing assumption that knowledge graph complexity is necessary to achieve high fidelity agent memory. Memanto integrates a typed semantic memory schema comprising thirteen predefined memory categories, an automated conflict resolution mechanism, and temporal versioning. These components are enabled by Moorcheh's Information Theoretic Search engine, a no indexing semantic database that provides deterministic retrieval within sub ninety millisecond latency while eliminating ingestion delay. Through systematic benchmarking on the LongMemEval and LoCoMo evaluation suites, Memanto achieves state of the art accuracy scores of 89.8 percent and 87.1 percent respectively. These results surpass all evaluated hybrid graph and vector based systems while requiring only a single retrieval query, incurring no ingestion cost, and maintaining substantially lower operational complexity. A five stage progressive ablation study is presented to quantify the contribution of each architectural component, followed by a discussion of the implications for scalable deployment of agentic memory systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
