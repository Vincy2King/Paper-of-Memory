# Clocks all the way down: does sequence-processing AI need endogenous temporal structure?

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.04181v1
- Published: 2026-11-03
- Updated: 2026-11-03
- Authors: Meysam Hashemi, Alireza Valizadeh, Viktor Jirsa
- Tags: retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.04181v1

## One-Sentence Summary
Mainstream sequence-processing AI is temporally reactive: each update is driven by input and learned state transitions, rather than by an independently evolving internal...

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Mainstream sequence-processing AI is temporally reactive: each update is driven by input and learned state transitions, rather than by an independently evolving internal temporal reference.

进一步看，论文的核心做法或实验重点可以概括为：Biological brains, by contrast, continuously generate rhythmic activity that structures perception, memory, and cognition, and this rhythmicity reaches all the way to behavior.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Mainstream sequence-processing AI is temporally reactive: each update is driven by input and learned state transitions, rather than by an independently evolving internal temporal reference. Biological brains, by contrast, continuously generate rhythmic activity that structures perception, memory, and cognition, and this rhythmicity reaches all the way to behavior. We ask whether this difference is merely implementational or genuinely computational. Four lines of evidence suggest that endogenous temporal structure supports putative functions that input-driven architectures may not readily replicate: 1) phase-dependent routing of information, 2) delay-structured combinatorial representation, 3) cross-frequency multiplexing of items, and 4) oscillation-gated offline consolidation. A proof-of-concept delay-ablation test dissociates representational capacity from memory retrieval. In recurrent and spatial spiking networks with fixed synaptic weights and connectivity, shuffling delays preserves part of the capacity but substantially impairs the sequence retrieval. The relative contrast is more pronounced for spatial networks and longer propagations. Instantaneous transmission collapses capacity itself. We then outline a cross-frequency multiplexing scheme that combines item identity and serial order with alternative mechanisms for selective memory retrieval. Finally, we state one falsifiable hypothesis, conditions for matched-resource tests, and three research directions: the components already exist; the disciplined comparison does not.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
