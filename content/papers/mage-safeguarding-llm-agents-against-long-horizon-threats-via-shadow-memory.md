# MAGE: Safeguarding LLM Agents against Long-Horizon Threats via Shadow Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.03228v1
- Published: 2026-05-04
- Updated: 2026-05-04
- Authors: Yuhui Wang, Tanqiu Jiang, Jiacheng Liang, Charles Fleming, Ting Wang
- Tags: agent, context
- Categories: cs.CR, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2605.03228v1

## One-Sentence Summary
As large language model (LLM)-powered agents are increasingly deployed to perform complex, real-world tasks, they face a growing class of attacks that exploit extended user-...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As large language model (LLM)-powered agents are increasingly deployed to perform complex, real-world tasks, they face a growing class of attacks that exploit extended user-agent-environment interactions to pursue...

进一步看，论文的核心做法或实验重点可以概括为：Such long-horizon threats pose significant risks to the safe deployment of LLM agents in critical domains.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.AI, cs.CL

## Abstract Snapshot
As large language model (LLM)-powered agents are increasingly deployed to perform complex, real-world tasks, they face a growing class of attacks that exploit extended user-agent-environment interactions to pursue malicious objectives improbable in single-turn settings. Such long-horizon threats pose significant risks to the safe deployment of LLM agents in critical domains. In this paper, we present MAGE (Memory As Guardrail Enforcement), a novel defensive framework designed to counter a wide range of long-horizon threats. Inspired by the "shadow stack" abstraction in systems security, MAGE maintains a dedicated, safety-focused agentic memory that distills and retains safety-critical context across the agent's full execution trajectory, leveraging this shadow memory to proactively assess the risk of pending actions prior to their execution. Extensive evaluation demonstrates that MAGE substantially outperforms existing defenses across diverse long-horizon threats in detection accuracy, achieves early-stage detection for the majority of attacks, and introduces only negligible overhead to agent utility. To our best knowledge, MAGE represents the first framework to detect and mitigate long-horizon threats using an agentic memory approach, establishing a new paradigm for this critical challenge and opening promising directions for future research.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
