# H2G-Mem: Heterogeneous HyperGraphs for Fine-Grained Long-term Conversational Agent Memory

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:h8EITsueME
- Published: 2026-06-02
- Updated: 2026-06-02
- Authors: Unknown
- Tags: agent, benchmark, context, conversation, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=h8EITsueME

## One-Sentence Summary
Large language models (LLMs) remain limited in long-horizon conversational settings due to their inability to reliably preserve and retrieve historical information.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large language models (LLMs) remain limited in long-horizon conversational settings due to their inability to reliably preserve and retrieve historical information.

进一步看，论文的核心做法或实验重点可以概括为：Existing agentic memory systems address this through a two-stage paradigm: structural memory database construction and memory database retrieval.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory, memory retrieval
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Large language models (LLMs) remain limited in long-horizon conversational settings due to their inability to reliably preserve and retrieve historical information. Existing agentic memory systems address this through a two-stage paradigm: structural memory database construction and memory database retrieval. However, most existing methods suffer from two key limitations: (1) they rely on oversimplified data structures, such as plain text chunks in a vector database, failing to capture the relational complexity of multi-session conversations; (2) they adopt coarse-grained information units, such as conversation periods or chunks of conversation indexed solely by semantic embeddings, which hinders fine-grained action matching and complex reasoning during retrieval. To address these issues, we propose a hierarchical heterogeneous hypergraph memory framework for long-term conversational agents. For memory construction, we design a hypergraph-based structure that organizes person- and activity-centric information into a unified hierarchy, where events act as hyperedge-like nodes connecting globally sharable entity anchors while maintaining activities and semantic facts as event-level attributes. For memory retrieval, we introduce a multi-granularity search strategy combining entity-based hypernode-cooccurrence matching for fine-grained event alignment with event-based semantic matching for coarse-grained contextual relevance. Experiments on the widely used benchmarks LoCoMo and LongMemEval demonstrate that our method achieves around 8\% performance improvements over state-of-the-art baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
