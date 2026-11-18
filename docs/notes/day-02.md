# Day 2: Tokens and tokenization

- A tokenizer turns text into integer IDs. BPE starts from bytes and repeatedly merges the most frequent adjacent pair; the vocabulary is fixed after training (gpt-oss: ~200k entries).
- Subwords balance vocabulary size against sequence length, and any text can be encoded because it starts from bytes.
- The model receives IDs, never letters. This is why letter-level tasks (counting r's in "strawberry" = st|raw|berry) are hard.
- A leading space is part of the token: "hello" = 24912, " hello" = 40617. The same word can even split differently with or without a space.
- My samples, in characters per token: English ~4.35, code 2.7, numbers 2.5, a date 1.67. Numbers are chopped arbitrarily: 1234567890 = 123|456|789|0.
- Same meaning, "We are learning Kannada": English 5 tokens, Kannada 7 (~1.4x) with o200k_base. One sentence pair, not a general rule.
- Control one variable at a time. My first comparison (8 vs 5) included a period; removing it gave 7 vs 5.
- Counts depend on the tokenizer, so they don't transfer between models.
- Predict before you run, and record real numbers only.
- Windows: `pip freeze > file` can write UTF-16, which Git treats as binary. Check with Get-Content, or use `| Out-File -Encoding ascii`.
- Git: if you edit a file after `git add`, add it again; check `git status` before committing.