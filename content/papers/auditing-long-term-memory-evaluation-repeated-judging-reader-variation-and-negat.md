# Auditing Long-Term Memory Evaluation: Repeated Judging, Reader Variation, and Negative Controls

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.38021v2
- Published: 2026-09-29
- Updated: 2026-10-02
- Authors: Christopher J. Chanhnourack
- Tags: long-term, retrieval
- Categories: cs.CL, cs.AI, cs.IR
- URL: http://arxiv.org/abs/2609.38021v2

## One-Sentence Summary
This report audits evaluation of a long-term-memory retrieval chain on the 500 LongMemEval-S development questions.

## Introduction
这篇论文被纳入仓库，是因为它和 `long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：This report audits evaluation of a long-term-memory retrieval chain on the 500 LongMemEval-S development questions.

进一步看，论文的核心做法或实验重点可以概括为：Its strongest historical reader lane scores 479 and 475 under an adapted GPT-4o rubric; re-judging the same pass-1 answers changes three labels and yields 478.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：long-term, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.CL, cs.AI, cs.IR

## Abstract Snapshot
This report audits evaluation of a long-term-memory retrieval chain on the 500 LongMemEval-S development questions. Its strongest historical reader lane scores 479 and 475 under an adapted GPT-4o rubric; re-judging the same pass-1 answers changes three labels and yields 478. Fixed-answer knowledge-update re-scoring gives 70/72 under the upstream template and 69/72 under the modified template. Reader lanes span 93 to 479 on fixed packets; paired tests between the two strongest historical lanes establish neither superiority nor equivalence. A different-family reader, configured without client tools or operator files, scores 474, 1.0 percentage point below the headline pass (paired 95% interval [-3.0,+1.0]). Live reader request bodies were not retained. With the same requested reader label, route and judge snapshot, the full package scores 474 versus 454 for baseline sessions, a difference of +4.0 percentage points [95% interval +2.2,+6.0]. Eighteen of the 23 gains, and no losses, occur where baseline packets lacked listed evidence; this post-hoc split does not identify a component effect. In recovered LoCoMo data, token-F1 gains do not survive answer-line extraction. A negative control rejects a verifier that repairs three wrong drafts but breaks eleven correct ones. All questions were used to develop the components; no untouched holdout was evaluated. These findings do not establish a new leaderboard leader or transferable memory advantage. The A/D comparison has one pass per arm, including six reused identical-prompt outcomes, with no pinned reader snapshot; B/C and repeats remain unrun. Original headline requests cannot be reconstructed and stages 1--4 remain closed. Released artifacts support packet inspection and saved-verdict recounting and re-scoring; they do not reconstruct the method.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
