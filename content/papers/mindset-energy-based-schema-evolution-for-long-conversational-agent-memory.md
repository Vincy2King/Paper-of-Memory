# MINDSET: Energy-based Schema Evolution for Long Conversational Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.08586v1
- Published: 2026-10-06
- Updated: 2026-10-06
- Authors: Sujato Dutta, Sreekruthy Tummala, Shashank Vanga, Ayushmi Pavani
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.08586v1

## One-Sentence Summary
Long conversational agents have become essential in our daily lives.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long conversational agents have become essential in our daily lives.

进一步看，论文的核心做法或实验重点可以概括为：They must remember what was said long back in order to help us efficiently complete a task without needing the user to repeat instructions and context repeatedly.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long conversational agents have become essential in our daily lives. They must remember what was said long back in order to help us efficiently complete a task without needing the user to repeat instructions and context repeatedly. However, the main issue is that instructions and context change over time and so the agents must be able to adapt accordingly. A useful memory system should preserve both current and historical states, distinguish stale information from active knowledge, retrieve evidence appropriate to the query and avoid repeatedly invoking a large language model to rewrite prior interactions. We introduce MINDSET, a memory controller that stores a conversation as immutable episodes and organizes them into versioned schemas through minimum-energy state transitions. Each incoming episode may reinforce, supersede, split or create a schema. The transition decision balances representation distortion, contradiction, historical damage, fragmentation and internal inconsistency, while hysteresis prevents isolated contradictions from prematurely rewriting stable memory. We evaluate MINDSET against 5 memory systems on a reproducible sample of 850 questions (700 LoCoMo + 150 MemoryAgentBench). MINDSET obtains the highest observed LoCoMo answer F1 while significantly improving retrieval ranking (Recall@8, MRR and nDCG@8) over the second best method LightMem (p<0.01 after Holm correction). It obtains the highest observed scores on MemoryAgentBench although the relative difference is low. Ablations identify controlled fragmentation and schema-aware assignment as the largest contributors to answer quality. Additionally, a 700-question cross-model evaluation with GLM-4.7 and Gemma-4-31B supported model independence. These results show that long-term memory can be better handled as constrained state management rather than continual summarization.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
