# Leto: Utility-Centric Agent Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.33005v1
- Published: 2026-11-24
- Updated: 2026-11-24
- Authors: Shuguang Chen, Salman Paracha
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2611.33005v1

## One-Sentence Summary
Large language model (LLM) agents rely on external memory to retain and reuse information across interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM) agents rely on external memory to retain and reuse information across interactions.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory systems treat memory as a record of the past and evaluate it by fidelity to the conversation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language model (LLM) agents rely on external memory to retain and reuse information across interactions. Existing memory systems treat memory as a record of the past and evaluate it by fidelity to the conversation. However, the value of memory lies in whether it improves the agent's response. A memory system decides what to memorize and what to serve before that response exists, and fidelity checks neither decision against it. Faithful memory can therefore fail to improve the response. We instead view memory as a prediction problem and present \textbf{\emph{\leto{}}}, a memory system for LLM agents that focuses on the utility of memory to the future rather than on its fidelity to the past. Because future requests are unknown, \emph{\leto{}} preserves access to conversation details through memory indexing, allowing information to remain available through its sources. When a request arrives, memory replay draws on this index to anticipate and supply the context the agent needs beyond what the request explicitly states. The utility of the served context remains uncertain until the response is generated, motivating a utility loop that uses response outcomes to refine future memory selection. We evaluate our system against six memory systems on five benchmarks across three scenarios. In personalization, it outperforms the strongest compared memory system by 16.3 percentage points in accuracy on PrefEval and by 3.1 points in task completion on PERMA. For long-horizon tasks, it achieves the best overall performance on MemoryArena averaged over five environments with a gain that increases with the chain depth. In long-context understanding, it is on par with retrieval over the raw history while serving fewer context tokens.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
