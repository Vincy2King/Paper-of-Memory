# RPMem: Learning Long-Term Recurrent Parametric Memory Across Sessions for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.23466v2
- Published: 2026-09-20
- Updated: 2026-09-22
- Authors: Fanyu Zhao, Ruike Cao, Liang Dong, Fugen Yao, Jian Xu, Guanjun Jiang, Han Zhang, Yifei Zhao, Yinsheng Li
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.23466v2

## One-Sentence Summary
Long-running LLM agents require memory that persists and evolves across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running LLM agents require memory that persists and evolves across sessions.

进一步看，论文的核心做法或实验重点可以概括为：Text-based memory retrieves and reconstructs past interactions at every query, making long-horizon performance increasingly dependent on retrieval quality and contextual reasoning as histories grow.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-running LLM agents require memory that persists and evolves across sessions. Text-based memory retrieves and reconstructs past interactions at every query, making long-horizon performance increasingly dependent on retrieval quality and contextual reasoning as histories grow. Parametric memory encodes experience directly into model computation, but existing approaches provide limited support for cross-session memory evolution. Their coupling to a specific backbone further restricts memory reuse after model replacement. We introduce RPMem, a two-stage architecture that compiles each session into a model-independent latent memory through forward computation and selectively integrates it with retained memory via a task-trained recurrent gate. The consolidated memory is then mapped to backbone-specific low-rank adaptation (LoRA) parameters, allowing the encoding capability to transfer when the backbone is replaced. Evaluation across three long-term memory benchmarks and five diverse backbones demonstrates broad generalization with near-constant update cost and memory footprint. With Qwen3-8B on PERMA, RPMem reaches 85.52%, outperforming the strongest parametric and text-based baselines by 5.32 and 12.98 percentage points, respectively. Ablations validate the complementary roles of session compilation and cross-session consolidation, while dynamics analyses reveal that the gate acquires task-specific memory integration strategies. These results establish RPMem as a lifecycle-independent parametric memory framework that maintains evolving cross-session memory that remains reusable across backbone replacements. Our implementation is available at https://github.com/Quark-Medical/rpmem/tree/main.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
