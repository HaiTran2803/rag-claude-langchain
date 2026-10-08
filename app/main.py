from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="RAG with Claude + LangChain", version="0.1.0")
app.include_router(router)


@app.get("/")
async def hello():
    return {"message": "RAG API is running"}
