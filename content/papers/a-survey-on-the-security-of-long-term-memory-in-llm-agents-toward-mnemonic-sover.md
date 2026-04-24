# A Survey on the Security of Long-Term Memory in LLM Agents: Toward Mnemonic Sovereignty

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.16548v1
- Published: 2026-04-17
- Updated: 2026-04-17
- Authors: Zehao Lin, Chunyu Li, Kai Chen
- Tags: agent, long-term, retrieval
- Categories: cs.CR, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2604.16548v1

## One-Sentence Summary
Research on large language model (LLM) security is shifting from "will the model leak training data" to a more consequential question: can an agent with persistent, long-term...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Research on large language model (LLM) security is shifting from "will the model leak training data" to a more consequential question: can an agent with persistent, long-term memory be continuously shaped, cross-...

进一步看，论文的核心做法或实验重点可以概括为：Recent surveys cover memory architectures and agent mechanisms, but fewer center the epistemic and governance properties of persistent, writable memory as the reason memory is an independent security problem.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.CR, cs.AI, cs.CL

## Abstract Snapshot
Research on large language model (LLM) security is shifting from "will the model leak training data" to a more consequential question: can an agent with persistent, long-term memory be continuously shaped, cross-session poisoned, accessed without authorization, and propagated across shared organizational state? Recent surveys cover memory architectures and agent mechanisms, but fewer center the epistemic and governance properties of persistent, writable memory as the reason memory is an independent security problem. This survey addresses that gap. Drawing on cognitive neuroscience and the philosophy of memory, we characterize agent memory as malleable, rewritable, and socially propagating, and develop a memory-lifecycle framework organized around six phases -- Write, Store, Retrieve, Execute, Share, Forget/Rollback -- cross-tabulated against four security objectives: integrity, confidentiality, availability, governance. We organize the literature on memory poisoning, extraction, retrieval corruption, control-flow hijacking, cross-agent propagation, rollback, and governance, and situate representative architectures as determinants of which phases are explicitly governable. Three findings stand out: the literature concentrates on write- and retrieve-time integrity attacks, while confidentiality, availability, store/forget, and benign-persistence failures remain sparsely studied; no published architecture covers all nine governance primitives we identify; and using LLMs themselves for memory security remains sparse yet essential. We unify these under mnemonic sovereignty -- verifiable, recoverable governance over what may be written, who may read, when updates are authorized, and which states may be forgotten -- arguing future secure agents will be differentiated not only by recall capacity, but by memory governance quality.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
