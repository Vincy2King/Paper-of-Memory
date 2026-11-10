# Correct Answers from Insufficient Histories: A Controlled Study of Agent Memory Evaluation

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.11840v1
- Published: 2026-11-09
- Updated: 2026-11-09
- Authors: Quan Xue, Zerui Yang, Chaorui Zhang, Haolin Ruan, Xueyan Niu, Xuanyu Zheng, Xiyuan Wang, Weixi Zhang, Wei Han, Bo Bai
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.11840v1

## One-Sentence Summary
An answer can match the reference for a complete agent history even when the reader's visible history does not determine it.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An answer can match the reference for a complete agent history even when the reader's visible history does not determine it.

进一步看，论文的核心做法或实验重点可以概括为：We study this distinction using executable device logs.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
An answer can match the reference for a complete agent history even when the reader's visible history does not determine it. We study this distinction using executable device logs. Our protocol separates reference agreement, certified evidence sufficiency, and context-appropriate behavior. Insufficiency requires two legal histories yielding byte-identical visible contexts but different answers; public chronology and query cutoffs certify sufficient prefixes. On 80 confirmation histories, Qwen3-32B matches 87 hidden references among 203 insufficient raw-prefix instances, with only seven appropriate abstentions. A fixed-input DeepSeek-V4-Flash replication matches 85 and abstains on 21 of the same 203 instances. Each reader makes 1,600 requests. Compact CSV's estimated appropriateness effects remain inconclusive: +3.16 percentage points, clustered 95% interval [0.00,6.57], for Qwen and +2.46, [-1.84,6.94], for DeepSeek. A separate held-out judge study achieves 99.38% correctness but retains support errors and truncations; a deterministic baseline solves all constructed cases. These results support an evaluation diagnosis across two hosted reader configurations, not gains for a general memory system or natural-language evidence assessment.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
