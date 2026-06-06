# From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.04329v1
- Published: 2026-06-03
- Updated: 2026-06-03
- Authors: Pritam Dash, Tongyu Ge, Aditi Jain, Tanmay Shah, Zhiwei Shang
- Tags: agent, benchmark, long-term
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2606.04329v1

## One-Sentence Summary
Memory is a core component of AI agents, enabling them to accumulate knowledge across interactions and improve performance.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory is a core component of AI agents, enabling them to accumulate knowledge across interactions and improve performance.

进一步看，论文的核心做法或实验重点可以概括为：However, persistent memory introduces the risk of memory poisoning, where a single adversarial memory write can exert long-term influence over agent behavior.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：persistent memory, retrieval memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Memory is a core component of AI agents, enabling them to accumulate knowledge across interactions and improve performance. However, persistent memory introduces the risk of memory poisoning, where a single adversarial memory write can exert long-term influence over agent behavior. We present a systematic study of memory poisoning in LLM-based agents. We identify four memory write channels and nine structural vulnerabilities in model capabilities, system prompt design, and agent system architecture that make these channels exploitable. Based on these vulnerabilities, we develop a taxonomy of six classes of memory poisoning attacks. Furthermore, we design MPBench -- a benchmark for evaluating memory poisoning attacks, and show that agents designed to write and retrieve memory more aggressively are more exploitable. We also show that existing prompt injection defenses fail to cover memory poisoning attacks. Our findings provide a foundation for understanding and mitigating memory poisoning attacks against AI agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
