from datetime import date
import re

def validation_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

def validation_id(id):
    if not isinstance(id,str):
        raise TypeError("ID must be a string")


def validation_date(date):
    if not isinstance(date, date):
        raise TypeError("Date must be a date")
    if date<date.today():
        raise TypeError("Date cannot be in the past")

def validation_phone(phone):
    if not re.match("^09[0-9]{9}$", phone):
        raise TypeError("Phone number must be a 9-digit number")

def validation_address(address):
    if not isinstance(address, str):
        raise TypeError("Address must be a string")

def validation_specialty(specialty):
    if not isinstance(specialty, str):
        raise TypeError("Specialty must be a string")

def validation_birthdate(birth_date):
    if not isinstance(birth_date, date):
        raise TypeError("Birth date must be a date")
    if birth_date>=date.today():
        raise TypeError("Birth date cannot be in the future")

def validation_appointment(appointment):
    from models.appointment import Appointment
    if not isinstance(appointment, Appointment):
        raise TypeError("Appointment must be a Appointment")

def validation_patient(patient):
    from models.patient import Patient
    if not isinstance(patient, Patient):
        raise TypeError("Patient must be a Patient")

def validation_doctor(doctor):
    from models.doctor import Doctor

    if not isinstance(doctor, Doctor):
        raise TypeError("Doctor must be a Doctor")

def validation_experience(experience):
    if not isinstance(experience, int):
        raise TypeError("Experience must be a integer")

def validation_disease(disease):
    if not isinstance(disease,str):
        raise ValueError("disease must be a string")