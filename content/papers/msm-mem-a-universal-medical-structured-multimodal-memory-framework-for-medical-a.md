# MSM-Mem: A Universal Medical Structured Multimodal Memory Framework for Medical AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.21810v1
- Published: 2026-08-22
- Updated: 2026-08-22
- Authors: Md Asaduzzaman Jabin, Khoa Le, Lin Zhao, Tianming Liu
- Tags: agent, context, episodic
- Categories: cs.LG, cs.CV
- URL: http://arxiv.org/abs/2608.21810v1

## One-Sentence Summary
Clinical decision-making is inherently experience-driven: physicians progressively refine their reasoning by synthesizing patient history, multimodal observations, and prior...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Clinical decision-making is inherently experience-driven: physicians progressively refine their reasoning by synthesizing patient history, multimodal observations, and prior diagnostic experiences across interactions.

进一步看，论文的核心做法或实验重点可以概括为：In contrast, current multimodal large language model (MLLM)-based medical AI agents largely operate as stateless inference systems, generating decisions independently for each interaction without retaining or...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic
- 检索关键词命中：agent memory
- 来源分类信息：cs.LG, cs.CV

## Abstract Snapshot
Clinical decision-making is inherently experience-driven: physicians progressively refine their reasoning by synthesizing patient history, multimodal observations, and prior diagnostic experiences across interactions. In contrast, current multimodal large language model (MLLM)-based medical AI agents largely operate as stateless inference systems, generating decisions independently for each interaction without retaining or internalizing experiential knowledge. This discrepancy limits their ability to progressively improve reasoning reliability through usage and adapt to longitudinal patient contexts in real-world clinical workflows. In this study, we propose Medical Structured Multimodal Memory (MSM-Mem), an agentic memory framework that enables medical AI agents to evolve through accumulated clinical experiences. MSM-Mem organizes heterogeneous clinical experiences into semantic, episodic, and visual memory and incrementally updates them during inference, allowing the agent to retrieve prior experiences to inform current reasoning and progressively refine decision-making over time. Evaluations on MoE-LLaVA backbones demonstrate consistent performance improve- ments with further gains observed through continued usage. In general, MSM-Mem offers a viable pathway toward medical AI agents capable of evolving their reasoning competence in a manner analogous to the way clinicians learn from practice over time.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
