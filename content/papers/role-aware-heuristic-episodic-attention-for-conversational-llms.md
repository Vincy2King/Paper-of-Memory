# Role-aware Heuristic Episodic Attention for Conversational LLMs

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.00958v1
- Published: 2026-10-01
- Updated: 2026-10-01
- Authors: Wanyang Hong, Zhaoning Zhang, Yi Chen, Libo Zhang, Baihui Liu, Linbo Qiao, Zhiliang Tian, Dongsheng Li
- Tags: context, conversation, episodic, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2610.00958v1

## One-Sentence Summary
Large language models often lose track of persistent instructions and relevant information as multi-turn conversations grow.

## Introduction
这篇论文被纳入仓库，是因为它和 `context, conversation, episodic, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language models often lose track of persistent instructions and relevant information as multi-turn conversations grow.

进一步看，论文的核心做法或实验重点可以概括为：We study this cumulative contextual decay through three related failure modes: attention pollution, dilution, and drift.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, conversation, episodic, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Large language models often lose track of persistent instructions and relevant information as multi-turn conversations grow. We study this cumulative contextual decay through three related failure modes: attention pollution, dilution, and drift. We propose REA (Role-aware Heuristic Episodic Attention), a context-management framework that assigns different persistence and representation policies to instructions and episodic interactions. Instructional Memory retains identified global constraints in a dedicated prefix. Episodic Memory preserves user inputs and compresses model replies, while heuristic retrieval selects raw text, compressed representations, or omission for each historical turn. On Long-MT-Bench+, REA improves the judge score from 6.32 to 7.36 on a 10-point scale, a 16.5% relative gain over the Vanilla baseline, and reduces average latency by 2.91$\times$. Additional evaluations show aggregate gains on three backbones spanning 1.7B-7B parameters and on Chinese and English role-playing tasks. These results support role-aware context management as a practical approach to maintaining conversational continuity and instruction adherence.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
