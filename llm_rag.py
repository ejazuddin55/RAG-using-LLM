import streamlit as st
from together import Together
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

import tempfile
from PyPDF2 import PdfReader

# 🔑 Set Together.AI API Key
TOGETHER_API_KEY = "tgp_v1_XxOUZZ5oDOhquMy2v7kDWWhi9OGDAV22AvM7LQxUixM"  # Replace with actual key
client = Together(api_key=TOGETHER_API_KEY)

# Streamlit App Title
st.title("RAG Chatbot with Your PDF 🤖📄")

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        pdf_path = temp_pdf.name

    # Extract text from PDF
    def extract_text_from_pdf(pdf_path):
        pdf_reader = PdfReader(pdf_path)
        text = "\n".join([page.extract_text() or "" for page in pdf_reader.pages])
        return text

    pdf_text = extract_text_from_pdf(pdf_path)

    # Chunk the text for better search
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(pdf_text)

    # ✅ Use Together-compatible embeddings
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # More stable model
        st.success("✅ Embeddings Loaded Successfully!")
    except Exception as e:
        st.error(f"❌ Error loading embeddings: {str(e)}")
        st.stop()

    # Embed text chunks & store in FAISS
    vector_db = FAISS.from_texts(chunks, embeddings)

    st.success("✅ PDF Uploaded & Processed!")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # User input should be inside the uploaded_file block
    prompt = st.chat_input("Ask something about your PDF...")

    if prompt:
        # Retrieve relevant chunks
        docs = vector_db.similarity_search(prompt, k=3)  # Get top 3 matches
        retrieved_text = "\n".join([doc.page_content for doc in docs])

        # Call Together.AI model
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
                messages=[
                    {"role": "system", "content": "Use the provided text to answer questions accurately."},
                    {"role": "user", "content": f"Context:\n{retrieved_text}\n\nQuestion: {prompt}"}
                ]
            )
            reply = response.choices[0].message.content

        # Append user input & response to session state
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": reply})

        # Refresh UI
        st.rerun()

    # Display updated chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

else:
    st.warning("⚠️ Please upload a PDF file to start chatting.")
