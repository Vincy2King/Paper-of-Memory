# Revisiting Persistent Indexing Structures on Intel Optane DC Persistent Memory

- Source: OpenReview
- Venue: J. Comput. Sci. Technol. 2021
- Paper ID: openreview:301wnSekzs
- Published: 2021-12-31
- Updated: 2026-09-19
- Authors: {'fullname': 'Heng Bu', 'username': ''}, {'fullname': 'Mingkai Dong', 'username': ''}, {'fullname': 'Jifei Yi', 'username': ''}, {'fullname': 'Binyu Zang', 'username': ''}, {'fullname': 'Haibo Chen', 'username': '~Haibo_Chen1'}
- Tags: persistent memory
- Categories: OpenReview.net/Public_Article/DBLP.org/-/Record
- URL: https://openreview.net/forum?id=301wnSekzs

## One-Sentence Summary
Persistent indexing structures are proposed in response to emerging non-volatile memory (NVM) to provide high performance yet durable indexes.

## Introduction
这篇论文被纳入仓库，是因为它和 `persistent memory` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `J. Comput. Sci. Technol. 2021` 这个 venue 相关。

从摘要来看，作者主要关注的是：Persistent indexing structures are proposed in response to emerging non-volatile memory (NVM) to provide high performance yet durable indexes.

进一步看，论文的核心做法或实验重点可以概括为：However, due to the lack of real NVM hardware, many prior persistent indexing structures were evaluated via emulation, which varies a lot across different setups and differs from the real deployment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：J. Comput. Sci. Technol. 2021
- 高亮主题命中：persistent memory
- 检索关键词命中：persistent memory
- 来源分类信息：OpenReview.net/Public_Article/DBLP.org/-/Record

## Abstract Snapshot
Persistent indexing structures are proposed in response to emerging non-volatile memory (NVM) to provide high performance yet durable indexes. However, due to the lack of real NVM hardware, many prior persistent indexing structures were evaluated via emulation, which varies a lot across different setups and differs from the real deployment. Recently, Intel has released its Optane DC Persistent Memory Module (PMM), which is the first production-ready NVM. In this paper, we revisit popular persistent indexing structures on PMM and conduct comprehensive evaluations to study the performance differences among persistent indexing structures, including persistent hash tables and persistent trees. According to the evaluation results, we find that Cacheline-Conscious Extendible Hashing (CCEH) achieves the best performance among all evaluated persistent hash tables, and Failure-Atomic ShifT B+-Tree (FAST) and Write Optimal Radix Tree (WORT) perform better than other trees. Besides, we find that the insertion performance of hash tables is heavily influenced by data locality, while the insertion latency of trees is dominated by the flush instructions. We also uncover that no existing emulation methods accurately simulate PMM for all the studied data structures. Finally, we provide three suggestions on how to fully utilize PMM for better performance, including using clflushopt/clwb with sfence instead of clflush, flushing continuous data in a batch, and avoiding data access immediately after it is flushed to PMM.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
