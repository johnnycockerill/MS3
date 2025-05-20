from flask import render_template, request, redirect, url_for
from schedulemanager import app, db
from schedulemanager.models import Service, Vehicle


@app.route("/")
def home():
    vehicles = list(Vehicle.query.order_by(Vehicle.id).all())
    return render_template("vehicles.html", vehicles=vehicles)


@app.route("/services")
def services():
    services = list(Service.query.order_by(Service.service_name).all())
    return render_template("services.html", services=services)


@app.route("/add_service_type", methods=["GET", "POST"])
def add_service_type():
    if request.method == "POST":
        service = Service(service_name=request.form.get("service_name"))
        db.session.add(service)
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("add_service.html")


@app.route("/edit_service_type/<int:service_id>", methods=["GET", "POST"])
def edit_service_type(service_id):
    service = Service.query.get_or_404(service_id)
    if request.method == "POST":
        service.service_name = request.form.get("service_name")
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("edit_service.html", service=service)


@app.route("/delete_service_type/<int:service_id>")
def delete_service_type(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return redirect(url_for("services"))


@app.route("/add_vehicle", methods=["GET", "POST"])
def add_vehicle():
    services = list(Service.query.order_by(Service.service_name).all())
    if request.method == "POST":
        vehicle = Vehicle(
            vehicle_reg=request.form.get("vehicle_reg"),
            vehicle_type=request.form.get("vehicle_type"),
            work_completed=bool(True if request.form.get("work_completed") else False),
            due_date=request.form.get("due_date"),
            service_id=request.form.get("service_id")
        )
        db.session.add(vehicle)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_vehicle.html", services=services)
