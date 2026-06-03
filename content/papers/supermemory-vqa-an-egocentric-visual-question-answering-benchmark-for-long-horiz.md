# SuperMemory-VQA: An Egocentric Visual Question-Answering Benchmark for Long-Horizon Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.00825v1
- Published: 2026-05-30
- Updated: 2026-05-30
- Authors: Samiul Alam, Shakhrul Iman Siam, Michael J. Proulx, James Fort, Richard Newcombe, Hyo Jin Kim, Mi Zhang
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.CV, cs.ET, cs.HC, cs.MA
- URL: http://arxiv.org/abs/2606.00825v1

## One-Sentence Summary
AI glasses present a compelling platform for AI agents to serve as personalized memory assistants.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI glasses present a compelling platform for AI agents to serve as personalized memory assistants.

进一步看，论文的核心做法或实验重点可以概括为：To be genuinely useful, such systems must move beyond short-term video comprehension and address memory gaps that humans experience for practical, personal, or social purposes over longitudinal egocentric video streams.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.CV, cs.ET, cs.HC, cs.MA

## Abstract Snapshot
AI glasses present a compelling platform for AI agents to serve as personalized memory assistants. To be genuinely useful, such systems must move beyond short-term video comprehension and address memory gaps that humans experience for practical, personal, or social purposes over longitudinal egocentric video streams. However, existing egocentric datasets predominantly focus on action recognition or generic QAs from short clips, measuring perceptual capabilities rather than realistic human memory needs. We introduce SuperMemory-VQA, an egocentric visual question answering (VQA) dataset for evaluating AI assistants on practical, long-horizon memory tasks. It contains 52.9 hours of everyday activities recorded with AI glasses, including synchronized RGB video, audio transcription, eye gaze, IMU, and SLAM trajectories. Through a human-verified annotation pipeline, we construct grounded 4,853 question-answer pairs that span object and location memory, intent recall, visual scene recall, timeline reconstruction, conversational memory, and in-context retrieval. Each question is posed as multiple-choice with an explicit "unanswerable" option to test hallucination robustness. Benchmarking leading agentic frameworks and LLM backbones reveals that existing systems remain far from reliable on real-world memory tasks, highlighting the need for new architectures for grounded AI memory that can answer only when evidence is sufficient. A participant survey further supports that our questions are realistic, useful, and aligned with everyday memory needs.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
