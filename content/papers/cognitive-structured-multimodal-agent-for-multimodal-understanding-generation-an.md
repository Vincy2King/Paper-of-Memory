# Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.08497v1
- Published: 2026-07-09
- Updated: 2026-07-09
- Authors: Feng Wang, Canmiao Fu, Zhipeng Huang, Chen Li, Jing Lyu, Ge Li
- Tags: agent, benchmark, context, conversation, episodic, retrieval
- Categories: cs.CV, cs.AI, cs.CL, cs.LG
- URL: http://arxiv.org/abs/2607.08497v1

## One-Sentence Summary
Recent unified multimodal models show a single architecture can jointly perform vision/language understanding and image generation/editing.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recent unified multimodal models show a single architecture can jointly perform vision/language understanding and image generation/editing.

进一步看，论文的核心做法或实验重点可以概括为：However, they repeatedly feed all historical visual and textual inputs into a shared context window, limiting long-horizon multimodal dialogue due to visual token explosion and unreliable cross-turn referencing.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, episodic, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CV, cs.AI, cs.CL, cs.LG

## Abstract Snapshot
Recent unified multimodal models show a single architecture can jointly perform vision/language understanding and image generation/editing. However, they repeatedly feed all historical visual and textual inputs into a shared context window, limiting long-horizon multimodal dialogue due to visual token explosion and unreliable cross-turn referencing. We propose a Cognitive-structured Multimodal Agent that externalizes visual information into an Episodic Visual Memory and selectively reactivates relevant episodes during reasoning. The agent consists of a Perceptual Abstraction Engine for structured visual abstraction, a Cognitive Retrieval Engine for cross-turn memory retrieval, and a Multimodal Executive Controller for autonomous task inference and action planning. To address the lack of turn-level retrieval supervision in existing datasets, we develop a Unified Scenario Engine that programmatically generates structured multi-turn conversations with fine-grained retrieval annotations, enabling reinforcement learning to optimize abstraction and retrieval policies. We also construct a long-horizon visual-dialogue benchmark stratified by difficulty to evaluate episodic visual recall. Our 8B agent achieves 91.4% retrieval accuracy over 20-turn sessions, surpassing 32B baselines by +8.2% while nearly halving per-turn inference time (23.1s -> 12.7s). We further present the Cognitive-structured Multimodal Agent Harness (CMA-Harness), a tool-augmented deployment of the same cognitive structure integrating persistent multimodal memory, web access, image generation/editing/composition tools, and OpenAI-compatible serving. Structured memory and modular decision-making offer a more scalable, efficient paradigm for long-horizon multimodal agents than monolithic parameter scaling. Code: https://github.com/caseclose/cma-harness ; Project page: https://caseclose.github.io/cma-harness/

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
