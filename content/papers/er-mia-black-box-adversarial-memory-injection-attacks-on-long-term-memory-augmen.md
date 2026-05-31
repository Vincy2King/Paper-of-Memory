# ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models

- Source: OpenReview
- Venue: CoRR 2026
- Paper ID: openreview:dvHe2slkTV
- Published: 2026-12-31
- Updated: 2026-05-30
- Authors: {'fullname': 'Mitchell Piehl', 'username': ''}, {'fullname': 'Zhaohan Xi', 'username': ''}, {'fullname': 'Zuobin Xiong', 'username': ''}, {'fullname': 'Pan He', 'username': '~Pan_He1'}, {'fullname': 'Muchao Ye', 'username': ''}
- Tags: context, long-term, retrieval
- Categories: OpenReview.net/Public_Article/DBLP.org/-/Record
- URL: https://openreview.net/forum?id=dvHe2slkTV

## One-Sentence Summary
Large language models (LLMs) are increasingly augmented with long-term memory systems to overcome finite context windows and enable persistent reasoning across interactions.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `CoRR 2026` 这个 venue 相关。

从摘要来看，作者主要关注的是：Large language models (LLMs) are increasingly augmented with long-term memory systems to overcome finite context windows and enable persistent reasoning across interactions.

进一步看，论文的核心做法或实验重点可以概括为：However, recent research finds that LLMs become more vulnerable because memory provides extra attack surfaces.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：CoRR 2026
- 高亮主题命中：context, long-term, retrieval
- 检索关键词命中：long-term memory, memory-augmented
- 来源分类信息：OpenReview.net/Public_Article/DBLP.org/-/Record

## Abstract Snapshot
Large language models (LLMs) are increasingly augmented with long-term memory systems to overcome finite context windows and enable persistent reasoning across interactions. However, recent research finds that LLMs become more vulnerable because memory provides extra attack surfaces. In this paper, we present the first systematic study of black-box adversarial memory injection attacks that target the similarity-based retrieval mechanism in long-term memory-augmented LLMs. We introduce ER-MIA, a unified framework that exposes this vulnerability and formalizes two realistic attack settings: content-based attacks and question-targeted attacks. In these settings, ER-MIA includes an arsenal of composable attack primitives and ensemble attacks that achieve high success rates under minimal attacker assumptions. Extensive experiments across multiple LLMs and long-term memory systems demonstrate that similarity-based retrieval constitutes a fundamental and system-level vulnerability, revealing security risks that persist across memory designs and application scenarios.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
