import streamlit as st
import requests

# Together.AI API URL
API_URL = "https://api.together.xyz/v1/chat/completions"
API_KEY = "tgp_v1_XxOUZZ5oDOhquMy2v7kDWWhi9OGDAV22AvM7LQxUixM"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def query_deepseek_api(prompt):
    payload = {
        "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",  # Correct model name
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 200
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

st.title("Chat with DeepSeek AI 🤖")

prompt = st.chat_input("What's on your mind?")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.spinner("Thinking..."):
        reply = query_deepseek_api(prompt)
    
    with st.chat_message("assistant"):
        st.write(reply)
