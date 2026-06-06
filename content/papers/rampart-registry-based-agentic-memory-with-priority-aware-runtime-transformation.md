# RAMPART: Registry-based Agentic Memory with Priority-Aware Runtime Transformation

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04628v1
- Published: 2026-06-03
- Updated: 2026-06-03
- Authors: Nikodem Tomczak
- Tags: agent, context
- Categories: cs.CL, cs.MA
- URL: http://arxiv.org/abs/2606.04628v1

## One-Sentence Summary
RAMPART is a compile-time memory model and pure in-RAM block registry for LLM-based agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：RAMPART is a compile-time memory model and pure in-RAM block registry for LLM-based agents.

进一步看，论文的核心做法或实验重点可以概括为：Context assembly is a programmable runtime operation where content is compiled from a structured registry under explicit policy for ordering, inclusion, and eviction.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.MA

## Abstract Snapshot
RAMPART is a compile-time memory model and pure in-RAM block registry for LLM-based agents. Context assembly is a programmable runtime operation where content is compiled from a structured registry under explicit policy for ordering, inclusion, and eviction. Five composable primitives (promote, gate, write, evict, rollback) act on named addressable blocks before compilation at zero prompt-token cost. Provenance tags and non-evictable authorship flags implement a permissioned memory model with block-level ownership. Controlled probes with Qwen3-8B Q4 show that compile-time placement and the structural relationship between blocks and the task query affect task success, with the cliff falling at roughly the seventh block position when the task follows the registry and the twelfth when it precedes. Grouping the critical block with content-adjacent neighbours and promoting the group as a unit lifts task success by tens of percentage points at positions where single-block placement fails. Cross-model replication on Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3, and Qwen3-14B shows the content-priming effect appears at the same absolute positions across families, with magnitude varying with model strength. Block grouping raises Mistral's mean pass rate roughly fivefold at the hardest registry size, and a smaller model with the intervention can outperform a larger model without it in the mid-registry zone. Relevance gating reduces prompt cost by 67.8\% while recovering 83% of the promoted-condition success rate. Schema eviction produces 0% invocations against 100% with the schema present, a property policy-based approaches cannot guarantee by construction. Shared-registry coordination reduces inter-agent communication to a method call at zero coordination token cost.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
