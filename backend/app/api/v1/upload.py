from fastapi import APIRouter, File, UploadFile, HTTPException
import os
from app.utils.doc_processor import extract_text_from_document

router = APIRouter()

UPLOAD_DIR = "uploaded_documents"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@router.post("/document")
async def upload_document(file: UploadFile = File(...)):
    # Determine the file extension
    file_ext = file.filename.split(".")[-1].lower()

    # Set the target filename based on the file type
    if file_ext == "pdf":
        target_filename = "sample.pdf"
    elif file_ext == "docx":
        target_filename = "sample.docx"
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type. Please upload a PDF or DOCX file.")

    file_path = os.path.join(UPLOAD_DIR, target_filename)

    try:
        # Save the uploaded file with the new name
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Extract text from the document
        extracted_text = extract_text_from_document(file_path)

        if extracted_text is None:
            raise HTTPException(status_code=500, detail="Failed to extract text from the document.")

        return {
            "filename": target_filename,
            "path": file_path,
            "extracted_text": extracted_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
