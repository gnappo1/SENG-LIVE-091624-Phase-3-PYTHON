#!/usr/bin/env python3

# from lib.pet import Pet
# from lib.owner import Owner


# pat = Owner(
#     "Pat",
#     "Jones",
# )
# rose = Owner(
#     "Rose",
#     "Smith",
# )
# joe = Owner("Joe", "Jones")
# theresa = Owner("Theresa", "Jones")

# taco = Pet(
#     "Taco",
#     "Cat",
#     pat
# )
# fido = Pet(
#     "Fido",
#     "Dog",
#     rose
# )
# princess = Pet("Princess", "Fish", joe)


from lib.appointment import Appointment
from lib.doctor import Doctor
from lib.patient import Patient

jimmy = Patient("Jimmy")
patty = Patient("Patty")
may = Patient("May")

rosenbaum = Doctor("Dr. Rosenbaum", "Gynocology")
williams = Doctor("Dr. Williams", "Oncology")


a1 = Appointment(rosenbaum, may, "Stomach issues.", "5/25/23")
a2= Appointment(rosenbaum, patty, "Non-stop migrains", "5/26/23")
a3= Appointment(williams, jimmy, "Legs always sore in the mornings", "5/23/23")
a4=Appointment(williams, patty, "Feels light-headed when jogging", "5/12/23")
a5=Appointment(rosenbaum, may, "Can't keep food down", "5/30/23")


import ipdb

ipdb.set_trace()
