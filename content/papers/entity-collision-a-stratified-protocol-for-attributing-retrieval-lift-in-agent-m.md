# Entity-Collision: A Stratified Protocol for Attributing Retrieval Lift in Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.29630v1
- Published: 2026-05-28
- Updated: 2026-05-28
- Authors: Youwang Deng
- Tags: agent, benchmark, retrieval
- Categories: cs.CL, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2605.29630v1

## One-Sentence Summary
End-to-end agent-memory benchmarks report a single hit@k per retriever, confounding lexical leakage (uncontrolled query/gold/distractor entity overlap) with tag-mixing...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：End-to-end agent-memory benchmarks report a single hit@k per retriever, confounding lexical leakage (uncontrolled query/gold/distractor entity overlap) with tag-mixing (preferences, services, tools averaged together).

进一步看，论文的核心做法或实验重点可以概括为：We propose entity-collision, a system-agnostic protocol that pins the BM25 floor by construction -- every distractor shares the answer's entity tokens -- and stratifies queries by discriminator tag, so any lift over...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI, cs.IR

## Abstract Snapshot
End-to-end agent-memory benchmarks report a single hit@k per retriever, confounding lexical leakage (uncontrolled query/gold/distractor entity overlap) with tag-mixing (preferences, services, tools averaged together). We propose entity-collision, a system-agnostic protocol that pins the BM25 floor by construction -- every distractor shares the answer's entity tokens -- and stratifies queries by discriminator tag, so any lift over BM25 is attributable to the embedder. Applied to an open-source agent-memory testbed across 5 tags x 3 embedders x 5 collision degrees with paired-bootstrap 95% CIs, the protocol reveals a two-axis pattern: a 256-d hash trigram helps only on closed-vocabulary lexical tags at deep collision; MiniLM-384 dominates both axes; and a 2.7x-parameter BGE-large does not uniformly improve on MiniLM -- it wins on intent-style queries but loses on lexical ones. Encoder capacity alone is not the binding constraint. The synthetic intent-tag null replicates on LongMemEval (n=500) as a single-session-preference recall cliff. Adaptive vector-weight routing on LoCoMo is a measured null: 11.7pp of oracle headroom exists, but no signal we tested recovers it. All 26 result tables and 37 reproduce scripts are version-controlled and verified by a public registry; the protocol is exercised on a deterministically governed memory testbed (event-sourced decision log, DAG-state-machine schema lifecycle) so every reported CI is reproducible byte-for-byte from the ingest stream.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
