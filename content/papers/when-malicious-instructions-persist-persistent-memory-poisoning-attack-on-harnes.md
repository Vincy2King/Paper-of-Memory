# When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.13889v1
- Published: 2026-09-12
- Updated: 2026-09-12
- Authors: Shuhuai Huang, Jingfeng Zhang, Hong Jia
- Tags: agent
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2609.13889v1

## One-Sentence Summary
Harness design has transformed the development of LLM-based agents by integrating memory, tool use, and runtime control.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Harness design has transformed the development of LLM-based agents by integrating memory, tool use, and runtime control.

进一步看，论文的核心做法或实验重点可以概括为：However, this design also introduces security and privacy risks because malicious instructions from external sources may be written into persistent memory and persist across sessions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Harness design has transformed the development of LLM-based agents by integrating memory, tool use, and runtime control. However, this design also introduces security and privacy risks because malicious instructions from external sources may be written into persistent memory and persist across sessions. To study this risk, we propose PMPA, a Persistent Memory Poisoning Attack against harness-based agents. PMPA embeds malicious instructions into benign external sources and induces the victim agent to write them into persistent memory without directly accessing to the agent framework. Once stored, the poisoned memory can be retrieved in later sessions, triggering additional malicious actions and causing privacy leakage. We evaluate PMPA on OpenClaw and Claude Code across different backbone LLMs, input modalities, and trigger scenarios. Across all settings, PMPA achieves average Injection Success Rate (ISR) and Cross-session Attack Success Rate (C-ASR) of 73.7%/ 55.5% on OpenClaw and 66.9%/ 81.7% on Claude Code, while preserving benign task performance on both systems. We further evaluate a targeted prompt-level defense and find that it can reduce memory injection in many settings, but provides limited protection once the persistent memory has been poisoned.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
