from backend.app.db.database import get_db_connection

def get_user_by_id(user_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE user_id = ?", (user_id,))
        return cursor.fetchone()

def get_survey_by_id(survey_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Survey WHERE survey_id = ?", (survey_id,))
        return cursor.fetchall()

def get_responses_by_user_and_survey(user_id, survey_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Responses WHERE user_id = ? AND survey_id = ?", (user_id, survey_id))
        return cursor.fetchall()
