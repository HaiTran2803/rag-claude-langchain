from langchain_core.documents import Document

from app.ingestion.pdf_loader import load_pdf
from app.ingestion.text_splitter import split_text


def build_documents_from_pdf(file_path: str) -> list[Document]:
    text = load_pdf(file_path)
    chunks = split_text(text)

    return [
        Document(page_content=chunk, metadata={"source": file_path})
        for chunk in chunks
    ]
