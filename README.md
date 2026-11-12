# Ai-45

## Day 1

My script loads my Groq API key from a `.env` file, which authenticates the request, and sends a model name plus a `messages` list (each item has a `role` and `content`) to Groq's API. The model splits the text into tokens, then predicts one token at a time, appending each to the input, until it emits a stop token, so the reply is a plausible continuation rather than a looked-up fact. The response comes back as an object where the reply text is at `response.choices[0].message.content` and the token counts are in `response.usage`; in my first test, a short prompt used 78 prompt tokens and produced 1,737 completion tokens.