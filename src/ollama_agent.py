import requests
import os

# ---------- SIMPLE ROUTER ----------
def is_complex_query(prompt: str) -> bool:
    prompt = prompt.lower()

    keywords = [
        "best", "compare", "recommend", "analysis",
        "which should", "pros and cons", "explain"
    ]

    return any(k in prompt for k in keywords)


# ---------- OLLAMA (LOCAL) ----------
def ask_ollama_local(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=5
        )
        return response.json().get("response", "Ollama error")
    except:
        return "⚠️ Ollama not available. Using fallback response."


# ---------- OPENAI (CLOUD) ----------
def ask_openai(prompt):
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except:
        return "⚠️ OpenAI not configured. Falling back to local AI."


# ---------- MAIN FUNCTION ----------
def ask_ollama(prompt):
    if is_complex_query(prompt):
        result = ask_openai(prompt)

        # fallback if OpenAI fails
        if "⚠️" in result:
            return ask_ollama_local(prompt)

        return result

    else:
        return ask_ollama_local(prompt)
