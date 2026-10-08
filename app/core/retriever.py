from langchain_community.vectorstores import FAISS

from app.config import VECTORSTORE_PATH
from app.core.embeddings import create_embeddings


def create_vector_store(documents):
    embeddings = create_embeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    VECTORSTORE_PATH.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(str(VECTORSTORE_PATH))
    return vectorstore


def load_vector_store():
    embeddings = create_embeddings()
    if not VECTORSTORE_PATH.exists():
        raise FileNotFoundError("Vector store does not exist. Please ingest a PDF first.")

    return FAISS.load_local(
        str(VECTORSTORE_PATH),
        embeddings,
        allow_dangerous_deserialization=True,
    )
