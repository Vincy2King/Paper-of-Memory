# DuoMem: Towards Capable On-Device Memory Agents via Dual-Space Distillation

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.29961v1
- Published: 2026-06-29
- Updated: 2026-06-29
- Authors: Peyman Hosseini, Ondrej Bohdal, Ahmed Alajrami, Andrea Maracani, Ignacio Castro, Matthew Purver, Mete Ozay, Savas Ozkan, Taha Ceritli
- Tags: agent, benchmark, context
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2606.29961v1

## One-Sentence Summary
Large Language Model (LLM)-based agents can solve complex procedural tasks by interacting with environments over multiple turns, but this ability typically depends on large...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Model (LLM)-based agents can solve complex procedural tasks by interacting with environments over multiple turns, but this ability typically depends on large models, long contexts, and repeated...

进一步看，论文的核心做法或实验重点可以概括为：This makes advanced memory-augmented agents difficult to deploy on resource-constrained devices.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Large Language Model (LLM)-based agents can solve complex procedural tasks by interacting with environments over multiple turns, but this ability typically depends on large models, long contexts, and repeated inference calls. This makes advanced memory-augmented agents difficult to deploy on resource-constrained devices. We introduce DuoMem, a dual-space distillation framework that transfers procedural problem-solving ability from a large teacher model to compact student models. DuoMem distils in two complementary spaces: (1)context-space distillation, which replaces student-generated memories with higher-quality teacher-generated procedural memories prepended to the student's input, and (2)parameter-space distillation, which fine-tunes lightweight LoRA adapters on successful teacher trajectories. Evaluated on ALFWorld, a challenging embodied decision-making benchmark, DuoMem boosts a 4B-parameter model from 4.3% to 77.9% task success rate, closing most of the gap to a 72B teacher model (87.1%), while adding fewer than 10M trainable parameters and only a few megabytes of pre-computed teacher memories. Moreover, the DuoMem-enhanced 4B model completes tasks over 3x faster than the 72B teacher in wall-clock time, making it viable for real-time edge deployment, which would be challenging for the teacher.Extensive ablations across eight models spanning 2B-72B parameters reveal that both distillation axes contribute complementary

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
