# Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory

- Source: OpenReview
- Venue: ICLR 2026 Poster
- Paper ID: openreview:PMz29A7Muq
- Published: 2026-01-26
- Updated: 2026-04-11
- Authors: Lin Long, Yichen He, Wentao Ye, Yiyuan Pan, Yuan Lin, Hang Li, Junbo Zhao, Wei Li
- Tags: agent, benchmark, episodic, long-term
- Categories: ICLR.cc/2026/Conference/-/Submission
- URL: https://openreview.net/forum?id=PMz29A7Muq

## One-Sentence Summary
We introduce M3-Agent, a novel multimodal agent framework equipped with long-term memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, episodic, long-term` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ICLR 2026 Poster` 这个 venue 相关。

从摘要来看，作者主要关注的是：We introduce M3-Agent, a novel multimodal agent framework equipped with long-term memory.

进一步看，论文的核心做法或实验重点可以概括为：Like humans, M3-Agent can process real-time visual and auditory inputs to build and update episodic and semantic memories, gradually accumulating world knowledge.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ICLR 2026 Poster
- 高亮主题命中：agent, benchmark, episodic, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：ICLR.cc/2026/Conference/-/Submission

## Abstract Snapshot
We introduce M3-Agent, a novel multimodal agent framework equipped with long-term memory. Like humans, M3-Agent can process real-time visual and auditory inputs to build and update episodic and semantic memories, gradually accumulating world knowledge. Its memory is organized in an entity-centric, multimodal manner, enabling deeper and more consistent understanding of the environment. Given an instruction, M3-Agent autonomously performs multi-turn reasoning and retrieves relevant memories to complete tasks. To evaluate memory effectiveness and memory-based reasoning in multimodal agents, we develop M3-Bench, a long-video question answering benchmark comprising 100 newly recorded robot-perspective videos (M3-Bench-robot) and 920 diverse web-sourced videos (M3-Bench-web). We annotate QA pairs designed to test capabilities essential for agent applications, such as person understanding, general knowledge extraction, and cross-modal reasoning. Experimental results show that M3-Agent, trained via reinforcement learning, outperforms the strongest baseline, a prompting agent using Gemini-1.5-pro and GPT-4o, achieving 6.7%, 7.7%, and 5.3% higher accuracy on M3-Bench-robot, M3-Bench-web and VideoMME-long, respectively. Our work advances multimodal agents toward more human-like long-term memory and provides insights for their practical design. Models, datasets and code are available at https://github.com/ByteDance-Seed/m3-agent.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
