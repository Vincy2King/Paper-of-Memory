# Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.30252v1
- Published: 2026-08-31
- Updated: 2026-08-31
- Authors: Tong Yuan, Chengxi Liao, Zeyi Wen
- Tags: agent, context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2608.30252v1

## One-Sentence Summary
Long-context LLM applications such as document summarization and multi-turn agents require generation from prefixes spanning tens of thousands of tokens, making decoding latency...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-context LLM applications such as document summarization and multi-turn agents require generation from prefixes spanning tens of thousands of tokens, making decoding latency a major bottleneck.

进一步看，论文的核心做法或实验重点可以概括为：Speculative decoding (SD) reduces latency without changing model outputs, but its speedup depends on both accepted draft tokens and draft-step latency: Lightweight drafts are fast but lack the capacity to capture...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.LG

## Abstract Snapshot
Long-context LLM applications such as document summarization and multi-turn agents require generation from prefixes spanning tens of thousands of tokens, making decoding latency a major bottleneck. Speculative decoding (SD) reduces latency without changing model outputs, but its speedup depends on both accepted draft tokens and draft-step latency: Lightweight drafts are fast but lack the capacity to capture long-range dependencies, whereas strong independent drafts recover acceptance but incur growing KV-access cost at long prefixes. We introduce memory-augmented drafting for long-context SD, equipping a strong independent draft with compressed draft-side KV memory: A lightweight adaptor constructs and incrementally updates this memory to retain distant information and exact recent context. The target verifier retains its full KV cache and applies the standard accept/reject rule, preserving SD's lossless guarantee. Experiments on Llama~3.1-8B and 70B targets at prefix lengths up to 32K show that our method reduces draft-side memory by over 70%. It achieves speedups of up to 2.08x and 3.33x , respectively, over autoregressive decoding.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
