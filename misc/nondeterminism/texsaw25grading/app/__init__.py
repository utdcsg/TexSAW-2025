from flask import Flask

app = Flask(__name__)

from app import routes
from app.database import init_db

init_db()
