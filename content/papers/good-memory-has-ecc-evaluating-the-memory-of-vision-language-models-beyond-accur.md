# Good Memory Has ECC: Evaluating the Memory of Vision-Language Models Beyond Accuracy

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.00103v1
- Published: 2026-08-31
- Updated: 2026-08-31
- Authors: Shmuel Berman, Jia Deng
- Tags: agent, benchmark, compression
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2609.00103v1

## One-Sentence Summary
Memory is widely viewed as an important unsolved problem for LLMs and VLMs, and current benchmarks typically evaluate it by testing accuracy over long text or video.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory is widely viewed as an important unsolved problem for LLMs and VLMs, and current benchmarks typically evaluate it by testing accuracy over long text or video.

进一步看，论文的核心做法或实验重点可以概括为：However, accuracy alone misses properties that matter for real long-horizon tasks.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression
- 检索关键词命中：memory compression
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Memory is widely viewed as an important unsolved problem for LLMs and VLMs, and current benchmarks typically evaluate it by testing accuracy over long text or video. However, accuracy alone misses properties that matter for real long-horizon tasks. We introduce ECCBench, a benchmark and evaluation protocol that measures memory beyond a system's capacity--its raw accuracy at a specific budget--via three axes we call ECC: efficiency--the computation, in FLOPs, needed to answer from memory; compression--whether compressible inputs are remembered more accurately or efficiently; and calibration--whether the system abstains in response to its own uncertainty and the cost of an error. We find that pretrained VLMs compress their memory over text but not video and are poorly calibrated on both. Among a broader set of memory backbones, several non-Transformer architectures achieve better compression-calibration tradeoffs than RoPE Transformers, suggesting they may be useful components for agents operating over long horizons.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
