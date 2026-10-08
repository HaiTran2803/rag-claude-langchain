from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.core.guardrails import validate_question
from app.core.retriever import create_vector_store, load_vector_store
from app.ingestion.document_pipeline import build_documents_from_pdf
from app.schemas import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()


@router.post("/ingest")
async def ingest_pdf(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    try:
        saved_path = chat_service.store_uploaded_file(file)
        documents = build_documents_from_pdf(saved_path)
        index = create_vector_store(documents)
        return {
            "message": "PDF ingested successfully",
            "filename": file.filename,
            "chunks": len(documents),
            "vector_store": str(index)
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to ingest PDF: {str(exc)}") from exc


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        validated_question = validate_question(request.question)
        answer = chat_service.ask(validated_question)
        return ChatResponse(answer=answer, sources=chat_service.last_sources)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail="No vector store exists yet. Please ingest a PDF first."
        ) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Chat processing failed: {str(exc)}") from exc
