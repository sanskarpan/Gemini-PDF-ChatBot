from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.gemini import get_gemini_response
from app.db.database import get_all_db_data
from app.utils.doc_processor import extract_text_from_document
import os

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    user_id: int

def format_response(text: str) -> str:
    # Basic formatting adjustments for readability
    formatted_text = text.replace("**", "")  # Remove bold markers
    formatted_text = formatted_text.replace("*", "")  # Remove italics markers
    formatted_text = formatted_text.replace("#", "")  # Remove headers markers
    formatted_text = formatted_text.replace("\n", "\n\n")  # Add extra line breaks for readability
    
    return formatted_text.strip()

@router.post("/")
async def chat_with_bot(request: ChatRequest):
    try:
        user_query = request.query
        user_id = request.user_id

        db_data = get_all_db_data()

        # Determine the document path based on file existence
        pdf_path = "uploaded_documents/sample.pdf"
        docx_path = "uploaded_documents/sample.docx"

        if os.path.exists(pdf_path):
            doc_path = pdf_path
        elif os.path.exists(docx_path):
            doc_path = docx_path
        else:
            raise HTTPException(status_code=404, detail="No document found for processing.")

        # Extract text from the identified document
        doc_text = extract_text_from_document(doc_path)
        
        combined_prompt = (
        f"User query: {user_query}\n"
        f"Here is the data from the database:\n{db_data}\n"
        f"Document Content:\n{doc_text}\n"
        "Please answer the query using the above information."
        )


        # Get a response from the Gemini LLM
        gemini_response = get_gemini_response(combined_prompt)
        gemini_response = format_response(gemini_response)
        return {"response": gemini_response}

    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    except:
        return "None"
