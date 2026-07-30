# Setoka: A Benchmark for Hierarchical User Understanding in Personalized Agents over Heterogeneous Data

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.27056v1
- Published: 2026-07-29
- Updated: 2026-07-29
- Authors: Lingyang Zeng, Guangze Chen, Kaichen Yu, Zhicheng Pan, Siyang Weng, Zirui Hu, Xiangyun Du, Hailin He, Rong Zhang, Chengcheng Yang, Kai Huang, Xuan Zhou
- Tags: agent, benchmark, conversation, episodic, long-term, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2607.27056v1

## One-Sentence Summary
Personalized agents are increasingly applied to assist users across a wide range of tasks.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personalized agents are increasingly applied to assist users across a wide range of tasks.

进一步看，论文的核心做法或实验重点可以概括为：Effective personalized assistance requires not only retrieving explicit facts from past interactions stored in agent memory, but also inferring abstract personal characteristics.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, episodic, long-term, retrieval
- 检索关键词命中：agent memory, episodic memory, memory augmented, memory benchmark, memory benchmarks, memory retrieval
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Personalized agents are increasingly applied to assist users across a wide range of tasks. Effective personalized assistance requires not only retrieving explicit facts from past interactions stored in agent memory, but also inferring abstract personal characteristics. However, existing memory benchmarks primarily evaluate whether an agent can retrieve information explicitly stated in conversational histories, failing to provide an effective assessment of deeper user understanding. In this work, we propose Setoka, a benchmark for evaluating memory-augmented personalized agents with hierarchical user understanding from heterogeneous data. Grounded in theories from cognitive and personality psychology, Setoka defines four levels of user understanding, i.e., semantic memory, episodic memory, behavior pattern, and personality trait. Moreover, to enable realistic yet privacy-preserving evaluation, we design a psychometrics-based pipeline that synthesizes diverse, coherent heterogeneous user data and queries at scale. Finally, we leverage Setoka to evaluate 3 language models combined with 5 memory systems for 10 synthetic users. Our comprehensive evaluation reveals that while existing systems perform well on semantic memory retrieval, their performance declines on episodic memory. Moreover, when dealing with behavior pattern and personality trait understanding tasks that require integrating heterogeneous and fragmented information dispersed over time, performance declines even further. These findings demonstrate that user understanding cannot be handled by simple fact retrieval, motivating the design of memory mechanisms for cross-source integration and abstraction over long-term user behavior.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
