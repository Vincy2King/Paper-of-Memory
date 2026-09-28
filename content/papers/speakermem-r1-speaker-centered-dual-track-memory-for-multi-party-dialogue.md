# SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.26780v2
- Published: 2026-09-22
- Updated: 2026-09-23
- Authors: Haobo Zheng, Tan Tang, Yan Chen, Weijie Wang, Yingcai Wu
- Tags: benchmark, conversation, long-term
- Categories: cs.CL, cs.AI, cs.IR, cs.LG
- URL: http://arxiv.org/abs/2609.26780v2

## One-Sentence Summary
Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals...

进一步看，论文的核心做法或实验重点可以概括为：Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed across members, groups, and time.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, conversation, long-term
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL, cs.AI, cs.IR, cs.LG

## Abstract Snapshot
Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals perceive one another, what information is shared by the group, and how states change over time. Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed across members, groups, and time. Together, these issues reveal two core bottlenecks: message attribution and relational understanding in multi-party dialogue, and state reconstruction from interleaved histories. To address both, we propose $\textbf{SpeakerMem-R1}$: its dual-track memory stores speaker-labeled verbatim messages and derived states organized into person-level and group-level views, then combines evidence from both tracks by entity, event, and time at query time. To reduce attribution and update errors during structured memory construction while enabling local deployment, we train Writer-R1 with SpeakerLevenshtein and speaker-conditioned GRPO. On GroupMemBench, SocialMemBench, and EverMemBench, SpeakerMem-R1 achieves binary accuracies of 47.9%, 69.2%, and 61.9%, respectively. On the publicly reported EverMemBench leaderboard from EverMind-AI, we achieves 62.33%, the best reported result among the latest state-of-the-art frameworks. It also achieves 70.85% on all 1,986 LoCoMo questions, which we use as a two-person long-term conversation boundary test. In a controlled evaluation of 305 questions, RL raises the SFT Writer's mean accuracy from 57.38% to 68.20%. We report both binary accuracy and token-F1, and ablations show that the verbatim and structured tracks, as well as person-level and group-level views, are complementary under the standardized evaluation interface.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
