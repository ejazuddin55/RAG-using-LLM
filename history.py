
import streamlit as st
from together import Together

# Initialize Together.AI client with API key
client = Together(api_key="tgp_v1_XxOUZZ5oDOhquMy2v7kDWWhi9OGDAV22AvM7LQxUixM")  # 🔑 Replace with your actual API key

# Title of the app
st.title("Chat with DeepSeek AI 🤖 you can ask anything you want!!!")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):  # Display as 'user' or 'assistant'
        st.write(msg["content"])

# User input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Display user message in chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Call Together.AI API
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
            messages=st.session_state.messages,  # Send full chat history
        )
        reply = response.choices[0].message.content

    # Display AI response in chat
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
