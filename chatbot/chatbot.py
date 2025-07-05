# chatbot/chatbot.py
import requests
import streamlit as st

API_URL = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {st.secrets['groq_api_key']}",
    "Content-Type": "application/json"
}

def generate_response(user_message):
    payload = {
        "model": "llama3-8b-8192",  # You can change this to llama3-70b if needed
        "messages": [
            {"role": "system", "content": "You are a helpful farming assistant. Answer questions about crops, weather, and plant diseases."},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    return result["choices"][0]["message"]["content"]
