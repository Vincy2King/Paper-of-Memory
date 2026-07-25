# CAST: Character-and-Scene Episodic Memory for Agents

- Source: OpenReview
- Venue: CoRR 2026
- Paper ID: openreview:LpgVDJo3MB
- Published: 2026-12-31
- Updated: 2026-07-25
- Authors: {'fullname': 'Kexin Ma', 'username': '~Kexin_Ma1'}, {'fullname': 'Bojun Li', 'username': ''}, {'fullname': 'Yuhua Tang', 'username': ''}, {'fullname': 'Liting Sun', 'username': ''}, {'fullname': 'Ruochun Jin', 'username': ''}
- Tags: agent, conversation, episodic
- Categories: OpenReview.net/Public_Article/DBLP.org/-/Record
- URL: https://openreview.net/forum?id=LpgVDJo3MB

## One-Sentence Summary
Episodic memory is a central component of human memory, which refers to the ability to recall coherent events grounded in who, when, and where.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, episodic` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Episodic memory is a central component of human memory, which refers to the ability to recall coherent events grounded in who, when, and where.

进一步看，论文的核心做法或实验重点可以概括为：However, most agent memory systems only emphasize semantic recall and treat experience as structures such as key-value, vector, or graph, which makes them struggle to represent and retrieve coherent events.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2026
- 高亮主题命中：agent, conversation, episodic
- 检索关键词命中：agent memory, episodic memory
- 来源分类信息：OpenReview.net/Public_Article/DBLP.org/-/Record

## Abstract Snapshot
Episodic memory is a central component of human memory, which refers to the ability to recall coherent events grounded in who, when, and where. However, most agent memory systems only emphasize semantic recall and treat experience as structures such as key-value, vector, or graph, which makes them struggle to represent and retrieve coherent events. To address this challenge, we propose a Character-and-Scene based memory architecture(CAST) inspired by dramatic theory. Specifically, CAST constructs 3D scenes (time/place/topic) and organizes them into character profiles that summarize the events of a character to represent episodic memory. Moreover, CAST complements this episodic memory with a graph-based semantic memory, which yields a robust dual memory design. Experiments demonstrate that CAST has averagely improved 8.11% F1 and 10.21% J(LLM-as-a-Judge) than baselines on various datasets, especially on open and time-sensitive conversational questions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
