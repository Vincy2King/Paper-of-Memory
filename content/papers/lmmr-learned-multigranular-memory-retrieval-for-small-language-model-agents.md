# LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.22425v1
- Published: 2026-11-17
- Updated: 2026-11-17
- Authors: Pengfeng Song, Yunkai Zhuang, Liye Shi
- Tags: agent, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.22425v1

## One-Sentence Summary
Small language model agents have limited space to read the memory needed for multi-hop questions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Small language model agents have limited space to read the memory needed for multi-hop questions.

进一步看，论文的核心做法或实验重点可以概括为：Relevant facts are often scattered across records whose surrounding text consumes much of that space.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CL

## Abstract Snapshot
Small language model agents have limited space to read the memory needed for multi-hop questions. Relevant facts are often scattered across records whose surrounding text consumes much of that space. We propose LMMR, a learned multigranular memory retrieval method that selects both the next source and how much of it to read. LMMR links paragraphs and sentence fragments to their original sources and pairs views that supply the same missing support during training. Relevant distractors and repeated information provide contrasting examples. At inference, the reranker scores what each candidate adds to an anchor passage, and a selector chooses the evidence within a token budget. On 22,398 official validation questions from HotpotQA, 2WikiMultihopQA, and MuSiQue, a frozen 2B answer model reaches 61.47, 43.26, and 30.58 F1 under a 400-token budget. The gains over query expansion are 3.06, 2.14, and 4.55 points, while memory input decreases by 23.1-26.9%. LMMR also uses 23.5-27.7% fewer input tokens than a coarse retriever trained on the same questions. Against that retriever followed by LLMLingua-2 at comparable input lengths, F1 gains reach 3.99 points and are significant on HotpotQA and 2WikiMultihopQA after Holm correction. All eight small answer models evaluated on HotpotQA improve over query expansion and MMR in both F1 and exact match.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
