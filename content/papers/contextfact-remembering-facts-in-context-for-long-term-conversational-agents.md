# ContextFact: Remembering Facts in Context for Long-Term Conversational Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.29155v1
- Published: 2026-11-22
- Updated: 2026-11-22
- Authors: Jiayu Huang, Yichao Cai, Xinyu Li, Zhen Zhang, Javen Qinfeng Shi
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2611.29155v1

## One-Sentence Summary
Agents built on large language models must maintain continuity across repeated interactions with users.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agents built on large language models must maintain continuity across repeated interactions with users.

进一步看，论文的核心做法或实验重点可以概括为：However, long-term conversations scatter facts across turns and sessions, making it difficult to retrieve the right evidence with enough context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：context memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Agents built on large language models must maintain continuity across repeated interactions with users. However, long-term conversations scatter facts across turns and sessions, making it difficult to retrieve the right evidence with enough context. Memory for such conversations must therefore preserve facts with their context while keeping evidence selectively accessible. We first study how memory construction and retrieval-unit boundaries affect answerability and evidence access. Reading the entire memory bank reveals gaps that cannot be resolved by retrieval selection alone, showing that some context must be preserved during memory construction. Adjacent-turn grouping improves evidence access at matched unique-turn budgets, while wider windows do not consistently help. This motivates keeping fact-specific context local while organizing cross-session evidence separately. We propose ContextFact, which links context-preserving fact memories with source-grounded entity representations. Within sessions, it gathers the context needed to interpret each fact. Across sessions, it aligns recurring referents and revisits the source dialogue to reconstruct coherent entity representations linked to the supporting facts. At query time, ContextFact retrieves fact and entity views, reranks them independently, and uses entity-linked expansion to surface related facts; complete entity representations then provide organized cross-session evidence. With Qwen3.5-27B as the backbone, ContextFact achieves state-of-the-art performance while using only $21\%$ of the evidence tokens consumed by the strongest evaluated baseline, obtaining $86.49\%$ overall judge accuracy on LoCoMo and $91.00\%$ on LongMemEval-S. Controlled ablations support context-preserving fact boundaries and source-grounded entity reconstruction, while entity readout improves multi-hop accuracy beyond adding more facts.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
