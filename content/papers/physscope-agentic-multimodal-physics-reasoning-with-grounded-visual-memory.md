# PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.23010v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Haoyang Liu, Kecheng Liang, Xinyu Li, Weixing Chen, Yang Liu
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.23010v1

## One-Sentence Summary
Vision-language models (VLMs) can correctly interpret physics diagrams yet apply constraints outside the states or conditions in which they hold, causing premise errors to...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Vision-language models (VLMs) can correctly interpret physics diagrams yet apply constraints outside the states or conditions in which they hold, causing premise errors to propagate through subsequent calculations.

进一步看，论文的核心做法或实验重点可以概括为：We introduce PhysScope, an inference-time visual harness that supports self-correction of these scope mismatches without updating model weights.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Vision-language models (VLMs) can correctly interpret physics diagrams yet apply constraints outside the states or conditions in which they hold, causing premise errors to propagate through subsequent calculations. We introduce PhysScope, an inference-time visual harness that supports self-correction of these scope mismatches without updating model weights. PhysScope enables the model to link physical scopes directly to its visual observations and explicitly constructs derived views to support reasoning. The harness imposes explicit constraints on state distinctions, conditions, and physical scopes during model reasoning, and checks agent-proposed revisions against sources and scopes. Accepted revisions invalidate registered dependents, thereby maintaining scope-aware working memory. On PhysAlign, PhysScope achieves higher solving scores than direct solving across all six evaluated VLMs. With Gemini-3.8-flash, it outperforms Canvas-CoT by 9.34 percentage points and substantially improves solving accuracy on the out-of-distribution (OOD) PhysUniBench benchmark. Ablation studies support explicit scope management and dependency maintenance as design principles for multimodal physics reasoning agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
