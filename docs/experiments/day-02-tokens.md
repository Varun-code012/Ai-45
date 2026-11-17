# Day 2: Token experiments

**Encoding:** `o200k_base` (via `tiktoken`, version: `<0.14.0>`)
**Script:** `week-01-llm-fundamentals/tokenize_lab.py`

| Text | Characters | Tokens | Chars/token | My prediction |
|---|---|---|---|---|
| `"Hello"` | 5 | 1 | 5.0 | 1 |
| `"hello"` | 5 | 1 | 5.0 | 1 |
| `" hello"` | 6 | 1 | 6.0 | 1 |
| `"Paris"` | 5 | 1 | 5.0 | 1 |
| `" Paris"` | 6 | 1 | 6.0 | 1 |
| English sentence (see below) | 135 | 31 | 4.35 | 36 |
| `"supercalifragilisticexpialidocious"` | 34 | 10 | 3.4 | 12 |
| `"1234567890"` | 10 | 4 | 2.5 | 10 |
| `"2026-11-13"` | 10 | 6 | 1.67 | 7 |
| `"def add(a, b): return a + b"` | 27 | 10 | 2.7 | 12 |
| Kannada sentence (see below) | 27 | 8 | 3.4 | none |
| `"strawberry"` | 10 | 3 | 3.3 | 3 |
| `"We are learning kannada"` (English, same meaning) | 23 | 5 | 4.6 | 6 |
| Kannada, leading space, no period (`" ನಾವು ಕನ್ನಡ ಕಲಿಯುತ್ತಿದ್ದೇವೆ"`) | 27 | 6 | 4.5 | none |
| Kannada, leading space, with period | 28 | 7 | 4.0 | none |
| Kannada, no leading space, no period (`"ನಾವು ಕನ್ನಡ ಕಲಿಯುತ್ತಿದ್ದೇವೆ"`) | 26 | 7 | 3.7 |none |

**English sentence used:** "It's so nice when you have someone who can sit with and not have to talk to them, and you can just be together. It's a beautiful thing."
**Kannada sentence used:** ನಾವು ಕನ್ನಡ ಕಲಿಯುತ್ತಿದ್ದೇವೆ.

## What the table shows

For each text I recorded the character count, the token count, and characters per token using `o200k_base`, and I wrote my prediction before running each test (I didn't predict the Kannada sentence). My predictions matched exactly on 5 rows and were too high on the other 5, and I never guessed too low, so the tokenizer merges text into bigger chunks than I expected; the biggest miss was `1234567890`, where I guessed 10 and got 4. What surprised me most was that the Kannada sentence is split into pieces at all: its 27 characters became 8 tokens, and the byte output showed that each token holds several bytes of Kannada text, so code, numbers, and other languages are split very differently from plain English.

