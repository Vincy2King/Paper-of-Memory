# Retrieved but Not Delivered: Multimodal Memory Delivery for Long-Term Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32590v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Yuhang Jiang, Qingwei Liao, Kaize Yin, Xingling Liu, Luca Cuomo, Silvio Bacci
- Tags: agent, benchmark, context, long-term, retrieval
- Categories: cs.CV, cs.AI, cs.CL, cs.IR
- URL: http://arxiv.org/abs/2609.32590v1

## One-Sentence Summary
Work on memory for multimodal agents optimizes what is written, updated and retrieved.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Work on memory for multimodal agents optimizes what is written, updated and retrieved.

进一步看，论文的核心做法或实验重点可以概括为：Between retrieval and the answer, however, is a stage that multimodal memory evaluations do not isolate: what of the retrieved memory reaches the model, and in what form.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CV, cs.AI, cs.CL, cs.IR

## Abstract Snapshot
Work on memory for multimodal agents optimizes what is written, updated and retrieved. Between retrieval and the answer, however, is a stage that multimodal memory evaluations do not isolate: what of the retrieved memory reaches the model, and in what form. We call it delivery, and a controlled decomposition on MemLens locates the remaining room there. With the retrieved evidence set exactly fixed, delivering the original pixels instead of withholding them raises accuracy by 13.87 points on an 8B backbone, whereas making retrieval perfect on those same messages improves it by 2.31. Delivery is the larger term on all three MemLens backbones and grows with backbone strength; retrieval grows too, without closing the gap. We propose DeliverMem, an instantiation of delivery as three decisions: keep the original modality, give each item a readable identity, and state when it was seen, with a retrieval-side adapter for the one property delivery cannot supply. Each is measured against a delivery-matched control that alters only its own variable. DeliverMem leads the strongest published memory agent on MemLens at all four context lengths, and beats DMV-Bench's own strongest method at every setting on both backbones. On MemLens it does this on a tenth to a seventieth of the input. Each decision helps only where the question lacks what it supplies, and is null elsewhere. A single fixed configuration nonetheless leads both benchmarks, without training any component or modifying the stored records. Project page: https://avalon-s.github.io/DeliverMem/

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
