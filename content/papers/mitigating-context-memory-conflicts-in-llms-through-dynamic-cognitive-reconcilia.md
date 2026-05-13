# Mitigating Context-Memory Conflicts in LLMs through Dynamic Cognitive Reconciliation Decoding

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.12185v1
- Published: 2026-05-12
- Updated: 2026-05-12
- Authors: Yigeng Zhou, Wu Li, Yifan Lu, Yequan Wang, Xuebo Liu, Wenya Wang, Jun Yu, Min Zhang, Jing Li
- Tags: benchmark, context
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.12185v1

## One-Sentence Summary
Large language models accumulate extensive parametric knowledge through pre-training.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models accumulate extensive parametric knowledge through pre-training.

进一步看，论文的核心做法或实验重点可以概括为：However, knowledge conflicts occur when outdated or incorrect parametric knowledge conflicts with external knowledge in the context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, context
- 检索关键词命中：context memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Large language models accumulate extensive parametric knowledge through pre-training. However, knowledge conflicts occur when outdated or incorrect parametric knowledge conflicts with external knowledge in the context. Existing methods address knowledge conflicts through contrastive decoding, but in conflict-free scenarios, static approaches disrupt output distribution. Other dynamic decoding methods attempt to measure the degree of conflict but still struggle with complex real-world situations. In this paper, we propose a two-stage decoding method called Dynamic Cognitive Reconciliation Decoding (DCRD), to predict and mitigate context-memory conflicts. DCRD first analyzes the attention map to assess context fidelity and predict potential conflicts. Based on this prediction, the input is directed to one of two decoding paths: (1) greedy decoding, or (2) context fidelity-based dynamic decoding. This design enables DCRD to handle conflicts efficiently while maintaining high accuracy and decoding efficiency in conflict-free cases. Additionally, to simulate scenarios with frequent knowledge updates, we constructed ConflictKG, a knowledge conflict QA benchmark. Experiments on four LLMs across six QA datasets show that DCRD outperforms all baselines, achieving state-of-the-art performance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
