# Don't Overthink, Don't Underthink: Toward Adaptive Reasoning in Agentic AI

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.26442v1
- Published: 2026-08-26
- Updated: 2026-08-26
- Authors: Md Jueal Mia, M. Hadi Amini
- Tags: agent, benchmark, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2608.26442v1

## One-Sentence Summary
Recent advances in Large Language Models (LLMs) have shown that increased inference-time reasoning can improve performance on complex tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent advances in Large Language Models (LLMs) have shown that increased inference-time reasoning can improve performance on complex tasks.

进一步看，论文的核心做法或实验重点可以概括为：However, many existing approaches rely on fixed or preallocated reasoning controls, such as fixed token budgets, pre-execution difficulty estimates, or activation-space interventions, and are often evaluated on...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Recent advances in Large Language Models (LLMs) have shown that increased inference-time reasoning can improve performance on complex tasks. However, many existing approaches rely on fixed or preallocated reasoning controls, such as fixed token budgets, pre-execution difficulty estimates, or activation-space interventions, and are often evaluated on standalone reasoning benchmarks rather than full agentic workflows. These assumptions may not hold in agentic AI systems, where reasoning requirements evolve dynamically through planning, tool use, memory retrieval, and agent-to-agent interactions. Consequently, reasoning can become either excessive or insufficient, resulting in unnecessary computation, increased latency, planning drift, excessive tool use, or incomplete solutions. We argue that a major challenge for next-generation agentic AI is not merely how much reasoning a language model should perform, but how it should allocate reasoning according to evolving task demands. We characterize over-reasoning and under-reasoning as recurring failure modes of misallocated reasoning and evaluate them on MATH-500 and the GAIA public validation benchmark. Using tool-decision latency, token consumption, token-limit exhaustion, and answer correctness, our results suggest that cases classified as over-reasoning are associated with higher computational cost without proportional accuracy gains, whereas cases classified as under-reasoning are consistently associated with incorrect or incomplete solutions. These findings motivate future research on adaptive reasoning mechanisms for agentic AI.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
