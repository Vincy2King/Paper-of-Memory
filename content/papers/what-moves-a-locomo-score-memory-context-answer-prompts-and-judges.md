# What Moves a LoCoMo Score? Memory Context, Answer Prompts and Judges

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.19199v1
- Published: 2026-11-14
- Updated: 2026-11-14
- Authors: Nikhil Kumar Jha, Amitoj Cheema
- Tags: agent, benchmark, context, conversation, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.19199v1

## One-Sentence Summary
LoCoMo is a widely reported benchmark for long-term conversational memory, but published scores mix memory quality with choices of answer prompt, judge and baseline layout that...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LoCoMo is a widely reported benchmark for long-term conversational memory, but published scores mix memory quality with choices of answer prompt, judge and baseline layout that are rarely reported together.

进一步看，论文的核心做法或实验重点可以概括为：We measure how much these choices move a score, and evaluate Becos, a team memory system for coding agents, as a black box under all of them: ten conversations (1,540 questions), two answer models (gpt-4o-mini,...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term
- 检索关键词命中：conversational memory
- 来源分类信息：cs.AI

## Abstract Snapshot
LoCoMo is a widely reported benchmark for long-term conversational memory, but published scores mix memory quality with choices of answer prompt, judge and baseline layout that are rarely reported together. We measure how much these choices move a score, and evaluate Becos, a team memory system for coding agents, as a black box under all of them: ten conversations (1,540 questions), two answer models (gpt-4o-mini, gpt-4.1-mini), two answer prompts and three LLM judges, against a whole-conversation baseline rerun under identical conditions. Changing only the judge moves a score by up to 7.2 points and changing only the answer prompt by up to 9.3. A blind human check of 150 answers finds the judges reliable when they agree, and the primary judge's errors on disputed answers working against Becos rather than for it. Becos answers from a context with 90% fewer characters than the whole conversation. Its configuration was developed on LoCoMo itself, so there is no held-out set. With gpt-4o-mini answers it scores clearly higher than the whole conversation (79.7 vs 73.0 with the short prompt, paired 95% interval for the difference +3.8 to +9.5; 88.8 vs 77.5 with a step-by-step prompt). With gpt-4.1-mini answers the two score about the same (83.2 vs 83.1; 92.5 vs 92.1). We release every answer and verdict and the scoring script.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
