# Reproducible Social Structure Emerges From Free-Form Interaction Among LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.31543v1
- Published: 2026-11-23
- Updated: 2026-11-23
- Authors: Tom Alisch, Sonia Murthy, Robert Hawkins, Felix Sosa, Core Francisco Park
- Tags: agent
- Categories: cs.MA, cs.AI
- URL: http://arxiv.org/abs/2611.31543v1

## One-Sentence Summary
Multi-agent LLM simulations are increasingly used as models of social systems, but most published findings are anecdotal, i.e., drawn from a single run.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-agent LLM simulations are increasingly used as models of social systems, but most published findings are anecdotal, i.e., drawn from a single run.

进一步看，论文的核心做法或实验重点可以概括为：It is therefore unclear which observed phenomena are robust findings of the simulated system itself, and which were random events in one particular run.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.MA, cs.AI

## Abstract Snapshot
Multi-agent LLM simulations are increasingly used as models of social systems, but most published findings are anecdotal, i.e., drawn from a single run. It is therefore unclear which observed phenomena are robust findings of the simulated system itself, and which were random events in one particular run. Here, we introduce a repeatable, goal-free, proactive multi-agent framework in which fifty persona-conditioned agents with persistent memory choose whether, with whom, and how to communicate across three social platforms. The framework supports non-perturbative measurements across temporal snapshots and repetitions. Running the same world ten times from identical initial conditions for a total of 700 hours, we find that most measured network- and agent-level parameters are stable across repetitions. Throughout a run, initially broad communication contracts into sparse sustained dyads in all ten worlds. Importantly, we find that many identical dyads re-form across worlds significantly more often than expected by chance or from agent-specific sociability alone. Static personality similarity largely fails to predict these dyads. Instead, alignment and extremity in the emotions and traits expressed during first contact predict whether a pair later forms a sustained dyad. Additionally, individual agents' emotion and trait expression in their chain-of-thought predicts their future behavior. Finally, swapping either persona prompts or accumulated memories between agents causes recipients to exhibit behavior more similar to donors. Both kinds of transplant move the recipients about 60% of the way toward its donor personality, and state-transplanted agents start behaving similar to their donor agent from their next turn on. Overall, we show that repeated worlds enable robust, statistically-grounded conclusions about emergent within-configuration behavior in agent societies.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
