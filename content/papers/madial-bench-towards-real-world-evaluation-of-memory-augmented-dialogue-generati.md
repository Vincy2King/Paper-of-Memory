# MADial-Bench: Towards Real-world Evaluation of Memory-Augmented Dialogue Generation

- Source: OpenReview
- Venue: ACL ARR 2024 October Submission
- Paper ID: openreview:nRcK1XpioK
- Published: 2025-01-09
- Updated: 2026-07-02
- Authors: Unknown
- Tags: benchmark, conversation, long-term, retrieval
- Categories: aclweb.org/ACL/ARR/2024/October/-/Submission
- URL: https://openreview.net/forum?id=nRcK1XpioK

## One-Sentence Summary
Long-term memory is important for chatbots and dialogue systems (DS) to create consistent and human-like conversations, evidenced by numerous developed memory-augmented DS (MADS).

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `ACL ARR 2024 October Submission` 这个 venue 相关。

从摘要来看，作者主要关注的是：Long-term memory is important for chatbots and dialogue systems (DS) to create consistent and human-like conversations, evidenced by numerous developed memory-augmented DS (MADS).

进一步看，论文的核心做法或实验重点可以概括为：To evaluate the effectiveness of such MADS, existing commonly used evaluation metrics, like retrieval accuracy and perplexity (PPL), mainly focus on query-oriented factualness and language quality assessment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：ACL ARR 2024 October Submission
- 高亮主题命中：benchmark, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval, memory-augmented
- 来源分类信息：aclweb.org/ACL/ARR/2024/October/-/Submission

## Abstract Snapshot
Long-term memory is important for chatbots and dialogue systems (DS) to create consistent and human-like conversations, evidenced by numerous developed memory-augmented DS (MADS). To evaluate the effectiveness of such MADS, existing commonly used evaluation metrics, like retrieval accuracy and perplexity (PPL), mainly focus on query-oriented factualness and language quality assessment. However, these metrics often lack practical value. Moreover, the evaluation dimensions are insufficient for human-like assessment in DS. Regarding memory-recalling paradigms, current evaluation schemes only consider passive memory retrieval while ignoring diverse memory recall with rich triggering factors, e.g., emotions and surroundings, which can be essential in emotional support scenarios. To bridge the gap, we construct a novel Memory-Augmented Dialogue Benchmark (MADail-Bench) covering various memory-recalling paradigms based on cognitive science and psychology theories. The benchmark assesses two tasks separately: memory retrieval and memory recognition with the incorporation of both passive and proactive memory recall data. We introduce new scoring criteria to the evaluation, including memory injection, emotion support (ES) proficiency, and intimacy, to comprehensively assess generated responses. Results from cutting-edge embedding models and large language models on this benchmark indicate the potential for further advancement. Extensive testing further reveals correlations between memory injection, ES proficiency, and intimacy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
