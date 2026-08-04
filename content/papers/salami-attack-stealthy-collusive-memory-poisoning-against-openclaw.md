# Salami Attack: Stealthy Collusive Memory Poisoning against OpenClaw

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01637v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Zheng Lin, Yuzhe Huang, Zhenxing Niu, Xianmin Ye, Haichang Gao
- Tags: agent, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.01637v1

## One-Sentence Summary
Long-term memory enables LLM agents to retain useful information across sessions, but also creates an attack surface through which adversaries may poison an agent's persistent...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables LLM agents to retain useful information across sessions, but also creates an attack surface through which adversaries may poison an agent's persistent memory to steer its behavior.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory poisoning attacks mainly rely on individually malicious records, overlooking a compositional threat: multiple benign-looking memories may jointly induce unsafe behavior.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：long-term memory, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory enables LLM agents to retain useful information across sessions, but also creates an attack surface through which adversaries may poison an agent's persistent memory to steer its behavior. Existing memory poisoning attacks mainly rely on individually malicious records, overlooking a compositional threat: multiple benign-looking memories may jointly induce unsafe behavior. In this paper, we introduce MemCollusion, an automated red-teaming framework for constructing collusive memory poisoning attacks. MemCollusion applies salami tactics---a strategy that slices an adversarial objective into small, individually innocuous pieces---to generate memory fragments that are individually benign looking but collectively harmful. It constructs memory coalitions using four design constraints, five theory-informed strategies, and a fine-tuned generator. To assess collusive memory poisoning in a realistic cross-session setting, we develop MoltLab, a controlled research reproduction of Moltbook, in which crafted platform content must first be observed and distilled into persistent memory before influencing the agent's behavior in a separate session. We evaluate MemCollusion on OpenClaw using two backbone models across 48 scenarios. Under the strongest memory-saving setting, MemCollusion achieves an average Memory Save Rate of 81.3% and an Attack Success Rate of 75.0%, and remains effective under both benign memory dilution and memory-level defenses.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
