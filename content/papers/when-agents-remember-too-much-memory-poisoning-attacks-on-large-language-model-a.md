# When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.06595v1
- Published: 2026-07-06
- Updated: 2026-07-06
- Authors: George Torres, Sharad Shrestha, Satyajayant Misra
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2607.06595v1

## One-Sentence Summary
Personal AI agents powered by large language models can reason and act using available tools to access emails, manage calendars, and push code to remote repositories, all with...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personal AI agents powered by large language models can reason and act using available tools to access emails, manage calendars, and push code to remote repositories, all with minimal oversight.

进一步看，论文的核心做法或实验重点可以概括为：When augmented with long-term memory, an agent can recall specific details relevant to the current task, reducing the need for large context windows.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory retrieval
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Personal AI agents powered by large language models can reason and act using available tools to access emails, manage calendars, and push code to remote repositories, all with minimal oversight. When augmented with long-term memory, an agent can recall specific details relevant to the current task, reducing the need for large context windows. Currently, long-term memory agents tend to fall into two distinct domains: conversational and action-planning agents. Personal assistant agents sit at the convergence of these two domains and handle sensitive information while interacting with untrusted information sources, creating previously unaccounted security vulnerabilities. In this work, we introduce the novel attack vector, GhostWriter, which exploits current memory subsystems in tool-using personal agents to poison their memory store. GhostWriter operates in two phases: injection, where an adversary sends a hidden attack payload to the target agent; and activation, in which the poisoned memory is retrieved. We show that GhostWriter achieves near-universal injection rates of approximately 98% and a high average activation rate of approximately 60% against state-of-the-art agents. This attack is possible due to the lack of security-focused memory governance. In response, we propose Agentic Memory Sentry (AM-Sentry), which leverages two mitigation techniques: a memory-saving policy and a memory-retrieval screen. Our experiments show that AM-Sentry dramatically reduces GhostWriter's success rate while preserving agent utility.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
