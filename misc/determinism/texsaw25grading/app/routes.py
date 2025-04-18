from flask import request, jsonify, redirect, render_template, send_from_directory
from app import app
from app.database import get_db
from sqlite3 import IntegrityError
import os
from werkzeug.utils import secure_filename
from passlib.hash import bcrypt_sha256

ADMIN_PASSWORD = 'supersecret102394809823509812039840920100101039488482093dflksjfljthispasswordrocks'  # Replace with a real password

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if data.get('password') != ADMIN_PASSWORD:
        return jsonify({"error": "Invalid password"}), 403
    key = bcrypt_sha256.hash(str(data['key']))
    name = data['name']
    with get_db() as db:
        db.execute('INSERT OR IGNORE INTO students (key, name) VALUES (?, ?)', (key, name))
        db.execute('INSERT INTO submissions (student_key) VALUES (?)', (key,))
    return jsonify({"status": "registered"})

@app.route('/submit', methods=['GET'])
def submit_form():
    return render_template("submit.html")

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<path:filename>')
def uploads(filename):
    print(os.listdir(app.config['UPLOAD_FOLDER']), flush=True)
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], path=filename, as_attachment=True)

@app.route('/submit', methods=['POST'])
def submit():
    token = bcrypt_sha256.hash(str(request.form.get('token', '').strip()))
    submission = request.form.get('submission', '').strip()
    file = request.files.get('file')

    if not token:
        return "Token is required.", 400

    # Validate the token
    with get_db() as db:
        student = db.execute('SELECT * FROM students WHERE key = ?', (token,)).fetchone()
        if not student:
            return "Invalid token.", 400

    # Handle text submission
    if submission and not file:
        submission_filename = None
        submission_type = 'text'
    # Handle file upload (PDF or PNG)
    elif file and allowed_file(file.filename):
        filename = secure_filename(token + file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        submission_filename = filename
        submission_type = file.filename.rsplit('.', 1)[1].lower()
    else:
        return "Invalid file format. Only PDF and PNG are allowed.", 400

    # Save submission data to database
    with get_db() as db:
        db.execute('''
            UPDATE submissions SET submission = ?, submission_filename = ?, submission_type = ?, graded = 0 WHERE student_key = ?
        ''', (submission, submission_filename, submission_type, token))
        print(db.execute("SELECT * FROM submissions").fetchall(), flush=True)

    return redirect('/submit')

@app.route('/a9c9fbc12c4a06cdb0078ae60eb04881', methods=['GET'])
def grade():
    with get_db() as db:
        submissions = [dict(row) for row in db.execute('''
            SELECT * FROM submissions WHERE submission IS NOT NULL AND graded = 0
        ''').fetchall()]
        for s in submissions:
            for x in db.execute("SELECT * FROM students WHERE key = ?", (s['student_key'],)).fetchall():
                s.update(x)

        print(submissions, flush=True)
		
        comments = db.execute('SELECT * FROM canned_comments ORDER BY id DESC').fetchall()
        return render_template("grading.html", students=submissions, comments=comments)

@app.route('/a9c9fbc12c4a06cdb0078ae60eb04881/<key>', methods=['POST'])
def grade_student(key):
    action = request.form['action']
    comment = request.form.get('comment', '').strip()

    with get_db() as db:
        if action == 'accept':
            db.execute('UPDATE submissions SET comment = ?, graded = 1 WHERE student_key = ?', (comment, key))
            db.execute('UPDATE students SET solved = 1 WHERE key = ?', (key,))
        elif action in ['reject', 'reject_save']:
            db.execute('UPDATE submissions SET comment = ?, graded = 1 WHERE student_key = ?', (comment, key))
            if action == 'reject_save' and comment:
                try:
                    db.execute('INSERT INTO canned_comments (text) VALUES (?)', (comment,))
                except IntegrityError:
                    pass  # already exists

    return redirect('/a9c9fbc12c4a06cdb0078ae60eb04881')


@app.route('/flag', methods=['GET', 'POST'])
def flag():
    if request.method == 'POST':
        token = request.form.get('token', '').strip()
        with get_db() as db:
            student = dict(db.execute('SELECT * FROM students WHERE key = ?', (token,)).fetchone())
            if student:
                submission = db.execute("SELECT *  FROM submissions WHERE student_key = ?", (student['key'],)).fetchall()
                if len(submission):
                    submission = dict(submission[0])
                    student['comment'] = submission['comment']
                    student['graded'] = submission['graded']
                return render_template("flag_result.html", student=student)
            else:
                return render_template("flag_form.html", error="Invalid token.")
    return render_template("flag_form.html")
