# CommitKV: Lifecycle-Aware KV Cache Compression via Commit Transitions for Multi-Turn Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07855v1
- Published: 2026-08-08
- Updated: 2026-08-08
- Authors: Weizhong Huang, Jinchao Zhang, Xiawu Zheng
- Tags: agent, benchmark, compression
- Categories: cs.LG
- URL: http://arxiv.org/abs/2608.07855v1

## One-Sentence Summary
Multi-turn Reasoning-and-Acting (ReAct) agents accumulate growing trajectories of reasoning, tool calls, and observations.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-turn Reasoning-and-Acting (ReAct) agents accumulate growing trajectories of reasoning, tool calls, and observations.

进一步看，论文的核心做法或实验重点可以概括为：Their key-value (KV) caches grow accordingly, increasing memory use and attention cost during model inference.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Multi-turn Reasoning-and-Acting (ReAct) agents accumulate growing trajectories of reasoning, tool calls, and observations. Their key-value (KV) caches grow accordingly, increasing memory use and attention cost during model inference. Existing KV cache compression methods reduce these costs by evicting states with low attention scores. However, low attention in the current turn does not imply future irrelevance, as temporarily inactive information may become important later. Snapshot-based eviction methods therefore do not explicitly distinguish temporarily dormant information from information that appears to have completed its role. In this paper, we present CommitKV, which identifies KV lifecycles through commit transitions. Specifically, CommitKV first divides completed agent events into token pages and compares each eligible page's deletion effect before a tool-call commit and after the commit's returned observation has been incorporated. Based on these paired measurements, CommitKV distinguishes dormant pages from high-to-low completion candidates. It then applies a greedy joint test, accepting candidates for retirement only when their combined post-commit effect remains bounded. Finally, at a later compression checkpoint, accepted pages are excluded, a bounded set of pages awaiting post-commit measurement is protected, and the remaining KV states are retained within the cache budget using the same token indices for keys, values, and absolute positions. These mechanisms ensure that CommitKV can distinguish dormant information from information that has completed its observed role and can be safely removed. Experiments on various benchmarks show that CommitKV reduces agent memory use, accelerates end-to-end inference, and achieves higher accuracy than existing KV cache compression methods.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
