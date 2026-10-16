# Language Models Share a Readout Bottleneck in Working Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.21176v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Dongyu Gong
- Tags: working memory
- Categories: cs.LG, cs.AI, cs.CL, q-bio.NC
- URL: http://arxiv.org/abs/2610.21176v1

## One-Sentence Summary
Large language models (LLMs) reproduce a human working-memory signature on the N-back task: performance declines as memory load N increases, and errors concentrate on lures,...

## Introduction
这篇论文被纳入仓库，是因为它和 `working memory` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models (LLMs) reproduce a human working-memory signature on the N-back task: performance declines as memory load N increases, and errors concentrate on lures, items that repeat the current stimulus at a...

进一步看，论文的核心做法或实验重点可以概括为：We ask whether this shared behavioral signature reflects a shared mechanism.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：working memory
- 检索关键词命中：working memory
- 来源分类信息：cs.LG, cs.AI, cs.CL, q-bio.NC

## Abstract Snapshot
Large language models (LLMs) reproduce a human working-memory signature on the N-back task: performance declines as memory load N increases, and errors concentrate on lures, items that repeat the current stimulus at a neighboring but incorrect serial position. We ask whether this shared behavioral signature reflects a shared mechanism. The literature offers two candidate accounts. On a precision account, softmax attention cannot concentrate its weight on the item N positions back, so adjacent items are retrieved instead. On an interference account, attention selects the correct item, but the content of competing items corrupts the decision. We dissociate these accounts in 15 pretrained LLMs from three families (70 million to 14 billion parameters) and in minimal transformers trained from scratch. In all three families, the attention heads that carry the task attend to the target on most missed matches. Linear probes decode near-perfectly whether a matching letter occurred at the target or at a lure position, even on trials where the model false-alarms to the lure, although its own decisions barely distinguish the two. Sharpening attention yields negligible gains, whereas suppressing the letter identity of non-target items improves sensitivity (d') in nearly all model-by-load conditions. In larger models the task is spread over more heads, and removing interference helps more. In minimal transformers, precision limits a single attention layer, but a second layer removes this constraint. The working-memory limit of LLMs therefore lies in reading items out under interference rather than in locating them, consistent with interference accounts of human working memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
