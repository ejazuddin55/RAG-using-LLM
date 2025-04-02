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
st.title("📄 RAG Chatbot with Your PDF 🤖")

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# ✅ Process PDF only if it's new
if uploaded_file and "pdf_text" not in st.session_state:
    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        pdf_path = temp_pdf.name

    # Extract text from PDF
    def extract_text_from_pdf(pdf_path):
        pdf_reader = PdfReader(pdf_path)
        text = "\n".join([page.extract_text() or "" for page in pdf_reader.pages])
        return text

    st.session_state.pdf_text = extract_text_from_pdf(pdf_path)  # Store in session state

    # Chunk the text for better search
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(st.session_state.pdf_text)

    # ✅ Load Together-compatible embeddings
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  
        st.success("✅ Embeddings Loaded Successfully!")
    except Exception as e:
        st.error(f"❌ Error loading embeddings: {str(e)}")
        st.stop()

    # Embed text chunks & store in FAISS
    st.session_state.vector_db = FAISS.from_texts(chunks, embeddings)

    st.success("✅ PDF Uploaded & Processed!")

# ✅ Ensure everything runs only if PDF is processed
if "pdf_text" in st.session_state:
    # Initialize chat history only once
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # User input
    prompt = st.chat_input("Ask something about your PDF...")

    if prompt:
        # Retrieve relevant chunks
        docs = st.session_state.vector_db.similarity_search(prompt, k=3)  # Get top 3 matches
        retrieved_text = "\n".join([doc.page_content for doc in docs])

        # Call Together.AI model
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
                    messages=[
                        {"role": "system", "content": "Use the provided text to answer questions concisely (5-6 sentences max)."},
                        {"role": "user", "content": f"Context:\n{retrieved_text}\n\nQuestion: {prompt}"}
                    ]
                )
                reply = response.choices[0].message.content.strip()
                reply = " ".join(reply.split()[:60])  # Limit response to ~5-6 sentences
            except Exception as e:
                reply = "⚠️ Sorry, an error occurred while generating a response."
                st.error(f"Error: {e}")

        # Append user input & response to session state
        if reply:
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": reply})

        # Refresh UI after adding new message
        st.rerun()

    # ✅ Display chat history ONCE at the end
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
else:
    st.warning("⚠️ Please upload a PDF file to start chatting.")
