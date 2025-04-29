from flask import render_template
from schedulemanager import app, db
from schedulemanager.models import Service, Vehicle


@app.route("/")
def home():
    return render_template("base.html")
