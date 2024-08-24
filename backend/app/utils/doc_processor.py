import fitz  # PyMuPDF for PDF processing
import docx  # python-docx for Word document processing

def extract_text_from_document(doc_path):
    try:
        if doc_path.endswith(".pdf"):
            doc = fitz.open(doc_path)
            text = ""
            for page in doc:
                text += page.get_text()
        elif doc_path.endswith(".docx"):
            doc = docx.Document(doc_path)
            text = "\n".join([para.text for para in doc.paragraphs])
        else:
            raise ValueError("Unsupported document format.")
        
        return text
    except Exception as e:
        print(f"Error extracting text from document: {e}")
        return None
