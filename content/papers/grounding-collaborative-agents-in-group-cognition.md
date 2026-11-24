# Grounding Collaborative Agents in Group Cognition

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.29036v1
- Published: 2026-11-21
- Updated: 2026-11-21
- Authors: Zhaoxuan Tan, Mengting Wan, Jingbo Yang, Kwei-Herng Lai, Renyi Qu, Lorenzo Jaime Flores, Meng Jiang, Longqi Yang, Victor Poznanski, Pei Zhou
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.29036v1

## One-Sentence Summary
Collaborative agents joining an ongoing team rely on shared context to connect multi-party interaction histories with downstream coordination decisions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Collaborative agents joining an ongoing team rely on shared context to connect multi-party interaction histories with downstream coordination decisions.

进一步看，论文的核心做法或实验重点可以概括为：Existing work typically focuses either on retrieving historical facts from conversation logs, which surfaces isolated evidence without capturing who knows or owns what, or on evaluating end-to-end interactions, which...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Collaborative agents joining an ongoing team rely on shared context to connect multi-party interaction histories with downstream coordination decisions. Existing work typically focuses either on retrieving historical facts from conversation logs, which surfaces isolated evidence without capturing who knows or owns what, or on evaluating end-to-end interactions, which conflates preparation with execution and lacks direct supervision because a team's history has no single ground-truth summary. To bridge this gap, we formulate group briefing, the task of reconstructing task-relevant group cognition across participants' expressed beliefs, group dynamics, and grounding gaps, and introduce a four-domain benchmark of 1,351 requests and 9,975 verified reference points paired with a two-stage evaluation pipeline combining reference-point coverage and downstream collaboration simulation. Using this pipeline, we show that GroupBrief, a simple task-guided approach that iteratively probes the message history and synthesizes a structured brief without offline memory indexing or graph construction, outperforms ten retrieval and agent-memory baselines in overall coverage with gpt-5.4-mini, while benchmarking nine language models reveals that prospective friction remains harder to recover than past state across model scales. We further use reference-point coverage as a feedback signal for harness optimization, refining GroupBrief's retrieval and synthesis instructions while keeping model weights frozen. On held-out Test projects, GroupBrief (optimized) improves coverage by 2.54 percentage points for gpt-5.4-mini and 12.88 for gpt-5.6-luna, achieving 64.46% and 68.42% preference over no brief in downstream simulations. These results establish our benchmark and evaluation pipeline as a foundation for measuring and optimizing how collaborative agents ground in group cognition.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
