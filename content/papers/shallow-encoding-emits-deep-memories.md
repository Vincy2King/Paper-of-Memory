# Shallow Encoding Emits Deep Memories

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.06084v1
- Published: 2026-11-04
- Updated: 2026-11-04
- Authors: Mingyuan Ma, Yangmin Li, Harris Nover, Zheyu Fu, Po-Han Huang, Alex Settle, Ashwin Nanjappa
- Tags: agent, compression
- Categories: cs.LG, cs.DC
- URL: http://arxiv.org/abs/2611.06084v1

## One-Sentence Summary
Hybrid language models interleave a few softmax-attention layers with many linear-attention or state-space layers, so every layer keeps a memory of earlier tokens: a key-value...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Hybrid language models interleave a few softmax-attention layers with many linear-attention or state-space layers, so every layer keeps a memory of earlier tokens: a key-value cache or a fixed-size recurrent state.

进一步看，论文的核心做法或实验重点可以概括为：Serving them spends more compute and high-bandwidth memory on these memories than the output requires.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression
- 检索关键词命中：working memory
- 来源分类信息：cs.LG, cs.DC

## Abstract Snapshot
Hybrid language models interleave a few softmax-attention layers with many linear-attention or state-space layers, so every layer keeps a memory of earlier tokens: a key-value cache or a fixed-size recurrent state. Serving them spends more compute and high-bandwidth memory on these memories than the output requires. The prefill runs every layer for every prompt token, and every decode step loads and stores whole recurrent states, which on Qwen3.8-Flash-Next take as many bytes per request as the attention cache of thousands of tokens. We find two properties of trained hybrids that locate this excess. First, writes are easier than reads: writing a deep layer's memory of a token needs little of the deep computation that predicting the next token needs. Trained copies of the deep layers' write paths, which we call emitters, therefore write a prompt's deep memories from the residual stream of a shallower anchor layer, and all prompt tokens but the last run as few as 63% of the layers. Second, recurrent states have a state sink: most of their energy lies in a rank-one term along a fixed direction of each head, and the rest is a low-rank working memory. SEED builds on both: it makes the prefill shallow in depth and the decode state shallow in representation. Each recurrent state is stored as its sink plus low-rank factors, which the Gated DeltaNet, Kimi Delta Attention and Mamba-2 updates extend exactly; we prove that the open-loop error of the periodic compressions back to low rank is bounded independently of their number. SEED keeps the original weights frozen, compresses no attention cache, and runs all layers for every generated token. On six checkpoints of five production hybrids of 30B to over 300B parameters, it is nearly lossless on eleven official exams. Served with SGLang on NVIDIA GB300 GPUs on an agentic-coding trace, it raises the per-GPU throughput of Qwen3.8-Flash-Next 1.2-1.4x.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
