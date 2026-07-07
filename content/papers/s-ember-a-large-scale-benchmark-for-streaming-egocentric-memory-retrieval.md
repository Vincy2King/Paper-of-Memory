# S-EMBER: A Large-Scale Benchmark for Streaming Egocentric Memory Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.02689v1
- Published: 2026-07-02
- Updated: 2026-07-02
- Authors: Xiaodong Wang, Xuanyi Zhao, Pedro Rodriguez, Devendra Singh Sachan, Barlas Oguz, Seungwhan Moon, Shang-Wen Li, Gargi Ghosh, Xin Dong, Wen-Tau Yih
- Tags: agent, benchmark, episodic, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2607.02689v1

## One-Sentence Summary
As wearable devices enable continuous first-person recording, AI assistants must reason across long time horizons to recall past experiences-a capability known as episodic memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：As wearable devices enable continuous first-person recording, AI assistants must reason across long time horizons to recall past experiences-a capability known as episodic memory.

进一步看，论文的核心做法或实验重点可以概括为：Current benchmarks often rely on offline evaluation with access to entire video files, failing to simulate the streaming reality of wearable intelligence.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, episodic, retrieval
- 检索关键词命中：episodic memory, memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
As wearable devices enable continuous first-person recording, AI assistants must reason across long time horizons to recall past experiences-a capability known as episodic memory. Current benchmarks often rely on offline evaluation with access to entire video files, failing to simulate the streaming reality of wearable intelligence. We introduce S-EMBER (Streaming Egocentric Memory Benchmark for Episodic Retrieval), a large-scale benchmark comprising 3,141 videos totaling 388 hours of organic activity captured via Ray-Ban Meta smart glasses. S-EMBER formalizes grounded streaming episodic retrieval, a paradigm shift from global offline search to causal, active recall triggered by visual events in a continuous stream. We provide 9,448 QA pairs requiring manual visual proof through precise temporal localization and supporting flexible response lengths to simulate natural human-AI interaction. Our extensive benchmarking of frontier models uncovers a localization paradox: while semantic reasoning improves with parameter scale, temporal grounding precision remains a stagnant architectural bottleneck that does not benefit from brute-force increases in model size, resolution, or frame density. S-EMBER establishes a hardware-authentic foundation for developing grounded, reliable episodic memory in the next generation of wearable AI agents.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
