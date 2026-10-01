# CoEM: Empowering Long-Context Reasoning with Commit-on-Evidence Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.36935v2
- Published: 2026-09-29
- Updated: 2026-09-30
- Authors: Jingguang Li, Yebo Wu, Zuyi Guo, Kailang Ma, Xianjie Dai, Han Zheng, Benwang Chen, Li Li, Can Rong, Heye Huang
- Tags: compression, context
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2609.36935v2

## One-Sentence Summary
Long-context reasoning is essential for complex and long-horizon tasks, yet the performance of large language models (LLMs) degrades as context length increases.

## Introduction
这篇论文被纳入仓库，是因为它和 `compression, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-context reasoning is essential for complex and long-horizon tasks, yet the performance of large language models (LLMs) degrades as context length increases.

进一步看，论文的核心做法或实验重点可以概括为：Recent approaches address this by processing input chunk by chunk while maintaining a bounded textual memory in model context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：compression, context
- 检索关键词命中：context memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Long-context reasoning is essential for complex and long-horizon tasks, yet the performance of large language models (LLMs) degrades as context length increases. Recent approaches address this by processing input chunk by chunk while maintaining a bounded textual memory in model context. However, premature information compression can discard critical details essential for subsequent reasoning. In this paper, we introduce Commit-on-Evidence Memory (CoEM), which learns when to convert source evidence into compact memory facts. Specifically, under a fixed context-memory budget, CoEM preserves potentially useful source excerpts verbatim in a pending set, allowing subsequent context to clarify their relevance before irreversible compression. As new context arrives, a learned policy revisits each pending excerpt and decides whether to promote it to the committed memory, retain it for further consideration, or discard it. A frozen verifier ensures proposed facts are accepted only if supported by retained excerpts and current context. To further guide effective memory management, we train this policy using reinforcement learning by combining fine-grained, step-level evidence rewards with final answer rewards. Extensive experiments demonstrate that CoEM consistently improves long-context reasoning. When evaluated on 6,400 documents long-context input, CoEM outperforms the strongest memory baseline by 10.4-11.4 F1 points on Qwen3.5-9B. Code repository: https://github.com/benmagnifico/CoEM.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
