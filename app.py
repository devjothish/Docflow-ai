import streamlit as st
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Streamlit
st.set_page_config(page_title="DocFlow AI", page_icon="📒", layout="wide")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vector_store_initialized" not in st.session_state:
    st.session_state.vector_store_initialized = False

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Function to extract text from PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)

        # Handle encrypted PDFs
        if pdf_reader.is_encrypted:
            try:
                pdf_reader.decrypt("")
            except:
                st.warning(f"Skipping encrypted PDF: {pdf.name}")
                continue  # Skip if decryption fails

        for page in pdf_reader.pages:
            text += page.extract_text() or ""

    return text

# Function to create FAISS vector store
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    st.session_state.vector_store_initialized = True

# Function to load retrieval-based conversational chain
def get_conversational_chain(vector_store):
    prompt_template = """
    Answer the question as detailed as possible from the provided context and mention from which page of the document the answer is derived and say the uploaded pdf name.
    If the answer is not in the provided context, say: "The answer is not available in the context"
    
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    # Use RetrievalQA instead of load_qa_chain
    chain = RetrievalQA.from_chain_type(
        llm=model,
        chain_type="stuff",  # Retains original behavior
        retriever=vector_store.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )
    return chain


# Function to handle user input and retrieval
def user_input(user_question):
    if not st.session_state.vector_store_initialized:
        st.error("PDF not found! Please upload PDFs and process them first.")
        return

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain(new_db)
    response = chain.invoke({"query": user_question})
    reply = response["result"]
    # Store conversation in session state
    st.session_state.chat_history.append({"question": user_question, "reply": reply})

# UI Layout
#st.sidebar.image("img/cover.jpg")
st.sidebar.title("📁 PDF Upload")
pdf_docs = st.sidebar.file_uploader("Upload PDFs & Click 'Submit'", accept_multiple_files=True)

if st.sidebar.button("Submit PDFs"):
    with st.spinner("Processing PDFs..."):
        raw_text = get_pdf_text(pdf_docs)
        text_chunks = RecursiveCharacterTextSplitter(chunk_size=50000, chunk_overlap=1000).split_text(raw_text)
        get_vector_store(text_chunks)
        st.sidebar.success("✅ Processing Complete!")

st.sidebar.write("---")
st.sidebar.write("AI Agent by Jothiswaran Arumugam")

# Chat Interface
st.title("DocFlow AI - A central hub for interacting with multiple PDFs")
#st.subheader("Chat History")

chat_container = st.container()

# Display chat history (Bottom-up)
with chat_container:
    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(f"**User:** {chat['question']}")
        with st.chat_message("assistant"):
            st.write(f"**Agent:** {chat['reply']}")

# User input at bottom
user_question = st.chat_input("Ask anything...")
if user_question:
    user_input(user_question)
    st.rerun()  # Refresh UI after sending a message
