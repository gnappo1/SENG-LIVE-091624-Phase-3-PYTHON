class Owner:
    all_ = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        type(self).all_.append(self)

