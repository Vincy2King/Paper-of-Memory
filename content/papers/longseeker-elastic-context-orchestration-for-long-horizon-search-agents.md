# LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.05191v1
- Published: 2026-05-06
- Updated: 2026-05-06
- Authors: Yijun Lu, Rui Ye, Yuwen Du, Jiajun Wang, Songhua Liu, Siheng Chen
- Tags: agent, benchmark, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.05191v1

## One-Sentence Summary
Long-horizon search agents must manage a rapidly growing working context as they reason, call tools, and observe information.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon search agents must manage a rapidly growing working context as they reason, call tools, and observe information.

进一步看，论文的核心做法或实验重点可以概括为：Naively accumulating all intermediate content can overwhelm the agent, increasing costs and the risk of errors.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context
- 检索关键词命中：working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-horizon search agents must manage a rapidly growing working context as they reason, call tools, and observe information. Naively accumulating all intermediate content can overwhelm the agent, increasing costs and the risk of errors. We propose that effective context management should be adaptive: parts of the agent's trajectory are maintained at different levels of detail depending on their current relevance to the task. To operationalize this principle, we introduce Context-ReAct, a general agentic paradigm for elastic context orchestration that integrates reasoning, context management, and tool use in a unified loop. Context-ReAct provides five atomic operations: Skip, Compress, Rollback, Snippet and Delete, which allow the agent to dynamically reshape its working context, preserving important evidence, summarizing resolved information, discarding unhelpful branches, and controlling context size. We prove that the Compress operator is expressively complete, while the other specialized operators provide efficiency and fidelity guarantees that reduce generation cost and hallucination risk. Building on this paradigm, we develop LongSeeker, a long-horizon search agent fine-tuned from Qwen3-30B-A3B on 10k synthesized trajectories. Across four representative search benchmarks, LongSeeker achieves 61.5% on BrowseComp and 62.5% on BrowseComp-ZH, substantially outperforming Tongyi DeepResearch (43.2% and 46.7%) and AgentFold (36.2% and 47.3%). These results highlight the potential of adaptive context management, showing that agents can achieve more reliable and efficient long-horizon reasoning by actively shaping their working memory.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
