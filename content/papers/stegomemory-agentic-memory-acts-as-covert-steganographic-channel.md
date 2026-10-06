# StegoMemory: Agentic Memory Acts as Covert Steganographic Channel

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.04589v1
- Published: 2026-10-03
- Updated: 2026-10-03
- Authors: Snehasis Mukhopadhyay, Arun Nair
- Tags: agent, retrieval
- Categories: cs.CR, cs.CL
- URL: http://arxiv.org/abs/2610.04589v1

## One-Sentence Summary
Is agentic memory robust against stealthy steganographic attacks?

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Is agentic memory robust against stealthy steganographic attacks?

进一步看，论文的核心做法或实验重点可以概括为：We carry out a large-scale red-teaming exercise to test whether agents can encode attacker-controlled strings in one session and recover them in another without triggering safety oversight.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.CL

## Abstract Snapshot
Is agentic memory robust against stealthy steganographic attacks? We carry out a large-scale red-teaming exercise to test whether agents can encode attacker-controlled strings in one session and recover them in another without triggering safety oversight. Following SHADE-Arena-style tasks, we embed malicious side tasks to encode secret strings using steganography within otherwise benign tasks and evaluate them using independent task-completion and safety oversight. We test 14,000 attack trials spanning 91 model-attack configurations, 13 models, and 7 steganographic schemes: Acrostic, Mesostic, Telestich, Word-choice, Capitalization, Position-based, and Homoglyph. 41.2% of trials successfully encode the target payload in the generated response, while 29.8% survive the memory-write step with the encoding intact. Overall, 25.4% of trials yield a recoverable payload at retrieval, and 20.1% achieve exact-match recovery, including synthetic API keys and cryptographic material never exposed to the receiver. Among the exact-match transmissions, 71.4% also pass primary task-completion scoring and are independently judged safe by the oversight model, corresponding to 14.4% of all trials in which a successful covert transmission would appear to be an ordinary, benign interaction under task-level evaluation. Our results demonstrate that agentic memory can function as a persistent cross-session covert channel. The results further show that the principal bottleneck occurs at memory persistence rather than retrieval: once a steganographic payload survives the memory-write stage, a substantial fraction remains recoverable. We therefore argue that memory integrity, information-flow control, and covert-channel detection should be explicit security requirements for agentic systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
