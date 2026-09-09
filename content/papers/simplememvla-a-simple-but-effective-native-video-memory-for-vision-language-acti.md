# SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.05533v1
- Published: 2026-09-02
- Updated: 2026-09-02
- Authors: Cheng Yin, Wang Xu, Junpeng Yang, Sikyuen Tam, Hanyu Liu, Yuan Yao, Xiangrui Zeng, Junbo Cui, Yequan Wang, Zhouping Yin, Yankai Lin
- Tags: benchmark, compression, retrieval
- Categories: cs.CV, cs.LG, cs.RO
- URL: http://arxiv.org/abs/2609.05533v1

## One-Sentence Summary
Long-horizon manipulation is partially observable: the information needed to choose the next action may appear only in observations from minutes earlier.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, compression, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon manipulation is partially observable: the information needed to choose the next action may appear only in observations from minutes earlier.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory mechanisms: retrieval banks, learned compressors, recurrent states must decide what to keep from the past before knowing what a future decision will require.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, compression, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.CV, cs.LG, cs.RO

## Abstract Snapshot
Long-horizon manipulation is partially observable: the information needed to choose the next action may appear only in observations from minutes earlier. Existing memory mechanisms: retrieval banks, learned compressors, recurrent states must decide what to keep from the past before knowing what a future decision will require. This was motivated by the assumption that minute-scale history is too large to process directly, which modern VLM backbones no longer make true. In this work, we introduce SimpleMemVLA, a VLA without a dedicated memory module. It keeps the sampled history intact and passes it to the backbone in the timestamped video format the backbone was pretrained to process; the hidden states of a generated sub-task then form the only channel from history to a standard flow-matching action head. Since consecutive decisions share most of their history, prefilling the shared prefix during action execution keeps latency close to a single-frame VLA. SimpleMemVLA sets a new state of the art on four memory benchmarks without cost on general-purpose control. Holding the backbone and training setup fixed, it outperforms retrieval, compression and recurrent-state mechanisms by a wide margin, and causal interventions confirm that the policy genuinely reads its history. Code available at https://github.com/wadeKeith/SimpleMemVLA

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
