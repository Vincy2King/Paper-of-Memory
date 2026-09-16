# RunningTensor: Generalizing Linear Attention to Higher-Order Recurrent States

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.12814v1
- Published: 2026-09-11
- Updated: 2026-09-11
- Authors: Luca Herranz-Celotti, Vincent Guigue
- Tags: retrieval
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2609.12814v1

## One-Sentence Summary
Linear attention and state-space models provide linear-time sequence modeling, but their recurrent memory remains a second-order tensor (a matrix), limiting the order of...

## Introduction
这篇论文被纳入仓库，是因为它和 `retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Linear attention and state-space models provide linear-time sequence modeling, but their recurrent memory remains a second-order tensor (a matrix), limiting the order of interactions that can be represented in the state.

进一步看，论文的核心做法或实验重点可以概括为：We introduce the RunningTensor, which generalizes this memory to an order-$o$ tensor, updated by a rank-1 outer product and read by contracting against $o-1$ vector queries.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Linear attention and state-space models provide linear-time sequence modeling, but their recurrent memory remains a second-order tensor (a matrix), limiting the order of interactions that can be represented in the state. We introduce the RunningTensor, which generalizes this memory to an order-$o$ tensor, updated by a rank-1 outer product and read by contracting against $o-1$ vector queries. Order $2$ recovers linear attention; we study order $3$ as a proof of concept, retaining both recurrent and parallel forms while remaining linear in sequence length $T$ and improving working memory capacity from $\mathcal{O}(W^2)$ to $\mathcal{O}(W^o)$. On synthetic multi-query associative recall, RunningTensor outperforms linear-attention and SSM baselines. After pretraining, it also improves performance on language-understanding and non-synthetic retrieval tasks, suggesting that higher-order recurrent state can provide useful additional memory capacity beyond matrix-valued state.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
