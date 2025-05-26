from schedulemanager import db


class Service(db.Model):
    # schema for the service model
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(40), unique=True, nullable=False)
    vehicles = db.relationship("Vehicle", backref="service", cascade="all, delete", lazy=True) # noqa

    def __repr__(self):
        # __repr__ to represet itself in the form of a string
        return self.service_name


class Vehicle(db.Model):
    # schema for the vehicle model
    id = db.Column(db.Integer, primary_key=True)
    vehicle_reg = db.Column(db.String(50), nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)
    work_completed = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("service.id", ondelete="CASCADE"), nullable=False) # noqa

    def __repr__(self):
        # __repr__ to represet itself in the form of a string
        return "Reg: {0} - Type: {1} | Due: {2} - Completed: {3}".format(
            self.vehicle_reg, self.vehicle_type, self.due_date, self.work_completed # noqa
        )
