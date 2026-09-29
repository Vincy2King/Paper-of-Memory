# NLPG: Natural-Language Policy Gradients for Self-Evolving Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.33379v1
- Published: 2026-09-27
- Updated: 2026-09-27
- Authors: Xu Liu, WenZhang Wei, Jun Cao, Dehua Peng, Huan Chen, Zhipeng Gui, Huayi Wu
- Tags: agent, benchmark, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2609.33379v1

## One-Sentence Summary
Large language model agents increasingly rely on compound programs for retrieval, tool use, reasoning, and verification, yet their failures often arise from local procedural...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model agents increasingly rely on compound programs for retrieval, tool use, reasoning, and verification, yet their failures often arise from local procedural decisions.

进一步看，论文的核心做法或实验重点可以概括为：Existing reinforcement-learning and prompt-optimization approaches typically rely on scalar rewards or repeatedly modify entire prompts, making it difficult to capture and reuse procedural improvements while...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory reasoning
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Large language model agents increasingly rely on compound programs for retrieval, tool use, reasoning, and verification, yet their failures often arise from local procedural decisions. Existing reinforcement-learning and prompt-optimization approaches typically rely on scalar rewards or repeatedly modify entire prompts, making it difficult to capture and reuse procedural improvements while preserving a frozen agent. To address this problem, We propose Natural-Language Policy Gradients (NLPG), an external policy-memory method for improving a fixed agent without changing its model parameters or program structure. NLPG diagnoses execution traces, propagates downstream feedback backward through the module graph, and converts recurring failures into route-local natural-language corrections that are aggregated into bounded policy updates for subsequent executions. Across six benchmarks covering memory, reasoning, instruction following, and evidence verification, NLPG also outperforms the strongest listed baseline for each benchmark by 8.71 percentage points on average. These results provide evidence that evaluated procedural experience can be transformed into local and interpretable policy updates, enabling continual improvement of frozen agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
