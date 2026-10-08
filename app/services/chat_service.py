from pathlib import Path
from typing import List

from app.config import UPLOAD_FOLDER
from app.core.llm import create_llm
from app.core.retriever import load_vector_store
from app.core.rag_chain import build_rag_chain


class ChatService:
    def __init__(self):
        self.last_sources: List[str] = []

    def store_uploaded_file(self, uploaded_file):
        UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
        destination = UPLOAD_FOLDER / uploaded_file.filename
        destination.write_bytes(uploaded_file.file.read())
        return str(destination)

    def ask(self, question: str) -> str:
        vectorstore = load_vector_store()
        llm = create_llm()
        self.last_sources = []

        chain = build_rag_chain(vectorstore, llm)
        answer = chain.invoke(question)

        docs = vectorstore.similarity_search(question, k=4)
        self.last_sources = [doc.metadata.get("source", "unknown") for doc in docs]
        return answer
