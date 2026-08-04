# ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map Points to the Next Step

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.02358v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Vernon Toh, Navonil Majumder, Zhengyuan Liu, Nancy F. Chen, Soujanya Poria
- Tags: agent, benchmark
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.02358v1

## One-Sentence Summary
To operate robustly in open-world environments, autonomous agents should be able to infer the behavior of unfamiliar systems through interaction alone, even in the absence of...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：To operate robustly in open-world environments, autonomous agents should be able to infer the behavior of unfamiliar systems through interaction alone, even in the absence of documentation.

进一步看，论文的核心做法或实验重点可以概括为：However, existing tool-use benchmarks expose semantic tool schemas in static environments, allowing agents to rely on prior knowledge rather than autonomous discovery.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
To operate robustly in open-world environments, autonomous agents should be able to infer the behavior of unfamiliar systems through interaction alone, even in the absence of documentation. However, existing tool-use benchmarks expose semantic tool schemas in static environments, allowing agents to rely on prior knowledge rather than autonomous discovery. To address this limitation, we introduce ScrambleToolBench, an interactive terminal benchmark designed to isolate behavioral reasoning. By removing semantic cues and enforcing a continuous task curriculum, the benchmark requires agents to uncover hidden tool behaviors entirely through trial-and-error interaction. The benchmark further introduces dynamic challenges, including mapping drift, stochastic action failures, and temporal execution windows, to evaluate whether agents can revise and adapt their hypotheses as the environment changes. Our evaluation of state-of-the-art language models reveals that successful initial discovery does not translate into robust adaptation. When faced with structural changes such as mapping drift, agents fail to use deductive strategies such as cycle tracing, and instead exhibit belief inertia or fall back to exhaustive search. Increasing test-time reasoning only amplifies this expensive brute-force search rather than enabling deductive recovery. While equipping agents with persistent memory reduces compounding errors, they remain unable to efficiently infer structural changes, highlighting a gap in current agent reasoning.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
