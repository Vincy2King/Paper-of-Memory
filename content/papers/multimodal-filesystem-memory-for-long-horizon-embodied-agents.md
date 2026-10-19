# Multimodal Filesystem Memory For Long-Horizon Embodied Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.22686v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Chloe Su, Jiahan Li, Zhenting Qi, Chaoran Cheng, Haoyu Chen, Sejoon Jun, Weirui Ye, Yilun Du
- Tags: agent, context, episodic
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.22686v1

## One-Sentence Summary
Agents operating over long horizons need an effective memory that allows them to reuse their experience throughout long interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agents operating over long horizons need an effective memory that allows them to reuse their experience throughout long interactions.

进一步看，论文的核心做法或实验重点可以概括为：If the entire history of an interaction is retained, it becomes difficult to find the relevant experience, while compressing it into summaries may result in the loss of visual and spatial details that are required...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic
- 检索关键词命中：agent memory, episodic memory, persistent memory, working memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Agents operating over long horizons need an effective memory that allows them to reuse their experience throughout long interactions. If the entire history of an interaction is retained, it becomes difficult to find the relevant experience, while compressing it into summaries may result in the loss of visual and spatial details that are required later on. We present \textbf{MFM}, a multimodal filesystem memory architecture that keeps complementary types of agent memory. \textbf{Episodic memory} stores the observations, actions, and outcomes, and \textbf{spatial memory} associates experiences with locations. \textbf{Semantic and procedural memory} build up general knowledge and reusable methods of acting, and \textbf{working memory} holds the current plans. MFM makes use of searchable textual records to connect these different representations to the underlying multimodal episodes. The agents are able to find previous experiences by means of contextual cues and to examine the original observations in order to recover details that are missing from their textual descriptions. Through consolidation, the agents convert experience into higher-level knowledge and procedures while still keeping references to the original episodes. In the case of long-horizon Minecraft and computer-use tasks, MFM leads to improved performance with three base models. With GPT-6-Astra, MFM completes \emph{Mine Diamond from Scratch} and reaches 16 out of 24 milestones on the \emph{Ender Dragon} task, as against 12.7 for the best baseline. On CUABench-KiCad it attains a mean reward of 0.440, as compared to 0.400 for the best baseline and 0.267 in the case of no persistent memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
