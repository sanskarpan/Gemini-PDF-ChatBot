import sqlite3
from contextlib import contextmanager

DATABASE_URL = "app/db/chatbot.db"

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()

def execute_custom_query(query, params=()):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
    return rows

def get_db_data():
    # Execute the custom query
    query = """
    SELECT question, response 
    FROM Responses 
    JOIN Survey ON Responses.survey_id = Survey.survey_id 
    """
    rows = execute_custom_query(query)
    
    # Combine the data into a formatted string
    db_data = "\n".join([f"Q: {row[0]} - A: {row[1]}" for row in rows])
    
    return db_data

def get_all_db_data():
    # Fetching all data from your tables
    users_data = execute_custom_query("SELECT user_id, survey_id FROM Users")
    surveys_data = execute_custom_query("SELECT survey_id, question_id, question FROM Survey")
    responses_data = execute_custom_query("SELECT user_id, survey_id, question_id, response FROM Responses")

    # Formatting the data into a readable format for the model
    formatted_data = (
        "Users:\n" + "\n".join([f"User ID: {user[0]}, Survey ID: {user[1]}" for user in users_data]) +
        "\n\nSurveys:\n" + "\n".join([f"Survey ID: {survey[0]}, Question ID: {survey[1]}, Question: {survey[2]}" for survey in surveys_data]) +
        "\n\nResponses:\n" + "\n".join([f"User ID: {response[0]}, Survey ID: {response[1]}, Question ID: {response[2]}, Response: {response[3]}" for response in responses_data])
    )

    return formatted_data


