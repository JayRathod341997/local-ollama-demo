ollama serve
ollama create genAI-jayrathod -f .\modelfile
ollama list
ollama run genAI-jayrathod



CTRL + D => for exit

Postman 

http://localhost:11434/api/generate -> POST

{
    "model": "llama3",
    "prompt": "What is the capital of India?",
    "temperature": 0.9,
    "stream":false
}
