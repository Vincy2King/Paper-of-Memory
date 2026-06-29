# DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.27499v1
- Published: 2026-06-25
- Updated: 2026-06-25
- Authors: Yujin Tang, Chenming Shang, Ruize Xu, Nikhil Singh
- Tags: agent, benchmark
- Categories: cs.CV, cs.AI, cs.CL
- URL: http://arxiv.org/abs/2606.27499v1

## One-Sentence Summary
Research on agent memory has matured rapidly, but almost entirely on the text side: few existing benchmarks ask, in an interactive environment, when an agent genuinely needs to...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Research on agent memory has matured rapidly, but almost entirely on the text side: few existing benchmarks ask, in an interactive environment, when an agent genuinely needs to remember what it saw rather than what it...

进一步看，论文的核心做法或实验重点可以概括为：We introduce DMV-Bench (Code: https://github.com/yyyujintang/DMV-Bench), the first interactive benchmark for multimodal-agent visual memory.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory
- 来源分类信息：cs.CV, cs.AI, cs.CL

## Abstract Snapshot
Research on agent memory has matured rapidly, but almost entirely on the text side: few existing benchmarks ask, in an interactive environment, when an agent genuinely needs to remember what it saw rather than what it could write down. We introduce DMV-Bench (Code: https://github.com/yyyujintang/DMV-Bench), the first interactive benchmark for multimodal-agent visual memory. DMV-Bench is built on a controlled home-furnishing e-commerce catalogue of 1,000 product variants in which a text-leakage contract keeps the discriminative signal of each task in the pixels alone. Across a chain of autonomous shopping sessions, every visited product image carries a unique, pre-rendered incidental cue, and the agent is later asked to recall a particular cued product and navigate to its URL. Inspired by dual-coding theory, we propose DualMem, a memory architecture that maintains a visual and a verbal code in parallel. On DMV-Bench, DualMem outperforms a caption baseline and three recent multimodal agent-memory systems at every chain length J in {5, 10, 15, 50} on both Gemini 2.5 Flash and Qwen2.5-VL-7B, with the lead surviving controls for memory-bank size and encoding-position bias, and an asymmetric dual-coding regime in which vision carries the cue end-to-end while the verbal channel plays a smaller query-grounding role.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
