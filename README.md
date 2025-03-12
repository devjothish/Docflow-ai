
# **📚 DocFlow AI - AI-Powered Multi-PDF Chatbot**  

### **🚀 A Smarter Way to Search & Interact with Your PDFs**  

DocFlow AI allows you to **upload multiple PDFs**, ask questions, and get **AI-powered responses** with **document references**. No more manual searches—just **upload, ask, and get answers instantly!**  

---

## **📄 What is DocFlow AI?**  

### ✅ **Features:**  
✔ Upload multiple PDFs at once  
✔ Ask questions and get answers based on document content  
✔ Retrieve information from multiple files simultaneously  
✔ See **document names and page numbers** for referenced answers  
✔ Save time by **avoiding manual keyword searches**  

---

## **🔍 Why Did I Build DocFlow AI?**  
I’ve spent hours searching through **long PDFs**—lecture notes, research papers, reports—just to find **small pieces of important information**.  

I realized that a **simple AI-powered assistant** could:  
✅ Help **students** quickly pull facts from textbooks  
✅ Assist **researchers** in comparing studies  
✅ Support **professionals** in analyzing legal, financial, or technical reports  

That’s why I built **DocFlow AI**—to **improve productivity, reduce manual work, and offer a smarter way to interact with documents.**  

---

## **🛠️ How Does DocFlow AI Work?**  

### **📌 Step 1: PDF Upload & Processing**  
📂 Upload PDFs through the **chat interface**.  
📝 **PyPDF2** extracts text from each document, even handling **encrypted files**.  

### **📌 Step 2: Data Indexing with FAISS**  
🧩 Text is split into smaller **chunks** using **LangChain’s Text Splitter**.  
🔍 Each chunk is converted into **vector embeddings** using **Google Gemini AI** and stored in a **FAISS index** for **fast retrieval**.  

### **📌 Step 3: AI-Powered Q&A**  
❓ When you ask a question, **DocFlow AI** searches the FAISS index to find the most relevant text.  
🤖 The retrieved content is passed to **Google Gemini AI**, which generates a **detailed response** with the **document name and page number**.  

### **📌 Step 4: Displaying Results**  
✅ AI’s answers are **displayed in the chat interface** with **source references** for better traceability.  

---

## **🆚 Why Use DocFlow AI Instead of ChatGPT/Gemini File Uploads?**  

✅ **Files Stay Available** – No need to re-upload PDFs; **DocFlow AI keeps them indexed** for easy access.  
✅ **Multi-PDF Search** – Query **multiple PDFs at once**, unlike ChatGPT or Gemini, which only work **per session**.  
✅ **Faster Retrieval** – Indexed files allow **instant search results** without repeated reprocessing.  
✅ **Source Referencing** – Responses **clearly state the PDF name and page number** for better traceability.  
✅ **More Control & Privacy** – Files **stay local or on your private server**, unlike ChatGPT/Gemini, which **upload them externally**.  

---

## **👨‍💻 How Can DocFlow AI Help You?**  

📖 **Students & Researchers** → Quickly extract key points from **textbooks, papers, and notes**.  
💼 **Developers & Engineers** → Find **technical explanations** directly from **manuals or API docs**.  
⚖️ **Legal & Compliance Teams** → Identify specific **clauses or references** across multiple legal documents.  
📝 **Writers & Content Creators** → Summarize **ideas from multiple sources**.  

Whether you're **preparing for exams, analyzing contracts, or working with research papers**, **DocFlow AI** makes document interaction **faster and easier**.  

---

## **💻 Installation & Setup**  
Want to try **DocFlow AI** yourself? Follow these steps:  

### **🔹 Requirements**  
- **Python 3.9+**  
- `streamlit`  
- `langchain`  
- `faiss-cpu`  
- `google-generativeai`  
- `PyPDF2`  
- `python-dotenv`  

### **🔹 Installation Steps**  
```bash
# Clone the repository
git clone https://github.com/devjothish/Docflow-ai.git
cd docflow-ai

# Install dependencies
pip install -r requirements.txt

# Set up API Key by creating a .env file in the root directory
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# Run the app
streamlit run app.py
🚀 How to Use DocFlow AI
1️⃣ Upload PDFs via the chat interface.
2️⃣ Click "Process PDFs" to create a searchable index.
3️⃣ Type a question, and DocFlow AI will retrieve relevant answers.
4️⃣ Each response shows the PDF name and page number for easy reference.

📢 Get Involved
If you find DocFlow AI useful, here’s how you can contribute:

🔗 GitHub Repository: DocFlow AI Repo
💡 Got feedback or feature ideas? Let me know!

👨‍💻 About the Creator
I built DocFlow AI because I wanted to solve a real problem—and I’m excited to share this through the AI Builders Series. Stay tuned for more AI projects!

Happy Building! 🚀
Jothiswaran Arumugam 👨‍💻
