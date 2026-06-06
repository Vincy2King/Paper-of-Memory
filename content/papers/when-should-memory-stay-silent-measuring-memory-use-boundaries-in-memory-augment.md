# When Should Memory Stay Silent: Measuring Memory-Use Boundaries in Memory-Augmented Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.06055v1
- Published: 2026-06-04
- Updated: 2026-06-04
- Authors: Lingxiang Xu, Jiaoyun Yang, Min Hu, Hongtu Chen, Ning An
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.06055v1

## One-Sentence Summary
Long-term memory enables language model agents to support personalized interactions, but it remains unclear when available memories warrant integration into responses.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables language model agents to support personalized interactions, but it remains unclear when available memories warrant integration into responses.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory evaluations emphasize retrieval accuracy and downstream task utility, while overlooking whether retrieved sensitive memory content is warranted in the current turn.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory augmented, memory-augmented
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory enables language model agents to support personalized interactions, but it remains unclear when available memories warrant integration into responses. Existing memory evaluations emphasize retrieval accuracy and downstream task utility, while overlooking whether retrieved sensitive memory content is warranted in the current turn. We introduce RBI-Eval, a controlled measurement study built around a probe set that compares model behavior with and without access to sensitive memory under identical benign prompts. We evaluate four base LLMs against a matched no-memory reference across four memory-access settings: full-context exposure and three retrieval systems. Our results reveal substantial behavioral divergence. With memory available, the separation score for sensitive-memory integration decreases by 8.9\%--26.6\% relative to the matched no-memory reference for GPT-5.4-mini, but by 51.1\%--82.9\% for Claude-Sonnet-4.6, DeepSeek-V4-Flash, and Qwen3.5-9B. Control experiments on DeepSeek and GPT-5.4-mini show this effect is specific to sensitive content, rather than general personalization. Retrieval systems reduce exposure but do not eliminate integration once sensitive memory reaches the generator. These findings suggest safe personalization requires memory-aware decisions at both retrieval and generation time.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
