import ollama


res = ollama.chat(
    model="llama3",
    messages=[
        # {"role": "user", "content": "What is Python?"},
        # {"role": "assistant", "content": "Python is a programming language."},
        {"role": "user", "content": "What is Python used for?"}
    ],
    stream=True
)
# print(res['message']['content'])
for chunk in res:
    print(chunk['message']['content'], end="",flush=True)

