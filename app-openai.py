from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
import os
from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI

app = Flask(__name__)

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = ""

def process_pdf(pdf_path):
    pdfreader = PdfReader(pdf_path)
    raw_text = ''
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content
    return raw_text

def create_document_search(texts):
    embeddings = OpenAIEmbeddings()
    document_search = FAISS.from_texts(texts, embeddings)
    return document_search

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)
        raw_text = process_pdf(file_path)
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=800,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_text(raw_text)
        session['texts'] = texts
        
        return jsonify({"message": "Upload successful"}), 200

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get("question")

    if not question:
        return jsonify({"error": "Question not provided"}), 400

    if 'texts' not in session:
        return jsonify({"error": "Document not processed yet"}), 400

    texts = session['texts']
    document_search = create_document_search(texts)
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    docs = document_search.similarity_search(question)
    result = chain.run(input_documents=docs, question=question).strip()
    return jsonify({"answer": result}), 200


if __name__ == "__main__":
    app.secret_key = 'supersecretkey'
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
