# Can Agents Truly Forget? Explore Machine Unlearning for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.17659v1
- Published: 2026-10-13
- Updated: 2026-10-13
- Authors: Junkai Lin, Ge Xu, Zheng Xu, Junkai Chen, Xiangyuan Lan
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.17659v1

## One-Sentence Summary
Large language model (LLM) agents have shown strong capabilities in interactive problem solving, tool use, and long-horizon task execution.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents have shown strong capabilities in interactive problem solving, tool use, and long-horizon task execution.

进一步看，论文的核心做法或实验重点可以概括为：However, they may also acquire sensitive or private knowledge during training and expose it during deployment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM) agents have shown strong capabilities in interactive problem solving, tool use, and long-horizon task execution. However, they may also acquire sensitive or private knowledge during training and expose it during deployment. Retraining a model from scratch to remove such knowledge is prohibitively costly, making machine unlearning a more practical approach. Machine unlearning aims to remove targeted undesirable knowledge from trained models without retraining from scratch while preserving general utility. When language models are deployed as agents, parameter-level unlearning becomes insufficient: forgotten information may still persist in memory artifacts or be reacquired via tool calls. In this paper, we formulate the problem of agent unlearning as removing private information from an LLM-based agent across three information channels: parametric knowledge, persistent memory, and tool-call acquisition. To study this problem, we introduce we introduce Agent Unlearning Benchmark (AUBench), a controlled benchmark that extends the fictitious-author setting of TOFU into an agent environment with persistent memory, an offline web snapshot, tool-accessible documents, and provenance-tracked interaction trajectories. By evaluating existing parameter-level and memory-level unlearning methods in this setting, AUBench reveals the gap between model-level forgetting and system-level agent unlearning, and provides a foundation for developing unlearning methods that operate across the full lifecycle of LLM agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
