import requests

# Together.AI API URL
API_URL = "https://api.together.xyz/v1/chat/completions"

# Replace with your actual API key from Together.AI
API_KEY = "tgp_v1_XxOUZZ5oDOhquMy2v7kDWWhi9OGDAV22AvM7LQxUixM"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def query_deepseek(prompt):
    payload = {
        "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",  # ✅ Updated model name
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 200
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example Usage
user_input = "Tell me about DeepSeek AI"
response = query_deepseek(user_input)
print(response)
