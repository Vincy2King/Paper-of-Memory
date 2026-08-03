# ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.28678v1
- Published: 2026-07-29
- Updated: 2026-07-29
- Authors: Xinkui Zhao, Enbo Chen, Yifan Zhang, Chang Liu, Guanjie Cheng, Naibo Wang, Yueshen Xu
- Tags: agent, compression, retrieval
- Categories: cs.AI, cs.CV
- URL: http://arxiv.org/abs/2607.28678v1

## One-Sentence Summary
Multimodal agents operating in long-horizon environments must build and continually update multimedia memories to support entity-consistent, temporally grounded reasoning.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multimodal agents operating in long-horizon environments must build and continually update multimedia memories to support entity-consistent, temporally grounded reasoning.

进一步看，论文的核心做法或实验重点可以概括为：However, existing agentic memory approaches often discard fine-grained dentity cues under aggressive compression and segment-wise processing.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.CV

## Abstract Snapshot
Multimodal agents operating in long-horizon environments must build and continually update multimedia memories to support entity-consistent, temporally grounded reasoning. However, existing agentic memory approaches often discard fine-grained dentity cues under aggressive compression and segment-wise processing. They also rely heavily on vector similarity retrieval, which can surface semantically related yet identity-mismatched evidence, leading to entity confusion, error propagation, and hallucinated answers. We propose ViSAGE, a multimodal agentic memory framework that constructs self-correcting, entity-centric memories. Specifically, ViSAGE anchors entity identity via cross-modal binding over long temporal ranges. It then applies bidirectional memory refinement to propagate delayed identity evidence, retroactively unifying historical records and improving future reasoning. We also introduce multi-agent cross-verification to assess retrieved evidence under an identity-evidence alignment onstraint, enabling abstention instead of unsupported answers when evidence is missing. Extensive results demonstrate that ViSAGE consistently outperforms the strongest baseline, achieving 5.9% higher accuracy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
