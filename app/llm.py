
import requests

def get_llm_response(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "I'm having trouble responding right now. Please try again later."
