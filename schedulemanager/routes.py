from flask import render_template
from schedulemanager import app, db
from schedulemanager.models import Service, Vehicle


@app.route("/")
def home():
    return render_template("vehicles.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/add_service_type", methods=["GET", "POST"])
def add_service_type():
    return render_template("add_service.html")