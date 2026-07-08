# Memory in the Loop: In-Process Retrieval as ExtendedWorking Memory for Language Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.05690v1
- Published: 2026-07-06
- Updated: 2026-07-06
- Authors: Yusuf Khan, Carlo Lipizzi
- Tags: agent, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2607.05690v1

## One-Sentence Summary
Language agents run a loop - observe, reason, act - but the memory they reason over sits outside it: a store queried at most once per turn.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Language agents run a loop - observe, reason, act - but the memory they reason over sits outside it: a store queried at most once per turn.

进一步看，论文的核心做法或实验重点可以概括为：We study the regime where memory moves inside the loop, read and written on every step.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：working memory
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Language agents run a loop - observe, reason, act - but the memory they reason over sits outside it: a store queried at most once per turn. We study the regime where memory moves inside the loop, read and written on every step. The obstacle has always been latency: networked stores answer in tens to hundreds of milliseconds, and in-loop retrieval can inflate end-to-end latency by up to 83x when retrieval is expensive. Prior work manages that cost rather than questioning it: serving-layer scheduling hides it, "memory-first" designs ration retrieval to once per turn. We argue latency is a property of where the store lives, not the in-loop pattern: an in-process store answers in ~100us, three orders of magnitude below the network regime, and at that speed the per-step tax collapses. By the extended-mind thesis's parity principle, a store fast enough to be constantly and directly available becomes extended working memory, not a tool the agent merely consults. The premise is causal: holding a fixed per-turn memory-latency budget and varying only the store's answer speed, redundant actions rise monotonically with latency - 0.0 of 12 at in-process speed, 7.2 of 12 at a 110ms cloud round trip (gpt-5-nano, gpt-5-mini; exact permutation p=0.0079). We demonstrate the regime end-to-end: across four GPT-5-class models under a bounded window, recall improves from 0/5 to 3.6-4.8/5 with in-loop memory, store ops at p50 80-165us - though an instructed restate-every-reply baseline also solves it perfectly, at a token cost that grows with the working set. The store never lost a fact in any run (244 of 244 writes kept); every miss traces to the agent's read policy, not the store. Our measurements also relocate the bottleneck: the dominant per-step cost is embedding (~200-400ms over the network); pairing the in-process store with a small local embedder returns the complete operation to a measured ~40us.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
