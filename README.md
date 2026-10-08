# RAG with Claude API + LangChain + Guardrails + PDF ingestion

This project is a starter Python application for a Retrieval-Augmented Generation (RAG) system using:
- Anthropic Claude API
- LangChain
- Guardrails validation
- PDF ingestion with `pypdf`
- FAISS vector storage
- FastAPI backend

## Features
- Upload a PDF file
- Extract content from the PDF
- Split text into chunks
- Embed chunks with a sentence-transformer model
- Store embeddings in FAISS
- Ask questions using Claude via LangChain
- Validate the user input before processing

## Project structure
```text
rag-claude-langchain/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── run.sh
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── logger.py
│   ├── schemas.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── llm.py
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   ├── rag_chain.py
│   │   └── guardrails.py
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── pdf_loader.py
│   │   ├── text_splitter.py
│   │   ├── document_pipeline.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── chat_service.py
│   └── utils/
│       ├── __init__.py
│       ├── file_utils.py
│       └── validation.py
├── data/
│   ├── raw/
│   └── vectorstore/
├── tests/
│   ├── __init__.py
│   ├── test_ingestion.py
│   ├── test_rag.py
│   └── test_guardrails.py
└── .venv/
```

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
```
Then update `.env` with your Anthropic API key.

4. Run the application:
```bash
./run.sh
```

The app will start on:
```text
http://localhost:8000
```

## API endpoints

### Upload and ingest PDF
```http
POST /ingest
```
- Form-data field: `file`
- Accepts a PDF file

### Ask a question
```http
POST /chat
```
Request body:
```json
{
  "question": "What does this document say about the policy?"
}
```

## Example
```bash
curl -X POST "http://localhost:8000/ingest" -F "file=@data/raw/sample.pdf"
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"question":"Summarize this document in three bullet points."}'
```

## Notes
- The first PDF ingestion builds the FAISS vector store.
- The app reuses the vector store for later Q&A.
- Guardrails check for empty or suspicious input before processing.

## Security
Do not commit your `.env` file with real credentials.

## Future improvements
- Add persistent database metadata
- Add file history and chat log storage
- Add HTML/markdown document support
- Add custom prompt templates and validation rules
- Add Docker support
