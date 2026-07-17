# Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.14611v1
- Published: 2026-07-16
- Updated: 2026-07-16
- Authors: Soham Gadgil, David Alexander, Sai Sunku, Franziska Roesner
- Tags: agent
- Categories: cs.CR, cs.AI, cs.MA
- URL: http://arxiv.org/abs/2607.14611v1

## One-Sentence Summary
A growing class of agentic systems maintain persistent state across sessions through memory files, behavioral preferences, and knowledge bases.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：A growing class of agentic systems maintain persistent state across sessions through memory files, behavioral preferences, and knowledge bases.

进一步看，论文的核心做法或实验重点可以概括为：While this makes agents more useful and self-improving, it also creates a new attack surface for prompt injections in which malicious instructions can be embedded within persistent files and influence future behavior.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI, cs.MA

## Abstract Snapshot
A growing class of agentic systems maintain persistent state across sessions through memory files, behavioral preferences, and knowledge bases. While this makes agents more useful and self-improving, it also creates a new attack surface for prompt injections in which malicious instructions can be embedded within persistent files and influence future behavior. In this work, we study prompt injection attacks in memory-based agentic systems using a sandboxed synthetic workspace. We evaluate two agentic systems, Anthropic Claude Code and OpenAI Codex, across four models: Claude Haiku 4.5, Claude Opus 4.7, GPT-5.2, and GPT-5.5. Our results show that although it is difficult to make an agent overwrite its own memory files using untrusted external content, payloads already planted in those files can successfully attack current and future sessions. Attack success and payload persistence vary substantially across systems, models, adversarial goals, and multi-session attack sequences. These findings show that persistent memory changes the threat model for prompt injection and motivate defenses that protect memory updates without removing useful agent adaptation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
