# Wontopos Tablet 2: Measuring Multilingual and Multimodal Memory Retrieval Without Lexical Matching

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.23920v1
- Published: 2026-08-24
- Updated: 2026-08-24
- Authors: Sunwoo Kim
- Tags: benchmark, long-term, retrieval
- Categories: cs.IR, cs.CL, cs.CV
- URL: http://arxiv.org/abs/2608.23920v1

## One-Sentence Summary
We measure tablet-2, a production long-term memory engine for language models, on the text benchmarks the field already uses and on cross-lingual retrieval of photographs stored...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：We measure tablet-2, a production long-term memory engine for language models, on the text benchmarks the field already uses and on cross-lingual retrieval of photographs stored with no text at all.

进一步看，论文的核心做法或实验重点可以概括为：Its retrieval path contains no lexical matching, no keyword scoring, and no language model of its own.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval
- 来源分类信息：cs.IR, cs.CL, cs.CV

## Abstract Snapshot
We measure tablet-2, a production long-term memory engine for language models, on the text benchmarks the field already uses and on cross-lingual retrieval of photographs stored with no text at all. Its retrieval path contains no lexical matching, no keyword scoring, and no language model of its own. On LongMemEval-S (500 questions) it scores 95.7% [93.4, 97.1]; on BEAM-1M (700 questions, 2.21M stored memories) 67.5% [64.8, 70.2]. Those are question-sampling intervals, not the run-to-run spread, which is an order of magnitude narrower. Most of the paper is about how little they mean alone. Holding engine, corpus, settings and judge fixed, changing only the reader moves LongMemEval-S by 2.0 points; changing only the re-ask budget moves BEAM-1M by 8.9. Neither is stated in the reports we compare against, and the second exceeds most gaps there, so we give that table as a placement and not a ranking. For the multimodal axis we run two controls. Against BM25, configured as strongly as we could, we reach 95.2% mean recall@5 over 70 store-and-query language cells where BM25 reaches 19.0% and is exactly zero in 54. On captionless photographs a lexical method has no document to score at all. Open dense baselines on 300 Crossmodal-3600 photographs in 14 languages show that density confers no language independence: one scores 91.0% on English and 4.7% on Russian from identical image vectors, and a multilingual variant collapses on Telugu and Swahili. Our spread across languages is 14.0 against their 27.5 and 27.7. Three results run against us and are reported at equal weight: low-resource languages degrade sharply (Swahili 53.0%, Telugu 64.0%), attaching captions lowers cross-lingual retrieval by 11.4 points, and one setting omitted into one stage of our own retrieval cost 37 points of Korean top-1 accuracy while leaving nine languages untouched.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
