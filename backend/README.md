# Gemini PDF ChatBot Backend

## Overview

This is the backend for the Gemini PDF ChatBot, a project that allows users to chat with PDF files and SQLite databases simultaneously. The backend is built with FastAPI, using the Gemini LLM model for natural language processing.

## Features

- Handle user queries about PDFs and SQLite databases.
- Extract text from PDFs and DOCX files.
- Integrate with the Gemini API for generating responses.
- Interact with a SQLite database to fetch user-specific data.

## Installation

### Prerequisites

- Python 3.8+
- Virtualenv (recommended)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sanskarpan/Gemini-PDF-ChatBot.git
   cd backend
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Setup Gemini API key:** <br/>
   Create your Gemini API key from [here](https://aistudio.google.com/app/apikey) and place it in backend/app/utils/gemini.py 
![backend/gemini_api_setup.png](backend/gemini_api_setup.png)
5. **Run Backend Server**
   ```bash
   uvicorn app.main:app --reload
   ```

### Project Structure
![backend/Backend_Structure.png](backend/Backend_Structure.png)

### Overall Flow
![backend/overall_flow.png](backend/overall_flow.png)