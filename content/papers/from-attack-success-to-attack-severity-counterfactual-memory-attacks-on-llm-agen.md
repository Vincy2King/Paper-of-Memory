# From Attack Success to Attack Severity: Counterfactual Memory Attacks on LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.34132v1
- Published: 2026-09-28
- Updated: 2026-09-28
- Authors: Mingxi Zou, Langzhang Liang, Zhuo Wang, Yiyang Zhao, Lizhen Qu, Zenglin Xu
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.34132v1

## One-Sentence Summary
As LLM agents increasingly rely on persistent memory for long-horizon and personalized behavior, they can retain and reuse information across interactions, but this also creates...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As LLM agents increasingly rely on persistent memory for long-horizon and personalized behavior, they can retain and reuse information across interactions, but this also creates a lasting channel through which...

进一步看，论文的核心做法或实验重点可以概括为：Persistent-memory attacks are typically evaluated by whether they succeed, yet successful attacks can leave persistent states with substantially different downstream consequences.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
As LLM agents increasingly rely on persistent memory for long-horizon and personalized behavior, they can retain and reuse information across interactions, but this also creates a lasting channel through which malicious memory writes can influence future behavior. Persistent-memory attacks are typically evaluated by whether they succeed, yet successful attacks can leave persistent states with substantially different downstream consequences. We study this severity as a distinct attack-design objective and formalize it with counterfactual memory regret (CMR), the paired increase in expected downstream loss relative to clean memory. We introduce MemHarm, which predeclares a finite class of sparse, grounded semantic edits, evaluates candidates through the normal agent memory interface using offline paired-loss feedback, and certifies resolved selections within that class. Compared with attack-success optimization, CMR-guided selection produces substantially larger downstream loss while retaining most of the success-rate gain. Across two agent benchmarks and diverse memory designs, MemHarm attains the highest CMR point estimates among the evaluated general attacks on identical support. Factor-removal interventions link this harm to the selected semantic factor, and native-agent deployments verify the write-to-fresh-process attack path.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
