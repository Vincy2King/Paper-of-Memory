# Learning Complementary Agent Groups via Task Hypergraphs for Next-POI Recommendation with Missing Modalities

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.25801v1
- Published: 2026-10-19
- Updated: 2026-10-19
- Authors: Jinze Wang, Yuze Liu, Liang Yuan, Gaoyuan Du, Xiaohang Xu, Yong Xiang, Jiong Jin
- Tags: agent
- Categories: cs.IR
- URL: http://arxiv.org/abs/2610.25801v1

## One-Sentence Summary
Next point-of-interest (POI) recommendation uses visit histories and POI content, but text and images are often missing.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Next point-of-interest (POI) recommendation uses visit histories and POI content, but text and images are often missing.

进一步看，论文的核心做法或实验重点可以概括为：Large language model agents have been applied to recommender systems for preference modeling and evidence acquisition.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Next point-of-interest (POI) recommendation uses visit histories and POI content, but text and images are often missing. Large language model agents have been applied to recommender systems for preference modeling and evidence acquisition. The challenge is to select agents that can jointly analyze the available evidence for each request. We propose \textsc{CATH} (\emph{Complementary Agents via Task Hypergraphs}), which learns to select agent groups for tasks such as comparing candidates or analyzing a POI with missing content. Agents with distinct processing roles are the task hypergraph nodes; each hyperedge connects the selected group and records its analysis goal and target POIs. The policy selects members conditioned on the request, task, and agents already selected. During execution, members share candidate-linked results that guide their subsequent operations. Completed tasks update candidate states and agent memories within the request. A shared ranking head converts candidate states into corrections to a fixed base ranking. Supervised ranking trains the executor, followed by policy optimization that accounts for computation cost. Experiments under natural missingness on Gowalla-CA, Foursquare-NYC, and Foursquare-TKY show 8.4--9.1\% relative NDCG@20 gains over HyperAgent4POI, the strongest prior baseline evaluated. Additional analyses compare group-selection and execution designs, test ranking under additional masking, and characterize quality--cost tradeoffs.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
