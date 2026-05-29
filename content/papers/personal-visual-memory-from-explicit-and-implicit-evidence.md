# Personal Visual Memory from Explicit and Implicit Evidence

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.28806v1
- Published: 2026-05-27
- Updated: 2026-05-27
- Authors: Viet Nguyen, Thao Nguyen, Vishal M. Patel, Yuheng Li
- Tags: agent, benchmark, context, conversation, long-term
- Categories: cs.CV, cs.CL, cs.IR
- URL: http://arxiv.org/abs/2605.28806v1

## One-Sentence Summary
Long-term memory is increasingly important for personalized AI agents, yet existing benchmarks and methods remain largely text-centric.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is increasingly important for personalized AI agents, yet existing benchmarks and methods remain largely text-centric.

进一步看，论文的核心做法或实验重点可以概括为：Even when images are included, the user-specific information needed for later questions is typically recoverable from text alone, and most memory systems reduce image turns to generic captions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, long-term
- 检索关键词命中：long-term memory, memory benchmark, memory benchmarks
- 来源分类信息：cs.CV, cs.CL, cs.IR

## Abstract Snapshot
Long-term memory is increasingly important for personalized AI agents, yet existing benchmarks and methods remain largely text-centric. Even when images are included, the user-specific information needed for later questions is typically recoverable from text alone, and most memory systems reduce image turns to generic captions. Yet images often carry personal information that text rarely states -- both explicit evidence, such as recurring user-associated entities, and implicit evidence, such as latent user facts inferred from visual or multimodal cues. We introduce a benchmark for personal visual memory that targets both forms of evidence, and propose VisualMem, a hybrid visual--text architecture that augments a text-memory backend with a structured personal visual memory module. Rather than collapsing images into captions, VisualMem uses conversational context to resolve identity, ownership, and durable user facts. Experiments show that VisualMem substantially outperforms prior memory systems on our benchmark while remaining competitive on standard text-memory benchmarks, indicating that personal visual memory is a distinct and important component of long-term memory for personalized AI agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
