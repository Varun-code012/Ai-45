import tiktoken

enc = tiktoken.get_encoding("o200k_base")

def show_tokens(text):
    ids = enc.encode(text)
    print(f"text: {text!r}")
    print(f"characters: {len(text)}   tokens: {len(ids)}")
    for tok_id in ids:
        piece = enc.decode_single_token_bytes(tok_id)
        print("  ", tok_id, piece)
    print()

samples = ["Hello", "hello", " hello"]
for s in samples:
    show_tokens(s)