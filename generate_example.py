import ollama

res = ollama.generate(
    model="llama3",
    prompt="What is Python used for?",
)

print(res.response)