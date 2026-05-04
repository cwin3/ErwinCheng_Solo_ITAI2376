import requests

def ask_ollama(prompt):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={"model":"llama3","prompt":prompt,"stream":False}
        )
        return res.json()["response"]
    except:
        return "⚠️ Ollama not running. Start it with: ollama run llama3"
