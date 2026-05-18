# Hidden in Memory: Sleeper Memory Poisoning in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.15338v1
- Published: 2026-05-14
- Updated: 2026-05-14
- Authors: Sidharth Pulipaka, Stanislau Hlebik, Leonidas Raghav, Sahar Abdelnabi, Vyas Raina, Ivaxi Sheth, Mario Fritz
- Tags: agent, context, conversation, long-term, retrieval
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2605.15338v1

## One-Sentence Summary
Large language models are increasingly augmented with persistent memory, allowing assistants to store user-specific information across sessions for personalization and continuity.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models are increasingly augmented with persistent memory, allowing assistants to store user-specific information across sessions for personalization and continuity.

进一步看，论文的核心做法或实验重点可以概括为：This statefulness introduces a new security risk: adversarial content can corrupt what an assistant remembers and thereby influence future interactions.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, long-term, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Large language models are increasingly augmented with persistent memory, allowing assistants to store user-specific information across sessions for personalization and continuity. This statefulness introduces a new security risk: adversarial content can corrupt what an assistant remembers and thereby influence future interactions. We propose and study sleeper memory poisoning, a delayed attack in which an adversary manipulates external context, such as a document, webpage, or repository, to cause the assistant to store a fabricated memory about the user. Unlike conventional prompt injection, the attack can remain dormant and re-emerge across multiple later conversations. We evaluate the full attack pipeline: whether poisoned memories are written, later retrieved, and ultimately used to steer the following conversations. Across stateful LLM assistants, poisoned memories were added up to 99.8% on GPT-5.5 and 95% on Kimi-K2.6. Crucially, among successful retrievals, poisoned memories cause attacker-intended agentic actions in 60-89% of evaluations across models. These results show that persistent memory can act as a long-term attack surface across multiple future conversations.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
