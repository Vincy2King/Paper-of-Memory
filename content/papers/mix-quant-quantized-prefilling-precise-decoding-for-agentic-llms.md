# Mix-Quant: Quantized Prefilling, Precise Decoding for Agentic LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.20315v1
- Published: 2026-05-19
- Updated: 2026-05-19
- Authors: Haiquan Lu, Zigeng Chen, Gongfan Fang, Xinyin Ma, Xinchao Wang
- Tags: agent, benchmark, context, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.20315v1

## One-Sentence Summary
LLM agents have recently emerged as a powerful paradigm for solving complex tasks through planning, tool use, memory retrieval, and multi-step interaction.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM agents have recently emerged as a powerful paradigm for solving complex tasks through planning, tool use, memory retrieval, and multi-step interaction.

进一步看，论文的核心做法或实验重点可以概括为：However, these agentic workflows often introduce substantial input-side overhead, making the compute-intensive prefilling stage a key bottleneck in long-context, multi-turn inference.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
LLM agents have recently emerged as a powerful paradigm for solving complex tasks through planning, tool use, memory retrieval, and multi-step interaction. However, these agentic workflows often introduce substantial input-side overhead, making the compute-intensive prefilling stage a key bottleneck in long-context, multi-turn inference. In this work, we propose Mix-Quant, a simple and effective phase-aware quantization framework for fast agentic inference. We first investigate FP4 quantization in agentic LLM workflows and observe that quantizing the entire inference process can incur significant performance degradation. In contrast, the prefilling stage exhibits substantial quantization redundancy and can therefore be quantized with minimal accuracy loss, despite being the dominant source of computation. Based on this insight, we apply high-throughput NVFP4 quantization to the prefilling phase while preserving BF16 precision for decoding. By decoupling prefilling acceleration from decoding quality, Mix-Quant combines phase-aware algorithmic quantization with hardware-efficient NVFP4 execution to alleviate the inference bottleneck in LLM agents. Extensive experiments across long-context and agentic benchmarks demonstrate that Mix-Quant largely preserves task performance while delivering significant efficiency improvements, achieving up to a 3x speedup during prefilling.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
