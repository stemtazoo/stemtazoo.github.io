# Shared Practice Question Answer Disclosure Rules

Applies to FE, GK, DS, and SG when an article gives readers a **question to solve before checking its answer**. Read this alongside the relevant theme-specific article guides.

## Reader flow

1. Show the full question, assumptions, and choices before the answer.
2. Keep the answer, correct option, and question-specific explanation **hidden by default**.
3. Let readers deliberately reveal the answer using native HTML `<details markdown="1">` and a descriptive `<summary>`. Do not add the `open` attribute.
4. Preserve answer reasoning, including why distractors are incorrect. A reveal must work without JavaScript and remain keyboard accessible.
5. Do not expose the correct option elsewhere immediately beside the question (e.g. labels, headings, captions, tables, or preview text). General explanations of the underlying concept earlier in the article may remain visible.

## Recommended Markdown

```md
## 確認問題

次のうち、適切なものはどれか。

- ア：...
- イ：...

<details markdown="1">
<summary>正解と解説を見る（タップして開く）</summary>

**正解：イ**

- ア：...
- イ：...

</details>
```

Keep blank lines around the HTML and Markdown content for Jekyll compatibility. Check the rendered output so Markdown inside the disclosure is formatted properly.

## Do not hide explanatory examples mechanically

A worked calculation, explanatory code trace, formula derivation, reference table, or demonstration intended to **teach a procedure** can show intermediate and final results immediately. Only apply disclosure when the reader is explicitly invited to solve a question first. An interactive simulation may use a different prediction-and-feedback interface if it does not reveal the answer before the learner acts and works with the stated accessibility and fallback requirements.

## Verification

- For new or edited questions, inspect initial display, opening/closing behavior, mobile layout, keyboard operation, and the complete answer explanation.
- Run `python -m unittest discover -s tests -p 'test_practice_answer_disclosure.py' -v` and `python scripts/audit_practice_answer_disclosure.py --fail-on-exposure`.
- The GitHub Actions `Practice answer disclosure audit` checks FE/GK/DS/SG and uploads its JSON results.
- The detector recognizes common textual answer labels; **zero findings is not proof** that all question formats or rendered UI are correct. Review new wording/patterns and extend regression cases when needed.
- Avoid hiding entire explanatory sections merely to satisfy a pattern-based checker.

SG-specific restrictions on when confirmation questions may be added, placement, and question quality remain in `sg-example-question-rules.md`.
