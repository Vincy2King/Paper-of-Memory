# Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational Interaction

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.29960v1
- Published: 2026-05-28
- Updated: 2026-05-28
- Authors: Hongtao Wang, Se Yang, Yu Chen, Puzhuo Liu
- Tags: agent, conversation, long-term
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2605.29960v1

## One-Sentence Summary
Large language model (LLM) agents increasingly leverage long term memory to support persistent and autonomous task execution.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents increasingly leverage long term memory to support persistent and autonomous task execution.

进一步看，论文的核心做法或实验重点可以概括为：However, this capability also introduces a new attack surface: memory poisoning, where adversaries can inject malicious information to influence future behavior.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Large language model (LLM) agents increasingly leverage long term memory to support persistent and autonomous task execution. However, this capability also introduces a new attack surface: memory poisoning, where adversaries can inject malicious information to influence future behavior. Existing memory poisoning attacks often assume that injected content can be stored directly in memory, overlooking the selective extraction and rewriting stages in modern memory pipelines. This makes prior methods ineffective under realistic settings. In this paper, we propose MemPoison, a novel memory poisoning attack that bypasses selective memory mechanisms in LLM agents, where an attacker can inject triggerable backdoors into the agent's long-term memory through dialogue interactions, thereby misleading its subsequent responses. MemPoison introduces three key components: (i) a semantic relational bridge that binds the trigger and payload into a coherent statement to ensure they are extracted into memory together; (ii) entity masquerading that optimizes triggers to mimic named entities, resisting rewriting; and (iii) joint embedding optimization that shapes trigger-injected texts into a tight cluster in the embedding space while maintaining isolation from benign embeddings for stealth. Evaluations across different agent domains and memory mechanisms show MemPoison achieves attack success rates up to 0.95, outperforming existing baselines. Mechanistic analysis indicates that the attack exploits embedding-space anisotropy and shifts attention patterns, highlighting core vulnerabilities in selective memory systems. We evaluate multiple defense strategies and demonstrate their fundamental limitations in mitigating the attack.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
