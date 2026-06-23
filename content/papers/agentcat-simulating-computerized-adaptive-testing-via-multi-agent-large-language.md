# AgentCAT: Simulating Computerized Adaptive Testing via Multi-Agent Large Language Models

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.21832v1
- Published: 2026-06-20
- Updated: 2026-06-20
- Authors: Weiyuan Zhou, Haiping Ma, Xiaoshan Yu, Changqian Wang, Shangshang Yang, Xingyi Zhang
- Tags: agent, benchmark, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.21832v1

## One-Sentence Summary
Computerized Adaptive Testing (CAT), as a key technology for personalized education, aims to accurately assess examinee proficiency by retrieving exercises dynamically matching...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Computerized Adaptive Testing (CAT), as a key technology for personalized education, aims to accurately assess examinee proficiency by retrieving exercises dynamically matching current ability estimates.

进一步看，论文的核心做法或实验重点可以概括为：However, existing CAT research is constrained by limitations of static offline data and isolated component optimization.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Computerized Adaptive Testing (CAT), as a key technology for personalized education, aims to accurately assess examinee proficiency by retrieving exercises dynamically matching current ability estimates. However, existing CAT research is constrained by limitations of static offline data and isolated component optimization. Restricted by partial labels in offline logs, researchers degrade the dynamic assessment process into static sequence prediction. Current research focuses on isolated perspectives, e.g., selection or diagnosis, neglecting the overall CAT interaction process. To address this, we propose AgentCAT, a Large Language Model-based multi-agent simulation system, to construct a high-fidelity benchmarking environment for dynamic testing. This framework comprises three modules: (1) The examinee agent with memory retrieval and Chain-of-Thought reasoning simulates responses based on cognitive profiles; (2) The selection agent uses coarse-to-fine bucketing and knowledge graph exploration to balance local difficulty and global coverage; (3) The supervisor uses dual-auditing and robust update to ensure convergence and validity. To validate the framework, we evaluated on two real-world datasets across three dimensions: macro-level ability convergence, micro-level interaction logic, and data sparsity resilience. Results show AgentCAT achieves effective ability estimation, and its selection strategy balances difficulty adaptation and instructional coherence, aligning with human pedagogical intuition.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
