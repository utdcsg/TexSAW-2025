import sqlite3

DATABASE = 'students.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        # Create homeworks table to track homework assignments
        db.execute('''
            CREATE TABLE IF NOT EXISTS homeworks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL  -- Name of the homework
            )
        ''')

        # Create students table to track students' submissions for each homework
        db.execute('''
            CREATE TABLE IF NOT EXISTS students (
                key TEXT PRIMARY KEY,
                name TEXT,
                solved INTEGER DEFAULT 0,
                graded INTEGER DEFAULT 0
            )
        ''')

        # Create submissions table to track each student's submission per homework
        db.execute('''
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_key TEXT,
                homework_id INTEGER,
                submission TEXT,  -- For text submission
                submission_filename TEXT,  -- For file submission (PDF/PNG)
                submission_type TEXT,  -- Type of submission (text, pdf, png)
                graded INTEGER DEFAULT 0,  -- Whether the submission is graded
                comment TEXT,  -- Comments related to this submission
                FOREIGN KEY(student_key) REFERENCES students(key),
                FOREIGN KEY(homework_id) REFERENCES homeworks(id)
            )
        ''')

        # Create canned comments table for reuse across homeworks
        db.execute('''
            CREATE TABLE IF NOT EXISTS canned_comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT UNIQUE NOT NULL
            )
        ''')

