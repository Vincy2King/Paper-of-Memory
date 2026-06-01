# Chain-of-Thought and Compressed Looped Transformers: A Memory-Budget Separation

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.30757v1
- Published: 2026-05-29
- Updated: 2026-05-29
- Authors: Haozhou Zhang
- Tags: context
- Categories: cs.LG
- URL: http://arxiv.org/abs/2605.30757v1

## One-Sentence Summary
Chain-of-thought prompting and looped Transformers both give a fixed model more test-time computation, but they differ in what they remember.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Chain-of-thought prompting and looped Transformers both give a fixed model more test-time computation, but they differ in what they remember.

进一步看，论文的核心做法或实验重点可以概括为：Chain-of-thought stores intermediate state in generated tokens that remain in the context, whereas a looped Transformer carries state through recurrent hidden activations.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：working memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Chain-of-thought prompting and looped Transformers both give a fixed model more test-time computation, but they differ in what they remember. Chain-of-thought stores intermediate state in generated tokens that remain in the context, whereas a looped Transformer carries state through recurrent hidden activations. We argue that this persistent mutable memory is a central resource for test-time reasoning. We compare three memory regimes, the compressed latent loop, the full sequence-state loop, and the chain-of-thought scratchpad. Our main result shows that a compressed loop is limited by the size of its recurrent state. Running the loop longer adds computation but does not by itself create a growing scratchpad, so a loop with a small recurrent state remains a small-space reasoner even when run for many steps. Under a standard complexity assumption, such loops cannot decide problems that are P-complete under logspace reductions, whereas polynomial-length chain-of-thought can. The separation is specific to compressed loops, as full sequence-state loops carry state at every input position and live in a memory-rich regime closer to explicit scratchpads. Controlled pointer-chasing and associative-recall sweeps illustrate this memory-budget view, with performance sensitive to whether the persistent-state budget matches the task's working-memory demand.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
