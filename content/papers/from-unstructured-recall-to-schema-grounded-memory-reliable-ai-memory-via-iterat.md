# From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.27906v1
- Published: 2026-04-30
- Updated: 2026-04-30
- Authors: Alex Petrov, Alexander Gusak, Denis Mukha, Dima Korolev
- Tags: agent, benchmark, context, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2604.27906v1

## One-Sentence Summary
Persistent AI memory is often reduced to a retrieval problem: store prior interactions as text, embed them, and ask the model to recover relevant context later.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent AI memory is often reduced to a retrieval problem: store prior interactions as text, embed them, and ask the model to recover relevant context later.

进一步看，论文的核心做法或实验重点可以概括为：This design is useful for thematic recall, but it is mismatched to the kinds of memory that agents need in production: exact facts, current state, updates and deletions, aggregation, relations, negative queries, and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Persistent AI memory is often reduced to a retrieval problem: store prior interactions as text, embed them, and ask the model to recover relevant context later. This design is useful for thematic recall, but it is mismatched to the kinds of memory that agents need in production: exact facts, current state, updates and deletions, aggregation, relations, negative queries, and explicit unknowns. These operations require memory to behave less like search and more like a system of record. This paper argues that reliable external AI memory must be schema-grounded. Schemas define what must be remembered, what may be ignored, and which values must never be inferred. We present an iterative, schema-aware write path that decomposes memory ingestion into object detection, field detection, and field-value extraction, with validation gates, local retries, and stateful prompt control. The result shifts interpretation from the read path to the write path: reads become constrained queries over verified records rather than repeated inference over retrieved prose. We evaluate this design on structured extraction and end-to-end memory benchmarks. On the extraction benchmark, the judge-in-the-loop configuration reaches 90.42% object-level accuracy and 62.67% output accuracy, above all tested frontier structured-output baselines. On our end-to-end memory benchmark, xmemory reaches 97.10% F1, compared with 80.16%-87.24% across the third-party baselines. On the application-level task, xmemory reaches 95.2% accuracy, outperforming specialised memory systems, code-generated Markdown harnesses, and customer-facing frontier-model application harnesses. The results show that, for memory workloads requiring stable facts and stateful computation, architecture matters more than retrieval scale or model strength alone.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
