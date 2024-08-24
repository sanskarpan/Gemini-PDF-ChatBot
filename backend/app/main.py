from fastapi import FastAPI
from app.api.v1 import chat, upload
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:8000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/v1/chat")
app.include_router(upload.router, prefix="/api/v1/upload")

@app.get("/")
async def root():
    return {"message": "Chatbot"}
