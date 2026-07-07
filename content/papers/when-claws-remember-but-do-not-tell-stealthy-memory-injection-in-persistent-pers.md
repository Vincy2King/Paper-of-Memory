# When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.05189v1
- Published: 2026-07-06
- Updated: 2026-07-06
- Authors: Yechao Zhang, Shiqian Zhao, Jiawen Zhang, Jie Zhang, Gelei Deng, Xiaogeng Liu, Chaowei Xiao, Tianwei Zhang
- Tags: agent, benchmark, conversation, long-term
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2607.05189v1

## One-Sentence Summary
Persistent personal agents combine long-term memory with access to users' external environments, enabling personalized foreground assistance and proactive background execution.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent personal agents combine long-term memory with access to users' external environments, enabling personalized foreground assistance and proactive background execution.

进一步看，论文的核心做法或实验重点可以概括为：This integration also creates a new path to compromise: untrusted external content can be silently written into persistent memory and later reused as trusted state.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term
- 检索关键词命中：long-term memory, persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Persistent personal agents combine long-term memory with access to users' external environments, enabling personalized foreground assistance and proactive background execution. This integration also creates a new path to compromise: untrusted external content can be silently written into persistent memory and later reused as trusted state. We study this threat as stealth memory injection, in which a remote black-box adversary delivers a single email payload that must induce the agent to write poisoned memory, stay hidden in the agent's response to the user, and affect future behavior. We introduce WhisperBench, a 108-case benchmark spanning five risk categories and both fact and preference poisoning. Built on a real IMAP/SMTP workflow and an authentic email agent skill, it enables full-cycle evaluation of stealth memory injection attacks. To enable this black-box attack under single-email delivery and without runtime feedback, we propose MemGhost, a one-shot payload generation framework. MemGhost uses an environment proxy to emulate persistent-agent execution and an objective proxy to convert memory adoption and conversational stealth into dense rubric-based rewards, then trains the attacker policy with supervised fine-tuning and reinforcement learning. Across 56 held-out test cases, MemGhost achieves 87.5% end-to-end success on OpenClaw with GPT-5.4 and 71.4% on Claude Code SDK with Sonnet 4.6. It also transfers across personal-agent architectures (NanoClaw and Hermes Agent) and memory backends (filesystem and vector-based Mem0), and remains effective against input-level, model-level, and system-level defenses. These results suggest that persistent memory can turn ordinary external processing into a practical pathway for long-term agent compromise.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
