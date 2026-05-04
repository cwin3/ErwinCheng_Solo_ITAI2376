import requests

def ask_ollama(prompt):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={"model":"llama3","prompt":prompt,"stream":False},
            timeout=5
        )
        return res.json()["response"]
    except:
        return "⚠️ AI unavailable on cloud. Run locally with Ollama."
