# Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.02560v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Anusha Madan Gopal, Aras Pirbadian, Kristofor D. Carlson, M Anthony Lewis, Jonathan Tapson
- Tags: context, episodic, long-term, retrieval
- Categories: cs.LG, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2608.02560v1

## One-Sentence Summary
Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, episodic, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token.

进一步看，论文的核心做法或实验重点可以概括为：State-Space Models (SSMs) avoid the second cost by construction; we eliminate the first, collapsing prefill from $O(L_{context})$ to $O(1)$ per query.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, episodic, long-term, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.LG, cs.AI, cs.IR

## Abstract Snapshot
Retrieval-augmented generation (RAG) imposes a prefill cost proportional to retrieved context length, and -- with Transformer backbones -- a KV-cache that grows with each generated token. State-Space Models (SSMs) avoid the second cost by construction; we eliminate the first, collapsing prefill from $O(L_{context})$ to $O(1)$ per query. We introduce PRECOG (Pre-Computed Context Injection), a retrieval mechanism that exploits a property unique to SSMs: the fixed-size, position-agnostic recurrent hidden state is a complete summary of everything the model has read. PRECOG pre-encodes document corpora offline as SSM hidden states and injects the best-matching state directly at query time, bypassing in-context re-ingestion entirely. The same state-injection mechanism enables SMC (Structured Memory Consolidation): a hierarchical persistent memory with cognitive-domain clustering, an adjustable fidelity-vs-storage dial, and $O(1)$ session initialization, which consolidates short-term episodic states into long-term semantic memory and fuses both with retrieved corpus states at query time. We demonstrate the system on TENNs-LLM, a 1.2B-parameter gated-SSM language model with a 192 KB hidden state. PRECOG matches in-context RAG answer quality, reducing prefill latency from $\sim$27 s to $<$6 ms on edge hardware -- a $\sim$4500$\times$ speedup that crosses the threshold from unusable to interactive. The mechanism is architecturally impossible for Transformer KV-caches, which are position-entangled and grow linearly with context length.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
