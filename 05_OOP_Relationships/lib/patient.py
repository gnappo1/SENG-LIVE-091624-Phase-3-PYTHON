from datetime import datetime
class Patient:
    all_ = []

    def __init__(self, name):
        self.name = name
        type(self).all_.append(self)
