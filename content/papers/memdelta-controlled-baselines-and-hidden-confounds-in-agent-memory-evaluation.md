# MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.29914v1
- Published: 2026-06-29
- Updated: 2026-06-29
- Authors: Kuan Wang
- Tags: agent, context, retrieval
- Categories: cs.CL, cs.LG
- URL: http://arxiv.org/abs/2606.29914v1

## One-Sentence Summary
Agent memory systems are increasingly evaluated against RAG and full-context baselines, but reported gains often mix changes in the memory method with changes in the language...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent memory systems are increasingly evaluated against RAG and full-context baselines, but reported gains often mix changes in the memory method with changes in the language model, embedding model, or retrieval...

进一步看，论文的核心做法或实验重点可以概括为：We present MemDelta, a controlled evaluation protocol that varies one component at a time on LongMemEval-S (500 questions, 50+ sessions, three model families).

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.LG

## Abstract Snapshot
Agent memory systems are increasingly evaluated against RAG and full-context baselines, but reported gains often mix changes in the memory method with changes in the language model, embedding model, or retrieval pipeline, making it unclear what is actually being measured. We present MemDelta, a controlled evaluation protocol that varies one component at a time on LongMemEval-S (500 questions, 50+ sessions, three model families). Four findings emerge: (1) verbatim RAG matches full-context GPT-4o-mini (47.2% vs. 49.8%, p = 0.34), but the ranking reverses across models: Gemini gains +14pp from full context, while Sonnet gains +31pp from RAG, partly because it refuses 63% of full-context queries; (2) swapping only the embedding model in an identical pipeline shifts accuracy by +6.2pp at n = 500 (p = 0.004), and Mem0 beats MiniLM-RAG by +11pp but loses to cloud-RAG by 1.2pp, so one variable flips the conclusion; (3) agent self-memory (42%) underperforms basic retrieval (47%); (4) on 2 of 6 question types (n = 88), Mem0 matches cloud RAG (72.7% vs. 73.9%, p = 1.0) at 50x the cost, suggesting narrow rather than general gains. We recommend memory evaluations fix embedding models across comparisons, stratify by model family, and report write-path cost before attributing gains to architecture.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
