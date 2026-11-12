import os
import sys
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

key = os.environ.get("GROQ_API_KEY")

if key is None:
    sys.exit("GROQ_API_KEY environment variable is not set. please set it in your .env file or export it in your shell.")
    

client = Groq(api_key=key)

response = client.chat.completions.create(
    model = "openai/gpt-oss-20b",
    messages = [
        {"role": "user", "content": "Explain the importance of fast language models"}
        
    ],
)

print(response.choices[0].message.content)

print("prompt tokens:", response.usage.prompt_tokens)
print("completion tokens:", response.usage.completion_tokens)
print("total tokens:", response.usage.total_tokens)