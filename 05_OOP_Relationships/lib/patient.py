from datetime import datetime
class Patient:
    all_ = []

    def __init__(self, name):
        self.name = name
        type(self).all_.append(self)

    def appointments(self):
        from lib.appointment import Appointment
        return [appt for appt in Appointment.all_ if appt.patient is self]

    def doctors(self):
        from lib.appointment import Appointment
        return list({appt.doctor for appt in self.appointments()})
