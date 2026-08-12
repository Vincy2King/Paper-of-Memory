# On Understanding, Identifying, and Mitigating Vulnerabilities in Agentic Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.10530v1
- Published: 2026-08-11
- Updated: 2026-08-11
- Authors: Md Jafrin Hossain, Mohammad Arif Hossain, Nirwan Ansari
- Tags: agent, conversation
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2608.10530v1

## One-Sentence Summary
Large Language Models (LLMs) have undergone a shift from stateless conversational interfaces to autonomous agents capable of multi-step planning, tool invocation, code...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large Language Models (LLMs) have undergone a shift from stateless conversational interfaces to autonomous agents capable of multi-step planning, tool invocation, code execution, and maintaining persistent memory.

进一步看，论文的核心做法或实验重点可以概括为：When these agents operate with real-world privileges---calling APIs, modifying files, and querying databases---a compromised reasoning step can trigger unauthorized data access, irreversible state changes, or...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Large Language Models (LLMs) have undergone a shift from stateless conversational interfaces to autonomous agents capable of multi-step planning, tool invocation, code execution, and maintaining persistent memory. When these agents operate with real-world privileges---calling APIs, modifying files, and querying databases---a compromised reasoning step can trigger unauthorized data access, irreversible state changes, or cascading failures, yet the security research community has not kept pace. To quantify the state of the field, we conducted a systematic literature review under PRISMA 2020 guidelines across six databases, screening 743 records and retaining 85 papers (2023--2025) on agentic LLM security. Attack research outpaces defense work by 3.9:1. Perception-layer vulnerabilities (prompt injection, jailbreaking, adversarial perturbations) dominate, accounting for 66\% of papers, while action-layer vulnerabilities (tool misuse, code injection, sandbox escape) appear in only 4.7\%, misaligned with real-world risk. Code execution security accounts for 3.5\%, and tool-augmented agents 12\%. We contribute a four-layer taxonomy mapping 13 vulnerability types across perception, brain, action, and interaction layers, and identify seven open problems centered on containment. Agentic LLM insecurity stems from architectural coupling, where weak isolation allows vulnerabilities to propagate across layers.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
