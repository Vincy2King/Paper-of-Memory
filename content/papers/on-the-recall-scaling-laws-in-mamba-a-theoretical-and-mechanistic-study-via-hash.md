# On the Recall Scaling Laws in Mamba: A Theoretical and Mechanistic Study via Hashing

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.07681v1
- Published: 2026-09-07
- Updated: 2026-09-07
- Authors: Yuval Koren, Assaf Ben-Kish, Raja Giryes, Lior Wolf, Itamar Zimerman
- Tags: benchmark, context
- Categories: cs.LG, cs.CL
- URL: http://arxiv.org/abs/2609.07681v1

## One-Sentence Summary
Associative Recall (AR) is the cognitive ability to learn and retrieve links between items in memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Associative Recall (AR) is the cognitive ability to learn and retrieve links between items in memory.

进一步看，论文的核心做法或实验重点可以概括为：In NLP, AR is used as a benchmark for evaluating the in-context memory capacity of architectures such as Mamba, and has been found to strongly correlate with language modeling performance.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：context memory
- 来源分类信息：cs.LG, cs.CL

## Abstract Snapshot
Associative Recall (AR) is the cognitive ability to learn and retrieve links between items in memory. In NLP, AR is used as a benchmark for evaluating the in-context memory capacity of architectures such as Mamba, and has been found to strongly correlate with language modeling performance. This paper explores AR from the perspective of mechanistic interpretability, aiming to reverse-engineer the exact internal algorithm used by Mamba to perform recall. Our key insight is that Mamba performs recall by implicitly learning linear hash functions, and we identify the low-level circuit that enables this behavior. Building on these findings and inspired by theoretical tools in similarity-preserving hashing, such as the Johnson-Lindenstrauss lemma, we develop a theoretical framework for analyzing AR, which we term Recall Scaling Laws. Given the vocabulary size and the number of facts in context, this framework allows us to (1) predict the embedding and state dimensions required for Mamba to achieve perfect recall, (2) predict recall success probability given the model dimensions, and (3) analyze multi-layer models and multi-head SSM patterns. Empirical results show that our theoretical findings are accurate and predictive, offering insights into how AR capacity scales with vocabulary, state, embedding size, and architecture.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
