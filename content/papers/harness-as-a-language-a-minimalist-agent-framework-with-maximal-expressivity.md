# Harness as a Language: A Minimalist Agent Framework With Maximal Expressivity

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.26891v2
- Published: 2026-09-22
- Updated: 2026-09-30
- Authors: Zhening Li, Joshua Liu, Mateja Vukelic, Nicole Shen, Supriya Lall, Amitayush Thakur, Alex Zhang, Omar Khattab, Jonathan Light, Armando Solar-Lezama
- Tags: agent, context, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.26891v2

## One-Sentence Summary
Modern language-model agents are built around the agent loop: the LLM is placed in an environment exposing a set of tools, and the LLM has full control over the workflow by...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Modern language-model agents are built around the agent loop: the LLM is placed in an environment exposing a set of tools, and the LLM has full control over the workflow by alternating between tool calls and observing...

进一步看，论文的核心做法或实验重点可以概括为：However, certain capabilities such as long-term memory and self-improvement currently require specialized systems beyond the agent loop itself.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Modern language-model agents are built around the agent loop: the LLM is placed in an environment exposing a set of tools, and the LLM has full control over the workflow by alternating between tool calls and observing their output. However, certain capabilities such as long-term memory and self-improvement currently require specialized systems beyond the agent loop itself. We built an LLM agent framework, JAZ, to explore the extent to which a minimal harness that is little more than the agent loop itself can accomplish tasks these specialized systems are built for. JAZ exposes a single LLM-based primitive `invoke` and provides a set of built-in hooks that allow the programmer to apply constraints and perform monitoring. Generalizing existing code-mode agent loops, `invoke` is the simplest loop that satisfies two defining properties: (1) the LLM can write arbitrary executable code that can include recursive `invoke`; (2) everything visible to the LLM - all inputs to `invoke` as well as its interaction history with the code environment - are variables in the code environment. We motivate our design from first principles, viewing `invoke` as a language primitive representing a function whose implementation is provided at runtime by an LLM every time it is called. To validate the design of our core `invoke` primitive, we evaluate `invoke` - with only prompting, no manually designed tools, harness, or external systems (e.g., memory or the file system) - on workflows traditionally implemented through specialized harnesses. On long-horizon workflows requiring recall far beyond the context window, JAZ `invoke` outperforms Letta (MemGPT) by 8% at half its cost on the recall-heavy portion of StuLife. On continual self-improvement, JAZ `invoke` outperforms ACE by 4% at a lower cost on AppWorld.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
