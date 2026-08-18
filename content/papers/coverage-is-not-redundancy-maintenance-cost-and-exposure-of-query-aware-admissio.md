# Coverage Is Not Redundancy: Maintenance Cost and Exposure of Query-Aware Admission Indexes in Vector Databases Under Workload Drift

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.16043v1
- Published: 2026-08-17
- Updated: 2026-08-17
- Authors: Prashant Kumar Pathak
- Tags: retrieval
- Categories: cs.DB, cs.IR
- URL: http://arxiv.org/abs/2608.16043v1

## One-Sentence Summary
In a vector database serving production-scale retrieval, a single inserted document can be retrieved for an anomalously large share of the query workload -- a retrieval hub --...

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In a vector database serving production-scale retrieval, a single inserted document can be retrieved for an anomalously large share of the query workload -- a retrieval hub -- and dominate the evidence returned for an...

进一步看，论文的核心做法或实验重点可以概括为：An emerging defense guards against this at ingest with an admission check: it maintains a set of sentinel queries and admits a document only if its reverse-kNN count against them stays below a threshold tau.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory compression
- 来源分类信息：cs.DB, cs.IR

## Abstract Snapshot
In a vector database serving production-scale retrieval, a single inserted document can be retrieved for an anomalously large share of the query workload -- a retrieval hub -- and dominate the evidence returned for an entire topic. An emerging defense guards against this at ingest with an admission check: it maintains a set of sentinel queries and admits a document only if its reverse-kNN count against them stays below a threshold tau. Under workload drift this sentinel set is a query-aware auxiliary index that must be maintained online, and we study the cost that maintenance imposes on the ingest path. We identify a structural limit -- coverage is not redundancy: a monitor stops promoting sentinels once a region is covered, but the predicate rejects a hub only once tau sentinels witness it, so exposure has an observation-limited floor that no reduction in update or enforcement latency can close. On real HNSW, IVF-Flat, and IVF-PQ indexes over an 8.8M-vector MS MARCO corpus this floor is only a best case: as index recall falls, exposure and churn rise above it, and below recall ~0.5 the gate stops containing altogether -- worst on the memory-compressed IVF-PQ used at billion scale -- while a recall-aware witness probe restores containment at a fixed O(|S|d) admission cost, under 0.1% of the ANN insert. We validate the law under real (COVID-19) workload drift, implement the gate in PostgreSQL/pgvector at a 0.33% ingest tax, and turn the bound into a provisioning rule that sizes the sentinel budget per emerging region. A count test contains the hub where retrieval-time score normalizers (NNN, QB-Norm) do not, and a pre-registered causal suite isolates the missing-coverage mechanism from retrieval fragmentation across two embedding families (BGE-1024, E5-768).

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
