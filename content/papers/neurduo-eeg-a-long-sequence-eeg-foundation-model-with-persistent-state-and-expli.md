# NeurDuo-EEG: A Long-Sequence EEG Foundation Model with Persistent State and Explicit Memory

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.38587v1
- Published: 2026-09-29
- Updated: 2026-09-29
- Authors: Yifan Wang, Haiping Liu, Yang Cui, Wenhao Cai, Shuhang Li, Xiaoyang Huang, Xianyang Liu, Jingyu Sun, Yizheng Sun, Cunhang Fan, Tianming Du, Jiancheng Yang, Zhenhong Li, Yunhao Zhang, Hongpeng Zhou, Jingyuan Sun
- Tags: benchmark, retrieval
- Categories: cs.LG
- URL: http://arxiv.org/abs/2609.38587v1

## One-Sentence Summary
Electroencephalography (EEG) is recorded continuously over hours, with relevant dynamics spanning timescales from milliseconds to hours.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Electroencephalography (EEG) is recorded continuously over hours, with relevant dynamics spanning timescales from milliseconds to hours.

进一步看，论文的核心做法或实验重点可以概括为：Most EEG foundation models nevertheless process fixed windows independently, limiting their ability to capture information encoded in long-timescale dynamics.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, retrieval
- 检索关键词命中：persistent memory
- 来源分类信息：cs.LG

## Abstract Snapshot
Electroencephalography (EEG) is recorded continuously over hours, with relevant dynamics spanning timescales from milliseconds to hours. Most EEG foundation models nevertheless process fixed windows independently, limiting their ability to capture information encoded in long-timescale dynamics. State-space architectures enable persistent recurrent processing, but long-range information remains implicitly compressed in recurrent states. We present NeurDuo-EEG, a causal EEG foundation model with channel-resolved persistent memory. NeurDuo-EEG introduces multi-timescale memory management with learned consolidation and selective retrieval, enabling persistent modelling of continuous EEG with fixed-size state. It is pre-trained on 3,955 hours of EEG from 17 public datasets using multichannel autoregressive prediction of discrete spectral codes. Across three short-window and two long-sequence downstream tasks, NeurDuo-EEG achieves the best performance on four of five benchmarks, including all three short-window tasks and seizure detection, where AUC-PR improves from $0.285$ to $0.471$ over the strongest non-NeurDuo baseline. NeurDuo-EEG also remains competitive on sleep staging and supports efficient streaming inference, with nearly constant per-chunk latency as the available history grows to one hour. Notably, the Small variant achieves this with only 4.7M backbone parameters. These results demonstrate the value of persistent, multi-timescale modelling for both long-sequence and short-window EEG analysis. Our code is available at https://github.com/YifaNNW/NeurDuo-EEG.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
