# OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.18930v1
- Published: 2026-05-18
- Updated: 2026-05-18
- Authors: Kaixiang Wang, Jiong Lou, Zhaojiacheng Zhou, Jie Li
- Tags: agent
- Categories: cs.CR, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2605.18930v1

## One-Sentence Summary
Memory-augmented large language model (LLM) agents use iterative reflection and self-evolution to solve complex tasks, but these mechanisms introduce security risks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory-augmented large language model (LLM) agents use iterative reflection and self-evolution to solve complex tasks, but these mechanisms introduce security risks.

进一步看，论文的核心做法或实验重点可以概括为：Existing agentic memory attacks require privileged access or explicit malicious content, making them detectable by advanced safety filters.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory, memory augmented, memory-augmented
- 来源分类信息：cs.CR, cs.AI, cs.LG

## Abstract Snapshot
Memory-augmented large language model (LLM) agents use iterative reflection and self-evolution to solve complex tasks, but these mechanisms introduce security risks. Existing agentic memory attacks require privileged access or explicit malicious content, making them detectable by advanced safety filters. This leaves a subtler attack surface underexplored: whether adversaries can induce agent to generate experiences that appear locally correct and semantically plausible yet induce harmful generalization during reflection. We find that reflective agents are vulnerable to such clean experiences, especially when paired with severe but plausible hypothetical consequences. Based on this observation, we introduce Obsessive Experience Poisoning (OEP), a low-privilege black-box attack requiring no direct control over the system prompt or memory database. OEP constructs adversarial clean edge-cases that combine locally correct solutions, non-transferable methods, and severe consequences, biasing reflection toward risk-averse rule formation. During memory consolidation, agents may over-trust self-generated reflections and distill localized experiences into high-priority but over-generalized rules, causing downstream failures. Evaluations across three domains show that OEP achieves ASR above 50\% with GPT-4o agents, and outperforms existing attacks under LLM auditing defense.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
