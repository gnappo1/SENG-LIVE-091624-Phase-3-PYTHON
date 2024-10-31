import datetime


class Appointment:
    all_ = []

    def __init__(self, doctor, patient, reason_for_visit, date):
        self.reason_for_visit = reason_for_visit
        self.date = date
        self.doctor = doctor
        self.patient = patient
        type(self).all_.append(self)
