# Day 1: First LLM call

- An LLM predicts one token at a time: text → tokens → a score for every token in its vocabulary → probabilities → one token chosen → appended → repeat until a stop token.
- It generates plausible continuations, not looked-up facts. That's where hallucination comes from.
- `completion_tokens` = how many times the predict-and-append loop ran. Reasoning tokens (444 of my 1,737) are included in it.
- The API is stateless: it remembers nothing between calls. To give it memory, send earlier messages in the `messages` list (roles: system, user, assistant).
- Every request carries about 70 tokens of hidden overhead. "Hi" cost 72 prompt tokens, my 8-word prompt cost 78; the 6-token difference is the real text.
- Response map: reply = `response.choices[0].message.content`; counts = `response.usage`; `finish_reason` is `stop` (finished) or `length` (cut off).
- API key goes in `.env`; `.env` goes in `.gitignore`; `.env.example` (placeholder only) is committed. Git history is permanent, so a leaked key must be revoked, not just deleted.
- A venv gives each project its own packages. Save them with `pip freeze > requirements.txt`.
- `load_dotenv()` won't override a variable already set in the terminal. Check `Test-Path Env:GROQ_API_KEY` first when `.env` seems ignored.
- Read tracebacks bottom-up. A 404 `model_not_found` means the model was retired. Docs examples go stale, so check the live model list.
- Git habit: `git add` named files, run `git status` before committing.