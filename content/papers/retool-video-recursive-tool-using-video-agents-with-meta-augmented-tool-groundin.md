# ReTool-Video: Recursive Tool-Using Video Agents with Meta-Augmented Tool Grounding

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.13228v1
- Published: 2026-05-13
- Updated: 2026-05-13
- Authors: Xiao Liu, Nayu Liu, Junnan Zhu, Ruirui Chen, Guohui Xiang, Changjian Wang, Kaiwen Wei, Rongzhen Li, Jiang Zhong
- Tags: agent, retrieval
- Categories: cs.CV, cs.AI
- URL: http://arxiv.org/abs/2605.13228v1

## One-Sentence Summary
Video understanding requires active evidence seeking, motivating tool-augmented video agents for temporal reasoning, cross-modal understanding, and complex question answering.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Video understanding requires active evidence seeking, motivating tool-augmented video agents for temporal reasoning, cross-modal understanding, and complex question answering.

进一步看，论文的核心做法或实验重点可以概括为：Existing video agents have improved video reasoning with retrieval, memory, frame inspection, and verifier tools, but they still face two limitations: (1) a coarse tool space that lacks fine-grained operations for...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：retrieval memory
- 来源分类信息：cs.CV, cs.AI

## Abstract Snapshot
Video understanding requires active evidence seeking, motivating tool-augmented video agents for temporal reasoning, cross-modal understanding, and complex question answering. Existing video agents have improved video reasoning with retrieval, memory, frame inspection, and verifier tools, but they still face two limitations: (1) a coarse tool space that lacks fine-grained operations for compositional reasoning; and (2) a flat action space that forces high-level video intents into primitive executable tool calls. In this paper, we address these challenges with two complementary designs. First, we construct a MetaAug-Video Tool Library (MVTL), an extensible tool library with 134 registered tools, including 26 base tools for general multimodal signal processing and 108 meta tools for filtering, aggregation, reranking, formatting, and other intermediate-result operations. MVTL supports dual-level access to both structured video information and raw modal evidence, enabling diverse video reasoning scenarios. Second, we propose ReTool-Video, a recursive tool-using method that grounds high-level video intents into executable tool chains. In ReTool-Video, matched actions are executed directly, while unmatched intents are delegated to a resolver for parameter repair, tool substitution, or decomposition. This allows abstract actions such as temporal merging, cross-modal verification, or repeated-event aggregation to be progressively translated into concrete multimodal operations at runtime. Experiments on MVBench, MLVU, and Video-MME w/o sub. show that ReTool-Video consistently outperforms strong baselines. Further analysis demonstrates that recursive grounding and fine-grained meta tools improve the stability and effectiveness of complex video understanding.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
