import requests
import os

# ---------- QUERY ROUTER ----------
def is_complex_query(prompt: str) -> bool:
    prompt = prompt.lower()
    keywords = [
        "best", "compare", "recommend", "analysis",
        "which should", "pros and cons", "explain"
    ]
    return any(k in prompt for k in keywords)


# ---------- OPENAI ----------
def ask_openai(prompt):
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception:
        return None  # fail silently → fallback


# ---------- OLLAMA ----------
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
        return response.json().get("response")

    except Exception:
        return None  # fallback


# ---------- FINAL SAFE AI ----------
def ask_ollama(prompt):
    # 1. Try OpenAI for complex queries
    if is_complex_query(prompt):
        result = ask_openai(prompt)
        if result:
            return result

    # 2. Try Ollama (local only)
    result = ask_ollama_local(prompt)
    if result:
        return result

    # 3. Final fallback (ALWAYS WORKS)
    return f"""
🤖 AI Insight (Fallback)

Query: "{prompt}"

• Compare price, mileage, and condition  
• Avoid deals that seem too cheap  
• Check vehicle history before buying  
• Consider long-term maintenance costs  
"""
