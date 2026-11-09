# Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.09807v1
- Published: 2026-11-06
- Updated: 2026-11-06
- Authors: Osamudiamen Edogun, Joshua Obigwe, Irfan Mehmood
- Tags: agent, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.09807v1

## One-Sentence Summary
A conversational agent that remembers has to decide what to keep.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A conversational agent that remembers has to decide what to keep.

进一步看，论文的核心做法或实验重点可以概括为：Retrieval-augmented generation keeps the transcript and searches it; the alternative is to compact each turn into atomic facts and search those.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CL

## Abstract Snapshot
A conversational agent that remembers has to decide what to keep. Retrieval-augmented generation keeps the transcript and searches it; the alternative is to compact each turn into atomic facts and search those. We compare the two on LoCoMo, with both arms answering all 1,985 questions in one window, against the same stores, with the same generator and judge, and both predictions on one row, which licenses McNemar's exact test on the 512 questions where they disagree. On the four categories comparable work reports, compaction scores 71.4 per cent against 64.6, a lead of 6.8 points (p = 5.5e-08) at 34 per cent fewer prompt tokens. On all five, including the adversarial set comparable work drops, the lead falls to 2.0 and stops being significant, because the baseline leads adversarial by 14.6. That loss has a structure. Our lead falls as the reference answer demands more source wording, 9.6 points ahead at one or two reference words and 3.1 behind past eight, with token overlap moving the same way, so the judge is not the cause. Compaction keeps what a fact asserts and discards how it was said, so it wins where the answer is a value and loses where it is a phrasing. We also report four negative results with their power calculations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
