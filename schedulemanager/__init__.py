import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from schedulemanager import routes

with app.app_context():
    db.create_all()
