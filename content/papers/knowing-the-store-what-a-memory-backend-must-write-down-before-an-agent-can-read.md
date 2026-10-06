# Knowing the Store: What a Memory Backend Must Write Down Before an Agent Can Read It

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.04794v1
- Published: 2026-10-03
- Updated: 2026-10-03
- Authors: Ansuman Mullick, Eray Tüzün
- Tags: agent, benchmark, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.04794v1

## One-Sentence Summary
An agent with long-term memory can answer from a record it should no longer use, such as a plan the user later cancelled.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：An agent with long-term memory can answer from a record it should no longer use, such as a plan the user later cancelled.

进一步看，论文的核心做法或实验重点可以概括为：We ask what a memory store must expose for an agent to know this before retrieving anything, and we score that judgment on its own, as metamemory monitoring.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
An agent with long-term memory can answer from a record it should no longer use, such as a plan the user later cancelled. We ask what a memory store must expose for an agent to know this before retrieving anything, and we score that judgment on its own, as metamemory monitoring. Readers see only a value-free summary: record counts by lifecycle state and a list of attribute names. Each of 148 questions is asked against three versions of one store that differ in one attribute, so wording cannot give the answer away. What a model adds depends on the length of that list. On the short lists the benchmark's ground truth produces (2.6 names on average), none of five language models reliably beats a cosine-similarity lookup over the names, and the three stronger ones are equivalent to it within 0.05. Under a control that fixes counts and list length, none is reliably above it and none is shown equivalent. On lists longer than the stores we tested write, padded to 60 names, the lookup loses 0.18; GPT-5.6 Luna and Sol lose 0.06 to 0.07 and lead it by 0.13 to 0.14, while the other three fall with it. The lead holds for Sol against a sibling padded to the same length and counts. Reworded to share no word with the names, the lookup loses 0.02 and one stronger reader edges 0.04 ahead. On the short lists the three stronger readers lead only where the summary counts a state without naming it, and one count feature closes that lead within a question, though not when items are pooled. The backends we tested omit or misstate this information: under FR-Bank's own metadata, GPT-4.1 mini, Haiku 4.5 and the lookup fall from 0.73, 0.82 and 0.75 to 0.60, 0.71 and 0.59. In these tests, what the store wrote down limited every reader we gave it to. All stores are synthetic; control, whether a better judgment yields a better answer, is left to a later study.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
