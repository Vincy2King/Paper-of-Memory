# LSTMem: Hierarchical Long Short-Term Online Memory for Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.33268v1
- Published: 2026-09-27
- Updated: 2026-09-27
- Authors: Xianglong Shi, Ruijie Yang, Sirui Zhao, Shukang Yin, Zihao Bian, Tinghao Yi, Enhong Chen
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.33268v1

## One-Sentence Summary
Large language models increasingly serve as long-horizon assistants and agents, where they must both accumulate information across interactions and make the relevant parts...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models increasingly serve as long-horizon assistants and agents, where they must both accumulate information across interactions and make the relevant parts available when later requests depend on them.

进一步看，论文的核心做法或实验重点可以概括为：Existing compact online memories typically use a single persistent state both to accumulate history and to serve readout, so what the memory stores cannot be controlled separately from what it exposes to the current...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language models increasingly serve as long-horizon assistants and agents, where they must both accumulate information across interactions and make the relevant parts available when later requests depend on them. Existing compact online memories typically use a single persistent state both to accumulate history and to serve readout, so what the memory stores cannot be controlled separately from what it exposes to the current computation. We propose LSTMem, an LSTM-inspired online memory that instead equips each layer of a frozen LLM with two matrix-valued states: a cell state that accumulates history and a hidden state whose readouts correct the backbone's attention. Input and forget gates control what the cell stores, while an output gate separately controls what the cell exposes through the hidden state. LSTMem further connects memory across depth through forward hidden-state propagation and block-end feedback, and uses higher-layer reconstruction gradients to refine lower-layer cell states before rebuilding hidden states from shallow to deep layers. Across memory benchmarks on Qwen3-4B-Instruct, LSTMem consistently improves MemoryAgentBench, LoCoMo, and HotpotQA over the plain backbone. Comparisons further show that the LSTM-based memory formulation outperforms an associative-memory counterpart, while removing cross-layer hidden-memory propagation degrades performance. These results demonstrate the benefits of separating memory accumulation from memory expression and organizing memory hierarchically across model depth. The code is available at https://github.com/Longchentong/LSTMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
