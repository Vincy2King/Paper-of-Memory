# A Multimodal Framework for Dementia Detection via Linguistic and Acoustic Representation Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.25540v1
- Published: 2026-05-25
- Updated: 2026-05-25
- Authors: Loukas Ilias, Dimitris Askounis
- Tags: context
- Categories: cs.SD, cs.LG
- URL: http://arxiv.org/abs/2605.25540v1

## One-Sentence Summary
Alzheimer's disease (AD) is a progressive neurodegenerative disorder and the leading cause of dementia, affecting memory, reasoning, communication, and daily functioning.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Alzheimer's disease (AD) is a progressive neurodegenerative disorder and the leading cause of dementia, affecting memory, reasoning, communication, and daily functioning.

进一步看，论文的核心做法或实验重点可以概括为：Early diagnosis is particularly important, as timely intervention may help slow cognitive decline and improve patient care.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：memory reasoning
- 来源分类信息：cs.SD, cs.LG

## Abstract Snapshot
Alzheimer's disease (AD) is a progressive neurodegenerative disorder and the leading cause of dementia, affecting memory, reasoning, communication, and daily functioning. Early diagnosis is particularly important, as timely intervention may help slow cognitive decline and improve patient care. Recent studies have demonstrated that spontaneous speech contains valuable linguistic and acoustic biomarkers associated with dementia. However, existing approaches often rely on independently trained modality-specific models, feature concatenation strategies, ensemble methods, or attention-based fusion mechanisms that do not explicitly maximize the dependency between speech and transcript representations. In this work, we propose a multimodal deep learning framework for automatic dementia detection that jointly exploits speech and transcript information in an end-to-end trainable manner. Specifically, speech recordings are divided into 10-second segments and passed through a pre-trained HuBERT model to extract contextualized acoustic representations. To better capture informative temporal speech characteristics, attentive statistics pooling is employed to aggregate frame-level acoustic embeddings. For the textual modality, transcripts are encoded using a pre-trained BERT model, where the [CLS] token representation is used as the linguistic embedding. The acoustic and textual representations are subsequently combined using an attention-based Audio-Text Fusion (AT-Fusion) mechanism. In addition, we introduce a MINE objective to maximize the mutual information between modalities and improve multimodal representation alignment. The fused multimodal representation is finally used for dementia classification. Experiments conducted on the publicly available ADReSS Challenge and PROCESS-2 dataset demonstrate the effectiveness and robustness of the proposed approach for speech-based dementia assessment.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
