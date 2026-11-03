# InteractionBench: Measuring Timing, Task Accuracy, Whisper and Volume, and Grounding in Real-Time Voice Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.02430v1
- Published: 2026-11-02
- Updated: 2026-11-02
- Authors: Richard Yucheng He, Chen Xu, Yihang Liu, Tairan Chen, Baodong Cao
- Tags: benchmark, conversation
- Categories: cs.SD, cs.CL, eess.AS
- URL: http://arxiv.org/abs/2611.02430v1

## One-Sentence Summary
Most benchmarks for real-time voice systems focus on one aspect, such as turn-taking, instruction following, paralinguistic control, or conversational memory, each with its own...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Most benchmarks for real-time voice systems focus on one aspect, such as turn-taking, instruction following, paralinguistic control, or conversational memory, each with its own data and set of systems.

进一步看，论文的核心做法或实验重点可以概括为：We present InteractionBench, a benchmark and evaluation harness that measures four dimensions on the same systems from the same recorded user audio: conversational timing, spoken-task accuracy, whisper and volume, and...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, conversation
- 检索关键词命中：conversational memory
- 来源分类信息：cs.SD, cs.CL, eess.AS

## Abstract Snapshot
Most benchmarks for real-time voice systems focus on one aspect, such as turn-taking, instruction following, paralinguistic control, or conversational memory, each with its own data and set of systems. We present InteractionBench, a benchmark and evaluation harness that measures four dimensions on the same systems from the same recorded user audio: conversational timing, spoken-task accuracy, whisper and volume, and groundedness in conversations of more than twenty turns. The benchmark contains 221 items per system in thirteen scenarios. Before any system runs, we fix the expected floor-control actions for spoken tasks by rule and take the expected answers from scripted dialogues. We score whispering from the audio signal. We evaluate GPT-Live, GPT-Realtime, Gemini Live, Moshi, PersonaPlex, Freeze-Omni, and a turn-based cascade in 1,519 graded runs. Among the six full-duplex systems, timing and spoken-task accuracy are rank-correlated ($ρ= 0.83$), while the cascade has the highest spoken-task score (38/50) and the second-lowest timing score. No system corrects a user's grammar within the required window. Only Gemini Live whispers on most requests (8/10). Hosted systems pass 67-88% of groundedness probes, compared with 14-35% for open full-duplex models. Timing is measured where the client hears each system, so the timing of hosted systems includes network delay: for GPT-Live, whose server reports its own clock, removing a delay of about 1.5 s lowers its timing score from 86% to 56%. We also document where the protocol differs across systems, including the text instructions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
