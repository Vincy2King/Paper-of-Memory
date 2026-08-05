# Memory-Bench at Short Context: Only Persistent Memory Beats Softmax Attention at 2048 Tokens

- Source: OpenReview
- Venue: CBW Poster
- Paper ID: openreview:XzM3pojgHN
- Published: 2026-08-04
- Updated: 2026-08-04
- Authors: Rob Sneiderman
- Tags: context
- Categories: colmweb.org/COLM/2026/Workshop/CBW/-/Submission
- URL: https://openreview.net/forum?id=XzM3pojgHN

## One-Sentence Summary
We report a controlled plug-in comparison of four transformer memory mechanisms at a single fixed context length of 2048 tokens.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CBW Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：We report a controlled plug-in comparison of four transformer memory mechanisms at a single fixed context length of 2048 tokens.

进一步看，论文的核心做法或实验重点可以概括为：Each mechanism is dropped into the same 286M-parameter nanochat GPT and trained from scratch under identical data, optimizer, and compute, so the only thing that varies is the memory module.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CBW Poster
- 高亮主题命中：context
- 检索关键词命中：persistent memory
- 来源分类信息：colmweb.org/COLM/2026/Workshop/CBW/-/Submission

## Abstract Snapshot
We report a controlled plug-in comparison of four transformer memory mechanisms at a single fixed context length of 2048 tokens. Each mechanism is dropped into the same 286M-parameter nanochat GPT and trained from scratch under identical data, optimizer, and compute, so the only thing that varies is the memory module. At 2048 tokens, Persistent Memory is the one mechanism that significantly improves on softmax attention (-1.79 mBPB, p=0.002). The other three degrade quality: RMT by 39.25 mBPB (p<0.001), TTT-Linear by 6.00 mBPB (p<0.001), and Gated DeltaNet by 1.35 mBPB (p=0.008). We state the scope plainly: 2048 tokens is a short-context regime, and RMT and TTT-Linear were designed for 8k+ contexts, so the negative results here are about behaviour at this length and are not a verdict on those mechanisms in the regime they target. Read that way, the finding is a clean negative result with a reproducible protocol: at short context, three of four tested mechanisms cost quality rather than add it, and the harness makes the longer-context comparison straightforward to run next. A multi-context sweep (2048/4096/8192) confirms the Persistent Memory gain is not an artifact of the shortest length. Code, weights, and seeds are released under MIT.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
