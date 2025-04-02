

# **📄 RAG-Based Chatbot with Your PDF 🤖**  
A **Retrieval-Augmented Generation (RAG) chatbot** powered by **DeepSeek AI**, **FAISS**, and **Together.AI**, built with **Streamlit**. This chatbot allows users to **upload a PDF document**, and then ask AI-powered questions based on the document’s content.  

---

## **🌟 Project Overview**  
This project combines **LLM-based text generation** with **semantic search** by embedding PDF content into a **vector database (FAISS)**. The chatbot first retrieves the most relevant text from the document before generating a response using **DeepSeek AI's Llama-70B model** via **Together.AI**.  

### ✅ **Key Features:**  
- **📂 Upload & Process PDFs** – Extract text from your document and store it for chat.  
- **🔍 AI-Powered Search** – Uses **FAISS vector database** to find the most relevant text chunks.  
- **🗨️ Context-Aware Responses** – Answers questions based on the **retrieved PDF content**.  
- **🚀 Fast & Scalable** – Uses **sentence-transformers embeddings** for quick search.  
- **🎨 Streamlit UI** – Clean and simple chat interface.  

---

## **🛠️ Tech Stack**  
- **Python** – Core programming language  
- **Streamlit** – UI for interaction  
- **Together.AI** – API for AI-powered responses  
- **DeepSeek AI (Llama-70B)** – Language model for response generation  
- **FAISS** – Efficient vector database for similarity search  
- **HuggingFace Embeddings** – `all-MiniLM-L6-v2` for semantic search  
- **PyPDF2** – Extract text from PDFs  

---

## **📸 Screenshots**  
### **1️⃣ Chat Interface**  
*(Add a screenshot of your Streamlit chatbot UI here)*  
### **2️⃣ PDF Upload & Processing**  
*(Another screenshot showing PDF upload and processing status)*  

---

## **📌 How It Works**  
1️⃣ **User uploads a PDF file**, which gets processed and converted into text.  
2️⃣ **Text is split into smaller chunks** for efficient retrieval.  
3️⃣ **Chunks are embedded** using **HuggingFace embeddings** and stored in **FAISS**.  
4️⃣ **User asks a question** related to the document.  
5️⃣ **Relevant text is retrieved** from FAISS using **similarity search**.  
6️⃣ **DeepSeek AI generates a response** based on the retrieved content.  
7️⃣ **The response is displayed** in the chat interface.  

---

## **📥 Installation & Setup**  
Follow these steps to set up and run the chatbot on your local machine.  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/ejazuddin55/RAG-using-LLM.git
cd RAG-using-LLM
```

### **2️⃣ Install Dependencies**  
Make sure you have **Python 3.8+** installed, then run:  
```bash
pip install streamlit together pymupdf pdfplumber faiss-cpu langchain langchain-community
```

### **3️⃣ Configure the API Key**  
Replace `your_api_key_here` with your **Together.AI API key** in `app.py`:  
```python
client = Together(api_key="your_api_key_here")
```
**(🚨 Never expose your API key publicly!)**

### **4️⃣ Run the Streamlit App**  
```bash
streamlit run app.py
```
The app will open in your **browser**.

---

## **🎯 Usage Instructions**  
1️⃣ **Open the app** in your browser after running `streamlit run app.py`.  
2️⃣ **Upload a PDF document** via the upload button.  
3️⃣ **Wait for the processing to complete** (text extraction, chunking, embedding).  
4️⃣ **Ask questions** related to the document.  
5️⃣ **Chatbot will provide accurate answers** based on retrieved content.  

---

## **🔧 Troubleshooting**  
- **Invalid API Key?** Ensure your Together.AI API key is correct.  
- **Missing FAISS?** Install it using `pip install faiss-cpu`.  
- **Slow response?** Large PDFs take longer to process; try a smaller document.  

---

## **🚀 Future Improvements**  
🔹 Support for **multiple document types (TXT, DOCX, CSV)**  
🔹 Implement **long-term chat history storage** (e.g., database)  
🔹 Improve **search efficiency** using **ChromaDB**  
🔹 Add **multi-document support**  

---

## **🤝 Contributing**  
Want to improve this project? Follow these steps:  
1. **Fork this repository**  
2. **Make your changes**  
3. **Submit a pull request**  

---
