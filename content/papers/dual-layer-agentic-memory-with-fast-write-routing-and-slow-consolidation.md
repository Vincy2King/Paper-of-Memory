# Dual-Layer Agentic Memory with Fast Write Routing and Slow Consolidation

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.22215v1
- Published: 2026-08-23
- Updated: 2026-08-23
- Authors: Wenzhi Li, Dong Nie, Rui Lan, Tongtong Lyu, Peiyao Wang, Lingzi Hong, Weihang Pan, Boyuan Pan, Yao Hu
- Tags: agent, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.22215v1

## One-Sentence Summary
Large language model (LLM) agents operate in dynamic environments where knowledge continuously evolves.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents operate in dynamic environments where knowledge continuously evolves.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems typically treat external memory as a monotonically growing repository, inevitably leading to retrieval degradation and increasing computational costs over time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language model (LLM) agents operate in dynamic environments where knowledge continuously evolves. Existing memory systems typically treat external memory as a monotonically growing repository, inevitably leading to retrieval degradation and increasing computational costs over time. We argue that the core challenge is not retrieval alone, but managing the knowledge lifecycle: deciding what to externalize, update, or ultimately internalize. Inspired by Complementary Learning Systems (CLS) theory in neuroscience, we propose Dual-Layer Agentic Memory, a framework that shifts memory management to the write phase through cost-aware epistemic routing and periodic parametric consolidation. Incoming information is categorized as non-write, write-new, or write-update, and routed through a small-to-large model cascade that minimizes routing overhead while filtering redundant memories. A subsequent write-back phase selectively consolidates high-value external memories into model parameters via supervised fine-tuning. Experiments demonstrate the dual efficiency of our approach: a 1.7B/8B cascade prunes up to 68% of redundant external memory while escalating fewer than 50% of inputs, yet retains over 98% of the downstream QA Exact Match (EM) achieved by an exhaustive retention baseline. We further show that periodic consolidation successfully internalizes external knowledge, allowing the router to adaptively suppress redundant writes as the model's epistemic boundaries evolve. Overall, our framework presents a unified paradigm for agent memory: selective externalization followed by selective internalization. Code and dataset will be released upon acceptance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
