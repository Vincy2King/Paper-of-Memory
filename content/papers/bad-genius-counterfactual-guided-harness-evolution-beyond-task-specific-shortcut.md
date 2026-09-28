# Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.18366v3
- Published: 2026-09-16
- Updated: 2026-09-24
- Authors: Guojun Zhu, Xunheng Huang, Peng Yin, Jiahui Xie, Sanguo Zhang, Doudou Zhou
- Tags: agent, benchmark, retrieval
- Categories: cs.AI, cs.LG, stat.ML
- URL: http://arxiv.org/abs/2609.18366v3

## One-Sentence Summary
Reliable agent evaluation is complicated by automatic harness optimization, which repeatedly uses a released benchmark $B_{\mathrm{rel}}$ to guide a Proposer that edits prompts,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Reliable agent evaluation is complicated by automatic harness optimization, which repeatedly uses a released benchmark $B_{\mathrm{rel}}$ to guide a Proposer that edits prompts, memory, retrieval, tools, and control...

进一步看，论文的核心做法或实验重点可以概括为：Task holdout is commonly used to guard against harness overfitting.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI, cs.LG, stat.ML

## Abstract Snapshot
Reliable agent evaluation is complicated by automatic harness optimization, which repeatedly uses a released benchmark $B_{\mathrm{rel}}$ to guide a Proposer that edits prompts, memory, retrieval, tools, and control code around a fixed foundation model. Task holdout is commonly used to guard against harness overfitting. It varies semantic tasks but leaves the benchmark protocol fixed, so a bad genius Proposer can produce a cheating harness whose improvement over the initial harness on $B_{\mathrm{rel}}$ depends on a benchmark-wide shortcut. We introduce Counterfactual Harness Search and Evolution (CHASE), which casts harness evolution as constraint generation over valid counterfactual benchmarks. After each Proposer update, a Challenger searches for an executable protocol transformation with large gain destruction. A validity firewall checks that task semantics are preserved, while a held-out confirmation set determines whether the counterfactual enters a finite archive. We formalize an ideal shortcut-neutralized benchmark $B_0$ and establish theoretical guarantees linking finite counterfactual archives to $B_0$ and characterizing sequential Challenger search. We evaluate CHASE on Syn-Ledger and OfficeQA, where CHASE retains strong released-benchmark gains while substantially reducing gain destruction under valid protocol transformations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
