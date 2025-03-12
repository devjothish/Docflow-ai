# Docflow-ai

📄 What is DocFlow AI?
DocFlow AI is a tool that lets you:

Upload multiple PDFs at once.
Ask questions and get answers based on the document content.
Retrieve information from multiple files simultaneously.
See exact document names and page numbers for referenced answers.
Save time by avoiding manual keyword searches

Why Did I Build DocFlow AI?
As a student, developer, and professional, I’ve spent hours digging through long PDFs — lecture notes, research papers, reports — just to find small pieces of important information. Manually skimming through hundreds of pages felt tedious.

I realized that a simple AI-powered assistant could:

Help students quickly pull facts from textbooks.
Assist researchers in comparing studies.
Support professionals in analyzing legal, financial, or technical reports

With this in mind, I built DocFlow AI to improve productivity, reduce manual work, and offer a smarter way to interact with documents.

How Does DocFlow AI Work?
DocFlow AI combines several technologies to create a smooth and efficient workflow:

Step 1: PDF Upload & Processing
Upload your PDFs through the chat interface.
PyPDF2 extracts text from each document, even handling encrypted files.

Step 2: Data Indexing with FAISS
Extracted text is split into smaller chunks using LangChain’s Text Splitter.
Each chunk is converted into vector embeddings using Google Gemini AI and stored in a FAISS index for fast retrieval.

Step 3: AI-Powered Q&A
When you ask a question, DocFlow AI searches the FAISS index to find the most relevant text.
The retrieved content is passed to Google Gemini AI, which generates a detailed response, mentioning the document name and page number.

Step 4: Displaying Results
The AI’s answer is shown in the chat interface along with source references, giving you complete traceability.

Why Use DocFlow AI Instead of ChatGPT/Gemini File Uploads?
Files Stay Available – No need to re-upload PDFs; DocFlow AI keeps them indexed for easy access.

Multi-PDF Search – DocFlow AI queries multiple PDFs at once, unlike ChatGPT or Gemini’s single-session file handling.

Faster Retrieval – Indexed files enable instant search results without repeated reprocessing.

Source Referencing – Responses clearly state PDF name and page number for better traceability.

More Control & Privacy – Files stay local or on your private server, ensuring better security for sensitive data.

How Can DocFlow AI Help You?
Students & Researchers: Quickly extract key points from textbooks, papers, and notes.

Developers & Engineers: Find technical explanations directly from manuals or API docs.

Legal & Compliance Teams: Identify specific clauses or references across multiple legal documents.

Writers & Content Creators: Summarize ideas from multiple sources.

Whether you're a student preparing for exams or a professional analyzing multiple documents, DocFlow AI makes document interaction faster and easier.

💻 Installation & Setup
Want to try DocFlow AI yourself? Follow these steps:

Requirements
Python 3.9+
Streamlit, langchain, faiss-cpu, google-generativeai, PyPDF2, python-dotenv

Installation Steps
#Clone the repository
git clone https://github.com/devjothish/Docflow-ai.git

#Install dependencies 
pip install -r requirements.txt

#Set up API Key by creating a .env file in the root directory
GOOGLE_API_KEY=your_api_key_here"

# Run the app 
streamlit run app.py
How to Use DocFlow AI
Upload your PDFs through the chat interface.
Click "Process PDFs" to create a searchable index.
Type a question, and DocFlow AI will retrieve relevant answers.
Each response shows the PDF name and page number for easy reference.

Get Involved
If you find DocFlow AI useful, here’s how you can contribute:

🔗 GitHub Repository: https://github.com/devjothish/Docflow-ai.git

Got feedback or feature ideas? Let me know!

I created DocFlow AI because I wanted to solve a real problem and I’m excited to share this through the AI Builders Series. Stay tuned for the next project!

Happy Building! 🚀

Jothiswaran Arumugam 👨💻
