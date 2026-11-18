# Ai-45

## Day 1

My script loads my Groq API key from a `.env` file, which authenticates the request, and sends a model name plus a `messages` list (each item has a `role` and `content`) to Groq's API. The model splits the text into tokens, then predicts one token at a time, appending each to the input, until it emits a stop token, so the reply is a plausible continuation rather than a looked-up fact. The response comes back as an object where the reply text is at `response.choices[0].message.content` and the token counts are in `response.usage`; in my first test, a short prompt used 78 prompt tokens and produced 1,737 completion tokens.

## Day 2

- Learned: BPE builds a fixed vocabulary of subword chunks; the model works on token IDs; spaces are part of a token; cost per character varies with content; counts are tokenizer-specific
- Built: tokenize_lab.py, docs/experiments/day-02-tokens.md (11+ rows, predictions vs results), tiktoken added to requirements.txt
- Can explain independently: why " hello" and "hello" differ; how I fixed my Kannada comparison (period inflated it from 7 to 8)
- Still unclear: why other languages cost more (bytes vs how frequent the text was in the tokenizer's training data); why "strawberry" trips models; Day 1 Q3/Q4
- Not done: loop refactor of tokenize_lab.py; token_vs_api.py overhead test (stretch)
- Revisit: all open questions at the end of Day 3
- Next: Day 3, temperature and sampling