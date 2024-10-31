from .appointment import *


class Doctor:
    all_ = []

    def __init__(self, name, field):
        self.name = name
        self.field = field
        type(self).all_.append(self)
