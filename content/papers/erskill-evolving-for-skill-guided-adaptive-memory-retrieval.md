# ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.12720v1
- Published: 2026-08-13
- Updated: 2026-08-13
- Authors: Haolong Chen, Liang Zhang, Zhuo Li, Lei Xue, Guanrxu Zhu
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2608.12720v1

## One-Sentence Summary
While Large Language Model (LLM) agents increasingly rely on long-term memory for persistent interactions, the retrieval mechanisms governing this memory are rarely treated as...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：While Large Language Model (LLM) agents increasingly rely on long-term memory for persistent interactions, the retrieval mechanisms governing this memory are rarely treated as evolvable components.

进一步看，论文的核心做法或实验重点可以概括为：This static approach limits performance on heterogeneous memory queries, which often demand diverse evidence construction strategies.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory, memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
While Large Language Model (LLM) agents increasingly rely on long-term memory for persistent interactions, the retrieval mechanisms governing this memory are rarely treated as evolvable components. This static approach limits performance on heterogeneous memory queries, which often demand diverse evidence construction strategies. To address this, we introduce \textbf{ERSkill}, a retrieval-centric framework for self-evolving, skill-guided memory access. ERSkill compiles interaction histories into a structured memory store and represents retrieval behaviors as executable skills composed of fundamental primitives. At inference time, a trained router dynamically matches each query to the optimal skill to construct tailored evidence for answer generation. To enable continuous improvement, ERSkill co-evolves the skill set and the router during training. It employs an experience trie to efficiently record explored retrieval paths, alongside a double-frontier mechanism that safely decouples the expansion of new skill capabilities from stable, router-facing deployment. Experiments across multiple agent memory benchmarks demonstrate that ERSkill substantially outperforms strong non-evolving and self-evolving baselines. Notably, it improves the overall average across F1, BLEU-1, and LLM-judge scores by 31.3\% with Qwen3-Next-80B-A3B-Instruct and by 28.1\% with GPT-5.4-nano.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
