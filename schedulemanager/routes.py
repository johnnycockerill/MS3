from flask import render_template, request, redirect, url_for
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
    if request.method == "POST":
        service = Service(service_name=request.form.get("service_name"))
        db.session.add(service)
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("add_service.html")