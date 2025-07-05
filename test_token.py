import requests

headers = {
    "Authorization": "YOUR_HUGGING_FACE_TOKEN_HERE"
}
API_URL = "https://api-inference.huggingface.co/models/OpenChat/openchat-3.5-1210"
data = {"inputs": "Hello, what crops grow best in black soil?"}

response = requests.post(API_URL, headers=headers, json=data)
print("Status Code:", response.status_code)
print("Response:", response.text)
