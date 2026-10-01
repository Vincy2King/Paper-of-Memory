# Quantum Computing for Network Security Classification: Near-Term Classification and Long-Term Memory Efficiency

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.36479v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Yuqing Li, Poonam Bala Nehru, Yunpeng Zhang, Danindu Gammanpilage, Xin Jin, Zeguan Wu, Junyu Liu
- Tags: long-term
- Categories: quant-ph, cs.AI, cs.LG
- URL: http://arxiv.org/abs/2609.36479v1

## One-Sentence Summary
Quantum computing has already been explored in several network-security applications.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Quantum computing has already been explored in several network-security applications.

进一步看，论文的核心做法或实验重点可以概括为：However, how quantum computing may contribute to network-security classification in both the near term and the longer term has not been systematically discussed.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term
- 检索关键词命中：long-term memory
- 来源分类信息：quant-ph, cs.AI, cs.LG

## Abstract Snapshot
Quantum computing has already been explored in several network-security applications. However, how quantum computing may contribute to network-security classification in both the near term and the longer term has not been systematically discussed. This paper studies this question through two complementary experiments. First, we evaluate near-term quantum-kernel support vector machines (SVMs) on practical network-security classification tasks and compare them with classical SVM baselines on KDD Cup 1999, CICIDS2017, and BoT-IoT. Across these runs, quantum kernels are competitive. They can match or improve classical baselines in some settings, while classical RBF kernels remain stronger in others. This suggests that near-term quantum-kernel methods should be evaluated as practical, dataset-dependent alternatives to classical kernels rather than as uniformly superior replacements. Second, we use quantum oracle sketching (QOS) to study a longer-term memory advantage for classification with streaming classical samples. In QOS, samples are processed online and used to incrementally construct an approximate quantum oracle, which provides coherent query access for downstream quantum algorithms without retaining the entire dataset. Under the QOS-inspired machine-size estimate, comparable accuracy corresponds to a substantially smaller effective memory-size proxy than explicit sparse/QRAM-style storage. Compared with a simple streaming proxy, the result is more nuanced because aggressive feature filtering can make the streaming dimension small. This suggests that the long-term value of quantum computing for network-security classification may lie in memory-efficient data access rather than immediate runtime speedup. Together, these experiments show how quantum computing may contribute to network-security classification from near-term classification performance and longer-term memory efficiency.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
