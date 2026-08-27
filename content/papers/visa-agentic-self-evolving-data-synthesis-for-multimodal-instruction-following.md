# VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.26013v1
- Published: 2026-08-26
- Updated: 2026-08-26
- Authors: Min Zeng, Guanxin Tan, Libin Cen, Yawei Wen, Rui Hu, Liuyang Bian, Xiaolong Chen, Xiaoxin Chen
- Tags: agent, benchmark
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.26013v1

## One-Sentence Summary
Multimodal instruction-following models require training data that is accurate, diverse, verifiable, and challenging.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multimodal instruction-following models require training data that is accurate, diverse, verifiable, and challenging.

进一步看，论文的核心做法或实验重点可以概括为：Existing synthesis pipelines typically follow a one-pass generate-and-filter paradigm, discarding feedback from failed samples, verifier outcomes, and target-model errors.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Multimodal instruction-following models require training data that is accurate, diverse, verifiable, and challenging. Existing synthesis pipelines typically follow a one-pass generate-and-filter paradigm, discarding feedback from failed samples, verifier outcomes, and target-model errors. We present VISA (Visual Instruction Synthesis Agent), an agentic framework that reformulates multimodal instruction synthesis as a self-evolving loop. At each round, VISA analyzes an image to filter incompatible constraints and discover new verifiable ones, samples diversity- and difficulty-aware constraint sets from persistent memory, generates candidate instructions, and verifies the resulting samples with executable tools and structured large language model judges. Failed samples trigger diagnostic-guided recovery, while accepted samples are probed against the target model to estimate difficulty. The resulting verifier signals and target-model failure profiles are written back to memory, allowing subsequent rounds to adaptively expand the constraint space, reduce template repetition, and focus on unresolved model weaknesses. The same verifier contracts further provide reward signals for reinforcement learning without a separately trained reward model. Experiments on MM-IFEval show that VISA consistently improves multimodal instruction following over strong baselines, while preserving general multimodal capability across seven public benchmarks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
