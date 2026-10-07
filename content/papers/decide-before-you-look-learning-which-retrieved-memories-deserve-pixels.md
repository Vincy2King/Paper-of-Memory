# Decide Before You Look: Learning Which Retrieved Memories Deserve Pixels

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.07984v1
- Published: 2026-10-06
- Updated: 2026-10-06
- Authors: Youxing LI
- Tags: long-term, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2610.07984v1

## One-Sentence Summary
Multimodal assistants answer questions from long-term memories that contain images.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multimodal assistants answer questions from long-term memories that contain images.

进一步看，论文的核心做法或实验重点可以概括为：After retrieval, each retrieved image reaches the answering model either as pixels, at about a thousand visual tokens per image, or as a stored text proxy that often misses the detail the question asks about.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term, retrieval
- 检索关键词命中：long-term memory, retrieval memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Multimodal assistants answer questions from long-term memories that contain images. After retrieval, each retrieved image reaches the answering model either as pixels, at about a thousand visual tokens per image, or as a stored text proxy that often misses the detail the question asks about. We find that the benefit of pixels usually comes from one or two retrieved memories, and that it can be predicted before the answering model runs, without reading any full-resolution image. In PixelTriage, a plug-in placed after retrieval, a small model that does not generate text reads the dialogue, a short note and a thumbnail of each retrieved memory and predicts how much its pixels would add. It is trained on synthetic memory episodes labeled by a frozen 27B model that answers each question with and without each memory's pixels. With a 7B answering model, PixelTriage lies on the accuracy--cost frontier of M$^3$Exam, DMV and MemEye and uses 11--23\% of the visual tokens without a significant loss of accuracy. On DMV it answers 2.9 times faster than opening all images. It outperforms retrieval order and uniform down-sizing at equal budgets and transfers to other memory systems and to a 397B answering model.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
