import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('app/db/chatbot.db')
cursor = conn.cursor()

# Create Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    survey_id INTEGER
);
''')

# Create Survey table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Survey (
    survey_id INTEGER,
    question_id INTEGER,
    question TEXT,
    PRIMARY KEY (survey_id, question_id)
);
''')

# Create Responses table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Responses (
    user_id INTEGER,
    survey_id INTEGER,
    question_id INTEGER,
    response TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (survey_id) REFERENCES Survey(survey_id)
);
''')

# Insert initial data into Users table
cursor.executemany('''
INSERT INTO Users (user_id, survey_id) VALUES (?, ?)
''', [(1, 101), (2, 101), (3, 102), (4, 102),(5,103)])

# Insert initial data into Survey table
cursor.executemany('''
INSERT INTO Survey (survey_id, question_id, question) VALUES (?, ?, ?)
''', [(101, 1, "How satisfied are you with our service?"),
      (101, 2, "Would you recommend our service to others?"),
      (102, 3, "How easy was it to use the product?"),
      (102, 4, "How likely are you to use the product again?")])

# Insert initial data into Responses table
cursor.executemany('''
INSERT INTO Responses (user_id, survey_id, question_id, response) VALUES (?, ?, ?, ?)
''', [(1, 101, 1, "Very satisfied"),
      (1, 101, 2, "Yes"),
      (2, 101, 1, "Satisfied"),
      (2, 101, 2, "Maybe"),
      (3, 102, 3, "Easy"),
      (3, 102, 4, "Very likely"),
      (4, 102, 3, "Difficult"),
      (4, 102, 4, "Unlikely"),
      (5, 103, 1, "Neutral")])

# Commit and close
conn.commit()
conn.close()
