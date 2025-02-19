import google.generativeai as genai

API_KEY = "<ENTER_YOUR_GEMINI_API_KEY_HERE>"

genai.configure(api_key=API_KEY)

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text if response else "No response from Gemini LLM."