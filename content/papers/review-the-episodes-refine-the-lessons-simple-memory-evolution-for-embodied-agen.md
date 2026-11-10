# Review the Episodes, Refine the Lessons: Simple Memory Evolution for Embodied Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.11509v1
- Published: 2026-11-08
- Updated: 2026-11-08
- Authors: Yifei Yao, Yude Zou, Xing Gao, Guanbo Jiao, Yukai Wang, Jianming Ma, Weinan Zhang, Chunhua Shen
- Tags: agent
- Categories: cs.RO, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2611.11509v1

## One-Sentence Summary
Recent studies of embodied agents based on frontier multimodal large language models (MLLMs) develop harness engineering around the MLLM, such as harnesses with post-trained...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent studies of embodied agents based on frontier multimodal large language models (MLLMs) develop harness engineering around the MLLM, such as harnesses with post-trained policies and recursive self-improvement loops.

进一步看，论文的核心做法或实验重点可以概括为：Yet whether these additions exceed the native capability of the MLLM remains unexplored.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：working memory
- 来源分类信息：cs.RO, cs.AI, cs.LG

## Abstract Snapshot
Recent studies of embodied agents based on frontier multimodal large language models (MLLMs) develop harness engineering around the MLLM, such as harnesses with post-trained policies and recursive self-improvement loops. Yet whether these additions exceed the native capability of the MLLM remains unexplored. We introduce SimplEvo to explore how far an MLLM can improve under direct control when it retains its execution experience in self-written text memories. It requires no weight updates, post-trained policies, or privileged information. The MLLM writes a coordinate-free task memory once from a single demonstration. Under a strict train-test protocol, it then creates a bounded working memory on training episodes only and refines it after each episode with lessons on procedure, completion, and recovery. Both memories stay fixed at test time. On EBench, SimplEvo lifts the success rate (SR) of GPT-6-Astra under direct control from 46.7% to 81.7%, and tops the RoboDojo leaderboard with 69.63% SR and a score of 75.32. Compared with memories that also store past visual frames, SimplEvo reaches a similar SR with text memory alone while using fewer tokens. With its memories fixed, SimplEvo also generalizes to unseen layouts and randomized scene configurations. Moreover, the working memory transfers across models: written by GPT-6-Astra, it can be reused as is by weaker MLLMs and improve their performance without any adaptation of their own.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
