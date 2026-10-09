# Gated Memory: Admission-Controlled Memory Formation for Conversational AI

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.11270v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Preeti Saraswat, Divya Neelagiri, Ajay Manoj
- Tags: benchmark, context, conversation, long-term, retrieval
- Categories: cs.CL, cs.AI, cs.IR, cs.LG
- URL: http://arxiv.org/abs/2610.11270v1

## One-Sentence Summary
Personalized conversational AI relies on long-term memory systems that extract facts from user utterances and store them in persistent vector stores.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personalized conversational AI relies on long-term memory systems that extract facts from user utterances and store them in persistent vector stores.

进一步看，论文的核心做法或实验重点可以概括为：Despite progress in retrieval, deduplication, and lifecycle management, the formation stage, the moment a fact is first written to storage has received almost no principled attention.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, conversation, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI, cs.IR, cs.LG

## Abstract Snapshot
Personalized conversational AI relies on long-term memory systems that extract facts from user utterances and store them in persistent vector stores. Despite progress in retrieval, deduplication, and lifecycle management, the formation stage, the moment a fact is first written to storage has received almost no principled attention. We identify this as the binding constraint on memory quality in production systems. Critical contextual signals, such as the distinction between a permanent user attribute and a transient situation, exist only in the original utterance and are irreversibly lost the moment extraction produces a subject-relation-object triple. No downstream process can recover them. We propose Gated Memory, a lightweight, modular formation framework that interposes two decision checkpoints between conversation and storage: an admission gate that evaluates every candidate fact against the full utterance context before extraction runs, and a conditional enrichment stage that grounds admitted facts through an entity scope taxonomy with privacy constraints. The gate evaluates only the current exchange while using prior turns as read-only reference context, and produces a structured formation record. Admitted content is decomposed into atomic facts, each categorized, tagged with provenance (directly stated versus inferred), scoped to its condition of applicability, and grounded in resolved time and place, subject to a constraint that no entity absent from the context may be asserted. On the LoCoMo-10 benchmark with atypical emotional density in utterance data, Gated Memory achieves an overall +2.6% relative improvement in LLM-judge accuracy over a strong baseline with identical retrieval and generation, establishing formation quality as a measurable constraint on memory performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
