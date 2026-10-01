# Who Said What, and Will It Be Remembered? Evaluating Persistent Speaker Attribution Across Meetings

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.39344v1
- Published: 2026-09-30
- Updated: 2026-09-30
- Authors: Shantanu Vispute, Aditya Mishra, Siddhartha Saxena
- Tags: benchmark, conversation, long-term
- Categories: cs.SD, cs.AI
- URL: http://arxiv.org/abs/2609.39344v1

## One-Sentence Summary
Speech transcripts used as long-term memory must preserve both words and stable speaker identities.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Speech transcripts used as long-term memory must preserve both words and stable speaker identities.

进一步看，论文的核心做法或实验重点可以概括为：Existing meeting-transcription metrics either ignore speakers or remap anonymous speakers independently in each recording, so they cannot measure whether the same person retains one identity across meetings.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, conversation, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.SD, cs.AI

## Abstract Snapshot
Speech transcripts used as long-term memory must preserve both words and stable speaker identities. Existing meeting-transcription metrics either ignore speakers or remap anonymous speakers independently in each recording, so they cannot measure whether the same person retains one identity across meetings. We evaluate persistent speaker attribution with Speaker Identified cpWER (SI-cpWER), which scores a corpus under one global speaker-ID assignment. The benchmark covers five commercial diarize-then-identify cascades, two open academic baselines, and ThyVoice on the full 129-meeting CHiME-8 NOTSOFAR evaluation set in clean and noiseaugmented form, plus CHiME-6. ThyVoice is our end-to-end reference system; it repairs overlap and gates the evidence used to create and update voiceprints. Requiring persistent identity changes the commercial ranking: ThyVoice records lower SI-cpWER than every evaluated commercial cascade in all three conditions and the lowest mean in the full panel, 47.13 versus 54.75 for the next system. Complementary lexical, diarization, per-recording attribution, and speaker-clustering diagnostics characterize upstream error surfaces in the final attributed record. These results show why persistent attribution must be evaluated directly in systems that reuse conversations across time.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
