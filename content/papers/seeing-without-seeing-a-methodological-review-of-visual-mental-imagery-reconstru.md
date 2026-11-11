# Seeing Without Seeing: A Methodological Review of Visual Mental Imagery Reconstruction from Brain Activity

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.13691v1
- Published: 2026-11-10
- Updated: 2026-11-10
- Authors: Shiyi Zhang, Dong Liang, Yihang Zhou
- Tags: benchmark
- Categories: cs.HC
- URL: http://arxiv.org/abs/2611.13691v1

## One-Sentence Summary
Reconstructing visual mental imagery from brain activity differs from reconstructing perceived images.

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Reconstructing visual mental imagery from brain activity differs from reconstructing perceived images.

进一步看，论文的核心做法或实验重点可以概括为：Imagery is generated top-down, its signal is weak, and the imagined content is never observed, so decoders are trained and scored against a proxy such as a cue or a seen exemplar.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark
- 检索关键词命中：working memory
- 来源分类信息：cs.HC

## Abstract Snapshot
Reconstructing visual mental imagery from brain activity differs from reconstructing perceived images. Imagery is generated top-down, its signal is weak, and the imagined content is never observed, so decoders are trained and scored against a proxy such as a cue or a seen exemplar. This criterion-guided methodological review of mainly non-invasive studies (fMRI, EEG, MEG) is narrative rather than systematic. We organise the field into a two-stage pipeline, two design axes and four method families, and formalise target-free evaluation, in which the proxy gap is a systematic bias rather than noise. A two-dimensional admissibility criterion crosses trial-level separability from working-memory maintenance with the memory source of the imagined content. Among the studies reviewed, every image-scored reconstruction concerns a recalled exemplar, none builds a scorable target for concept-generated content, and all come from fMRI, consistent with missing image-level targets in electrophysiological data. Published values for five decoders, compared under a common human forced-choice framing, show seen-to-imagined drops of 5.9 to 26.1 percentage points and a change in method ordering. We treat this as a diagnostic signal, not a controlled benchmark result, and specify a within-subject test for an altered neural code. Beyond this synthesis, we make two proposals. First, because frozen generative priors can produce photorealistic images weakly tied to neural signals, we combine existing null-signal controls into a normalised neural dependence with a within-category null, an unvalidated diagnostic quantity. Second, we propose a candidate ten-item reporting checklist with illustrative pass criteria. In an exploratory application to ten studies, none reports all items in a fully checkable form; this describes reporting practice, not study quality.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
