import sqlite3

# Connect to SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect("vivi.db")
cursor = conn.cursor()

# Create job_list table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS job_list (
        id INTEGER PRIMARY KEY,
        company_name TEXT,
        job_description TEXT
    )
''')

# Insert sample data into job_list table
job_list_data = [
    ("Company A", "Software Engineer"),
    ("Company B", "Data Scientist"),
    ("Company C", "Product Manager"),
    ("Company D", "UX/UI Designer"),
    ("Company E", "Marketing Specialist")
]
cursor.executemany('''
    INSERT INTO job_list (company_name, job_description)
    VALUES (?, ?)
''', job_list_data)

# Create resume table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS resume (
        id INTEGER PRIMARY KEY,
        candidate_email TEXT,
        resume_details TEXT
    )
''')

# Insert sample data into resume table
resume_data = [
    ("john@example.com", "Experienced software developer with expertise in Python and Django."),
    ("jane@example.com", "Data scientist with a strong background in machine learning."),
    ("mark@example.com", "Product management professional with a focus on agile methodologies."),
    ("alice@example.com", "Creative and detail-oriented UX/UI designer with a passion for user-centric design."),
    ("david@example.com", "Marketing specialist with a track record of successful digital campaigns.")
]
cursor.executemany('''
    INSERT INTO resume (candidate_email, resume_details)
    VALUES (?, ?)
''', resume_data)

# Create chat_history table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY,
        candidate_email TEXT,
        chat_text TEXT
    )
''')

# Insert sample data into chat_history table
chat_history_data = [
    ("john@example.com", "Hello, I'm interested in the Software Engineer position."),
    ("jane@example.com", "I have experience in building predictive models using machine learning."),
    ("mark@example.com", "What are the key responsibilities of the Product Manager role?"),
    ("alice@example.com", "I believe user experience is crucial for product success."),
    ("david@example.com", "How can we leverage digital marketing to reach our target audience?")
]
cursor.executemany('''
    INSERT INTO chat_history (candidate_email, chat_text)
    VALUES (?, ?)
''', chat_history_data)

# Commit changes and close the connection
conn.commit()
conn.close()
