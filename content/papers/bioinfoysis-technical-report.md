# Bioinfoysis Technical Report

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.03871v1
- Published: 2026-09-03
- Updated: 2026-09-03
- Authors: Qingyang Shao, Xin Zhang, Zhouyang Yuan, Xianying Chen, Yujia Xiang, Zihao Yang, Tong Ye, Yangqi Zhang, Jiakang Xu, Xiaoqing Yan, Xuan Luo, Keyi Li, Enci Fan, Kai Kang, Zhuohan Liu, Xingyu Jin, Chunran Teng, Tao Li, Xinyu Lv, Minghui Wang, Wenfeng Li, Yidan Gao, Siyu Liu, Mingrui Luo, Zhu Liang, Guanren Qiao, Zhiping Xu
- Tags: agent, context
- Categories: cs.AI, cs.MA
- URL: http://arxiv.org/abs/2609.03871v1

## One-Sentence Summary
Large language model agents have shown promise in bioinformatics, but most existing systems focus primarily on producing final answers, treating planning, tool use, and code...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model agents have shown promise in bioinformatics, but most existing systems focus primarily on producing final answers, treating planning, tool use, and code execution as transient interactions.

进一步看，论文的核心做法或实验重点可以概括为：This design is poorly suited to long-horizon bioinformatics tasks, where conclusions must remain connected to the data, computations, and intermediate evidence that support them.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.MA

## Abstract Snapshot
Large language model agents have shown promise in bioinformatics, but most existing systems focus primarily on producing final answers, treating planning, tool use, and code execution as transient interactions. This design is poorly suited to long-horizon bioinformatics tasks, where conclusions must remain connected to the data, computations, and intermediate evidence that support them. We introduce \textbf{Bioinfoysis}, a multi-agent harness that represents each request as a persistent, artifact-grounded analysis run. Bioinfoysis combines global planning with step-wise, evidence-driven replanning: the planner maintains an executable checklist and revises pending steps using structured handoffs returned after each worker execution. These handoffs bind intermediate results to their responsible agent, checklist step, and plan generation, preventing stale evidence from being silently reused after replanning. A controlled runtime validates generated scripts, tables, and figures before they are used in downstream analysis or reporting, while role-specific context, persistent memory, and governed bioinformatics skills support reliable execution over long analysis trajectories. We evaluate Bioinfoysis on BixBench and two question-answering tracks of LAB-Bench 2. On BixBench, Bioinfoysis achieves state-of-the-art accuracy of 82.4\%. Across four underlying language models, Bioinfoysis increases average accuracy from 27.81\% to 64.13\% on SeqQA2 and from 3.13\% to 31.25\% on DbQA2. These results demonstrate that reliable bioinformatics automation depends not only on model capability, but also on the harness that governs planning, execution, memory, and evidence flow. We hope that the emergence of Bioinfoysis will play a driving and leading role in the development of the bioinformatics community. Our demo website can be seen in https://report.bioinfoysis.com/.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
