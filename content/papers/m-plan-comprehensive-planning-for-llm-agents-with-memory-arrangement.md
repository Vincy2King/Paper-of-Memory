# M-Plan: Comprehensive Planning For LLM Agents with Memory Arrangement

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.27032v1
- Published: 2026-10-19
- Updated: 2026-10-19
- Authors: Ziyang Liu, Jiakang Yuan, Jiayuan Fan, Tao Chen
- Tags: agent, context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.27032v1

## One-Sentence Summary
Large language model (LLM)-based agents have recently demonstrated outstanding performance in single-turn tasks, yet they continue to struggle with long-horizon tasks,...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model (LLM)-based agents have recently demonstrated outstanding performance in single-turn tasks, yet they continue to struggle with long-horizon tasks, particularly in environments without prior training.

进一步看，论文的核心做法或实验重点可以概括为：A key limitation of single LLMs is their difficulty in processing long contexts, which stems from weaknesses in continuous decision-making and reasoning capabilities.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term, retrieval
- 检索关键词命中：long-term memory, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model (LLM)-based agents have recently demonstrated outstanding performance in single-turn tasks, yet they continue to struggle with long-horizon tasks, particularly in environments without prior training. A key limitation of single LLMs is their difficulty in processing long contexts, which stems from weaknesses in continuous decision-making and reasoning capabilities. Although existing multi-agent systems (MAS) equipped with long-term memory bases can partially address this gap, they mostly rely on knowledge reuse or summarization, an approach that is often constrained by directly retrieval without any adaptation for the current task, while the retrieved memory may contain much history noises waiting to be preprocessed. In contrast, MAS characterized by task-specific guidance often lack long-term memory specifically designed for the guidance. To address these challenges, we propose M-Plan, a closed-loop MAS framework that integrates long-term and short-term memory. By combining global-local and past-current guidance, M-Plan enhances agents' performance on multi-turn tasks while maintaining a plug-and-play design. During task execution, agents receive task-specific milestones and insights, and are provided with local hints only when confusion arises, which form global-local guidance together. These guidance generation and utilization construct the short-term memory as well. After task completion, relevant information about the current task is optimized or reorganized before being sent to the long-term memory storage for future retrieval. The designments mentioned above build a comprehensive framework different from other individual long-term or short-term memory works. Extensive experiments on multi-turn tasks including ALFWorld, Webshop, and PDDL across diverse models demonstrate that M-Plan outperforms multiple baseline methods in both accuracy and efficiency.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
