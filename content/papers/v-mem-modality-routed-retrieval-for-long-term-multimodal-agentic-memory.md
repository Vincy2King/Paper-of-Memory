# V-Mem: Modality-Routed Retrieval for Long-Term Multimodal Agentic Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01543v1
- Published: 2026-08-02
- Updated: 2026-08-02
- Authors: Dingyi Kang, Dongming Jiang, Yi Li, Guanpeng Li, Bingzhe Li
- Tags: agent, conversation, long-term, retrieval
- Categories: cs.AI, cs.CL, cs.CV, cs.IR
- URL: http://arxiv.org/abs/2608.01543v1

## One-Sentence Summary
Interaction between users and LLM agents is increasingly multimodal: conversations interleave text with images, and a later question may target either.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Interaction between users and LLM agents is increasingly multimodal: conversations interleave text with images, and a later question may target either.

进一步看，论文的核心做法或实验重点可以概括为：Yet most agent memories are designed around text, and even the few that support multimodal conversations still fail on vision-related questions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.CL, cs.CV, cs.IR

## Abstract Snapshot
Interaction between users and LLM agents is increasingly multimodal: conversations interleave text with images, and a later question may target either. Yet most agent memories are designed around text, and even the few that support multimodal conversations still fail on vision-related questions. We trace this failure to an assumption behind the similarity search they rely on: in the index space, a query lies close to the relevant evidence that answers it. In multimodal settings, two gaps break it. By the modality gap, a query lies closer to memory content of its own modality than to evidence in another, even in a trained joint embedding space. By the similarity-relevance gap, the content most similar to a query is often not the evidence that answers it, most acutely when a query carries both text and image and its evidence resembles neither part alone. We present V-Mem, a multimodal agentic memory system that routes retrieval by the modality of the query and that of the target evidence, both recognized from the query alone. To cross the modality gap, V-Mem organizes the conversation into rounds and returns the target-modality content from the same round as the match, without comparing across modalities. To close the similarity-relevance gap, it searches with an LLM-generated anchor that sits closer to the relevant evidence than the query does: a hypothetical caption for a text-only query seeking an image, and an enriched search anchor, the query text plus relevant keywords extracted from the query image, when the evidence is reachable only by combining the two. On Mem-Gallery, V-Mem reaches an LLM-judge score of 0.82 versus 0.56 for the second best, with the largest margin on questions carrying an image (0.87, no baseline above 0.47); on LoCoMo it scores 0.69 versus 0.58.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
