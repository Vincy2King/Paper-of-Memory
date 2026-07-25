# The Giant Hippocampus: From Structural Monoculture to a System of Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.19973v1
- Published: 2026-07-22
- Updated: 2026-07-22
- Authors: Jaeho Seol
- Tags: working memory
- Categories: cs.AI, cs.LG, cs.NE, q-bio.NC
- URL: http://arxiv.org/abs/2607.19973v1

## One-Sentence Summary
AI researchers describe state-of-the-art models as one thing repeated at scale: the Transformer, wired identically for text, pixels, or speech.

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI researchers describe state-of-the-art models as one thing repeated at scale: the Transformer, wired identically for text, pixels, or speech.

进一步看，论文的核心做法或实验重点可以概括为：Neuroscientists describe the cortex as a mosaic - dense Layer 4 in visual cortex for spatial encoding, thick Layers 5/6 in motion cortex for temporal integration - different jobs solved by different structures.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.LG, cs.NE, q-bio.NC

## Abstract Snapshot
AI researchers describe state-of-the-art models as one thing repeated at scale: the Transformer, wired identically for text, pixels, or speech. Neuroscientists describe the cortex as a mosaic - dense Layer 4 in visual cortex for spatial encoding, thick Layers 5/6 in motion cortex for temporal integration - different jobs solved by different structures. This paper argues the gap is a structural error, not a stylistic one, and is measurable. A century of cytoarchitecture, from Brodmann to single-cell Patch-seq, shows distinct cognitive functions are implemented by qualitatively different structures, not by rescaling one template. The convolutional neural network is the field's own proof: local receptive fields and hierarchical depth encoded this prior directly, reaching strong image recognition on far less data than later architectures needed. The paper traces how this lesson was discarded: the "Hardware Lottery" made the Transformer the path of least resistance, not the principled choice, and Mixture-of-Experts, often cited as diversity, in fact partitions parameters among identical experts. A functionalist analysis shows the Transformer is best understood as a functional analog of the hippocampal formation, not a general-purpose cortex - the same mistake as treating cortex as one giant Broca's area, except the field has now standardized on a giant hippocampus, applied to tasks it was never built for: audition, executive gating, working memory. The paper closes with an alternative: a Heterogeneous Topological Network, a System of Systems in which distinct modules keep the inductive bias their computation demands and communicate through standardized interfaces. This is a design discipline for AI architects, not cognitive science: specify modularity before training, using structural evidence as a design input rather than reverse-engineering architecture from a trained model's behavior.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
