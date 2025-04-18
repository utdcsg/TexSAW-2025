from app import app
from app.database import get_db

if __name__ == "__main__":
    with get_db() as db:
        db.execute('INSERT OR IGNORE INTO students (key, name) VALUES (?, ?)', ("test", "charles"))
        db.execute('INSERT OR IGNORE INTO students (key, name) VALUES (?, ?)', ("test2", "charles2"))
    app.run(debug=True, host="0.0.0.0")
