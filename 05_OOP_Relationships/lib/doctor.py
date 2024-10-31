from .appointment import *


class Doctor:
    all_ = []

    def __init__(self, name, field):
        self.name = name
        self.field = field
        type(self).all_.append(self)

    def appointments(self):
        from lib.appointment import Appointment
        return [appt for appt in Appointment.all_ if appt.doctor is self]

    def patients(self):
        from lib.appointment import Appointment
        return list({appt.patient for appt in self.appointments()})
