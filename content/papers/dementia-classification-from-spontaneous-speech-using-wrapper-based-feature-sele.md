# Dementia classification from spontaneous speech using wrapper-based feature selection

- Source: arXiv
- Venue: N/A
- Paper ID: 2502.03484v2
- Published: 2025-02-04
- Updated: 2026-04-23
- Authors: Marko Niemelä, Mikaela von Bonsdorff, Sami Äyrämö, Tommi Kärkkäinen
- Tags: memory
- Categories: eess.AS, cs.LG, cs.SD
- URL: http://arxiv.org/abs/2502.03484v2

## One-Sentence Summary
Dementia encompasses a group of syndromes that impair cognitive functions such as memory, reasoning, and the ability to perform daily activities.

## Introduction
这篇论文被纳入仓库，是因为它和 `memory research` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Dementia encompasses a group of syndromes that impair cognitive functions such as memory, reasoning, and the ability to perform daily activities.

进一步看，论文的核心做法或实验重点可以概括为：As populations globally age, over 10 million new dementia diagnoses are reported annually.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 检索关键词命中：memory reasoning
- 来源分类信息：eess.AS, cs.LG, cs.SD

## Abstract Snapshot
Dementia encompasses a group of syndromes that impair cognitive functions such as memory, reasoning, and the ability to perform daily activities. As populations globally age, over 10 million new dementia diagnoses are reported annually. Currently, clinical diagnosis of dementia remains challenging due to overlapping symptoms, the need to exclude alternative conditions and the requirement for a comprehensive clinical evaluation and cognitive assessment. This underscores the growing need to develop feasible and accurate methods for detecting cognitive deficiencies. Recent advances in machine learning have highlighted spontaneous speech as a promising noninvasive, cost-effective, and scalable biomarker for dementia detection. In this study, spontaneous speech recordings from the ADReSS and Pitt Corpus datasets are analyzed, consisting of picture description tasks performed by cognitively healthy individuals and people with Alzheimer's disease. Unlike prior approaches that focus solely on speech-active segments, acoustic features are extracted from entire recordings using the openSMILE toolkit. This representation reduces the number of feature vectors and improves computational efficiency without compromising classification performance. Classification models with classifier-based wrapper feature selection are employed to estimate feature importance and identify diagnostically relevant acoustic characteristics. Among the evaluated models, the Extreme Minimal Learning Machine achieved competitive classification accuracy with substantially lower computational cost, reflecting an inherent property of the model formulation and learning procedure. Overall, the results demonstrate that the proposed framework is computationally efficient, interpretable, and well suited as a supportive tool for speech-based dementia assessment.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
