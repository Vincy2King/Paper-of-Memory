# Remembering by Asking: Retrieval-Induced Memory Evolution for LLM Agents

- Source: OpenReview
- Venue: ACL ARR 2026 May Submission
- Paper ID: openreview:xjNO8EEDVy
- Published: 2026-06-02
- Updated: 2026-06-16
- Authors: Unknown
- Tags: agent, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2026/May/-/Submission
- URL: https://openreview.net/forum?id=xjNO8EEDVy

## One-Sentence Summary
Long-term memory is essential for LLM agents, yet most systems update memory only when new interactions arrive: dialogues trigger addition, revision, or deletion, while the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2026 May Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory is essential for LLM agents, yet most systems update memory only when new interactions arrive: dialogues trigger addition, revision, or deletion, while the memory bank remains mostly static once the...

进一步看，论文的核心做法或实验重点可以概括为：This contrasts with human memory, which can reorganize through self-initiated recall and be reshaped by external retrieval cues.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2026 May Submission
- 高亮主题命中：agent, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：aclweb.org/ACL/ARR/2026/May/-/Submission

## Abstract Snapshot
Long-term memory is essential for LLM agents, yet most systems update memory only when new interactions arrive: dialogues trigger addition, revision, or deletion, while the memory bank remains mostly static once the input stream pauses. This contrasts with human memory, which can reorganize through self-initiated recall and be reshaped by external retrieval cues. We propose RIME (Retrieval-Induced Memory Evolution), a framework that evolves an existing memory bank through self-driven evolution and user-query-driven adaptation. In the self-driven path, RIME periodically recalls existing memories without a user query to merge temporally related episodes, reduce redundancy, resolve conflicts, and strengthen entity-relation structures. In the user-query-driven path, retrieval activates memories, entities, relations, and temporal cues for the current question; feedback from recalled evidence then guides evidence-grounded refinement, relation revision, and importance-score adjustment while softly demoting inactive or redundant regions. Both paths share a recall-feedback-update process, making memory more compact, better organized, and easier to retrieve. On LoCoMo, RIME improves over D-Mem from 53.5 to 56.2 F1, 43.1 to 49.1 BLEU, and 76.3 to 81.6 GPT-4o-mini judge score, while reducing stored memories by 60.8%.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
