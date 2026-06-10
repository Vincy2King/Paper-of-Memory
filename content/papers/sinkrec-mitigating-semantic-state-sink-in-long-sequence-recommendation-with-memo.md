# SinkRec: Mitigating Semantic State Sink in Long Sequence Recommendation with Memory-Conditioned Gated Delta Networks

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.09888v1
- Published: 2026-06-03
- Updated: 2026-06-03
- Authors: Zhuang Zhuang, Zhipeng Wei, Ji Dai, Jie Chen, Fei Pan, Peng Jiang, Kun Gai
- Tags: memory
- Categories: cs.LG
- URL: http://arxiv.org/abs/2606.09888v1

## One-Sentence Summary
Linear attention provides an efficient backbone for long-sequence recommendation by avoiding the quadratic cost of standard Transformers, but its compressed recurrent state can...

## Introduction
这篇论文被纳入仓库，是因为它和 `memory research` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Linear attention provides an efficient backbone for long-sequence recommendation by avoiding the quadratic cost of standard Transformers, but its compressed recurrent state can be dominated by repetitive behavior...

进一步看，论文的核心做法或实验重点可以概括为：We identify this phenomenon as semantic state sink, where recurring semantics over-occupy the recurrent state and bias subsequent readouts.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.LG

## Abstract Snapshot
Linear attention provides an efficient backbone for long-sequence recommendation by avoiding the quadratic cost of standard Transformers, but its compressed recurrent state can be dominated by repetitive behavior patterns. We identify this phenomenon as semantic state sink, where recurring semantics over-occupy the recurrent state and bias subsequent readouts. To mitigate semantic state sink, we propose SinkRec, a hybrid memory-transition looped architecture that decouples collaborative behavioral pattern storage from dynamic transition modeling. SinkRec externalizes recurring local patterns into a learnable conditional memory through residual vector quantization, reinjects the retrieved codes, and exposes memory key-value pairs to the attention block. It further introduces Temporal-Aware State-Relation Differential Gated DeltaNet (TDGD), which uses memory to purify recurrent writing and reading by suppressing memory-covered updates and removing memory-aligned readout responses. This design turns recurring semantics from state-competing signals into memory-retrievable patterns, allowing the recurrent state to focus on dynamic transitions and alleviating semantic state sink with linear-time efficiency. Experiments on public and industrial datasets demonstrate the effectiveness and efficiency of SinkRec.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
