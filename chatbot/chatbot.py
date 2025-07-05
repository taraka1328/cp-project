# chatbot/chatbot.py
import requests
import streamlit as st

API_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_response(user_message):
    try:
        # Check if API key is available
        if 'groq_api_key' not in st.secrets:
            return "❌ Error: Groq API key not configured. Please add your API key to Streamlit secrets."
        
        headers = {
            "Authorization": f"Bearer {st.secrets['groq_api_key']}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama3-8b-8192",  # You can change this to llama3-70b if needed
            "messages": [
                {"role": "system", "content": "You are a helpful farming assistant. Answer questions about crops, weather, and plant diseases."},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code != 200:
            return f"❌ Error: API request failed with status {response.status_code}. Please check your API key."
        
        result = response.json()
        
        # Check if the response has the expected structure
        if "choices" not in result or len(result["choices"]) == 0:
            return "❌ Error: Unexpected API response format."
        
        return result["choices"][0]["message"]["content"]
        
    except KeyError as e:
        return f"❌ Error: Missing configuration - {str(e)}. Please check your Streamlit secrets."
    except requests.exceptions.RequestException as e:
        return f"❌ Error: Network request failed - {str(e)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"
