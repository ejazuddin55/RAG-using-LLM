import streamlit as st
from together import Together 
client = Together(api_key="tgp_v1_XxOUZZ5oDOhquMy2v7kDWWhi9OGDAV22AvM7LQxUixM")  # 🔑 Replace with your actual API key
st.title("Chat with AI 🤖")
if "messages" not in st.session_state:
    st.session_state.messages=[]


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt =st.chat_input("Whats is in your mind")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)

with st.spinner("Thinking..."):
    response=client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
        messages=st.session_state.messages,
    )
    reply=response.choices[0].message.content

st.session_state.messages.append({"role":"assistant","content":reply})
with st.chat_message("assistant"):
    st.write(reply)