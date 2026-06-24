# MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.24595v1
- Published: 2026-06-23
- Updated: 2026-06-23
- Authors: Enze Ma, Yufan Zhou, Wei-Chieh Huang, Jie Yang, Huanhuan Ma, Zixuan Wang, Chengze Li, Chunyu Miao, Philip S. Yu, Zhen Wang
- Tags: agent, benchmark, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2606.24595v1

## One-Sentence Summary
Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms.

进一步看，论文的核心做法或实验重点可以概括为：In practice, however, this memory is evaluated mostly through downstream behavior, such as later answers, personalization quality, or task success, which tests that understanding only indirectly and leaves the memory...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms. In practice, however, this memory is evaluated mostly through downstream behavior, such as later answers, personalization quality, or task success, which tests that understanding only indirectly and leaves the memory artifact itself largely unaudited. We argue that long-term memory should instead be evaluated as an auditable post-interaction artifact: after ordinary assistance, what structured user state can be reconstructed from the memory the agent leaves behind? We instantiate this view in MEMPROBE, a benchmark in which a memory-equipped agent assists simulated users, each carrying a hidden, taxonomy-anchored user-state bank, across a trajectory of leak-controlled tasks, after which that bank is reconstructed from the agent's resulting memory under both full-store and top-k access. Built on synthetic ground truth for efficient, scalable measurement, MEMPROBE spans 50 simulated users with 31 hidden dimensions each (1,550 recovery targets) and tests 5 representative memory systems. Testing state-of-the-art memory agents, we find that successful assistance and recoverable memory behave as distinct capabilities. Task completion nearly saturates, even for a memoryless baseline, while category-balanced recovery stays moderate (about 0.6) and drops further under top-k retrieval. MEMPROBE is the first benchmark to study memory recovery directly, reconstructing the user state a system retains and scoring it against ground truth. We see recovery as a concrete objective for future memory agents to optimize, and MEMPROBE as a step toward an environment where agents are trained to remember their users, growing more faithful the longer they know them.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
