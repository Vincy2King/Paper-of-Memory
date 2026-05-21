# MemGym: a Long-Horizon Memory Environment for LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.20833v1
- Published: 2026-05-20
- Updated: 2026-05-20
- Authors: Wujiang Xu, Yu Wang, Kai Mei, Kaiqu Liang, Zhenting Wang, Mingyu Jin, Han Zhang, Shi-Xiong Zhang, Wenyue Hua, Sambit Sahu, Dimitris N. Metaxas
- Tags: agent, benchmark, compression, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2605.20833v1

## One-Sentence Summary
Memory is a central capability for LLM agents operating across long-horizon tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, compression, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory is a central capability for LLM agents operating across long-horizon tasks.

进一步看，论文的核心做法或实验重点可以概括为：Existing memory benchmarks predominantly evaluate retention of personalized information in multi-turn chat scenarios, overlooking the dynamic memory formation that occurs during extended agent execution.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, compression, retrieval
- 检索关键词命中：agent memory, memory benchmark, memory benchmarks, memory reasoning
- 来源分类信息：cs.CL

## Abstract Snapshot
Memory is a central capability for LLM agents operating across long-horizon tasks. Existing memory benchmarks predominantly evaluate retention of personalized information in multi-turn chat scenarios, overlooking the dynamic memory formation that occurs during extended agent execution. Consequently, the memory systems they produce transfer poorly to realistic agentic environments, such as coding and web navigation. We present MemGym, a benchmark for agentic memory that unifies existing agent gyms and in-house memory-grounded pipelines behind one memory-reasoning interface. MemGym spans five evaluation tracks grouped into four agentic regimes: tool-use dialogue (tau2-bench), multi-turn deep-research search (MEMGYM-DR), coding (SWE-Gym and MEMGYM-CODEQA), and computer use (WebArena-Infinity). MemGym reports memory-isolated scores that decouple memory performance from reasoning, retrieval, and tool-use ability, so memory strategies can be ranked without those confounders. Our synthetic pipelines for MEMGYM-CODEQA and MEMGYM-DR are length-controllable, ablation-verified at every stage, and tightly aligned with downstream scenarios. To make evaluation on coding environments academically tractable, we train MemRM, a lightweight reward model (Qwen3-1.7B fine-tuned with QLoRA) that scores compression quality as a fast scalar read in place of full Docker rollouts.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
