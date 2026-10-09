# Real Long-Term Memory for AI: A 50-Million-Token Window That Is Faster and Cheaper Than Recompute

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.10845v1
- Published: 2026-10-07
- Updated: 2026-10-07
- Authors: Sietse Schelpe
- Tags: benchmark, context, long-term
- Categories: cs.CL, cs.AI, cs.DC, cs.LG
- URL: http://arxiv.org/abs/2610.10845v1

## One-Sentence Summary
A large language model can only use the text that fits in its context window, and it recomputes its internal key-value (KV) state for a prompt every time the prompt is sent.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A large language model can only use the text that fits in its context window, and it recomputes its internal key-value (KV) state for a prompt every time the prompt is sent.

进一步看，论文的核心做法或实验重点可以概括为：We test a memory layer, the public package galahad-kv, that saves the KV state of each block of about 16,000 tokens to encrypted local NVMe disk and loads it back later, byte-exact, without recomputing it.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL, cs.AI, cs.DC, cs.LG

## Abstract Snapshot
A large language model can only use the text that fits in its context window, and it recomputes its internal key-value (KV) state for a prompt every time the prompt is sent. We test a memory layer, the public package galahad-kv, that saves the KV state of each block of about 16,000 tokens to encrypted local NVMe disk and loads it back later, byte-exact, without recomputing it. We ran it on 50,000,000 tokens of real public text, served through vLLM on one NVIDIA H100, with Gemma 4 12B and Gemma 4 31B. Every block we probed was loaded back from the encrypted store with no recompute (100 of 100, at depths from 0 to 50M tokens) on both models. Loading a block was 2.8x to 4.3x faster than recomputing it and used 8.8x to 12.3x less GPU energy, and GPU memory stayed flat over the whole 50M-token stream. Asked about facts planted millions of tokens earlier, the 12B model gave the right answer 82 times out of 100 and the 31B model 98 times out of 100. Neither model made up an answer. The limits are as follows. This is reuse of stored state, not a wider attention window: one block is loaded at a time, and how well a question is answered depends on the model. Writing the memory is a one-time cost, and the store takes terabytes of local NVMe disk. We describe the test protocol, which is built to resist common ways of gaming long-context benchmarks, and give a single-GPU reproduction that uses public software and a free licence for the package.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
