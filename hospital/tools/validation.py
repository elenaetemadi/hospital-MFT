from datetime import date,datetime
import re




#--------- validation------------

def validation_name(name):
    if not isinstance(name,str):
        raise ValueError(' name must be an string')

def validation_address(address):
    if not isinstance(address, str):
        raise ValueError('Invalid address')

def validation_datetime(my_datetime):
    if not isinstance(my_datetime,datetime):
        raise ValueError('datetime must be an datetime')
    if date.today() > my_datetime.date():
        raise ValueError('date must be in the future')

def validation_id(my_id):
    if not isinstance(my_id,int):
        raise ValueError(' id must be an integer')
    if len(str(my_id)) != 10:
        raise ValueError(' id must be 10 digits')

#---------appointment validation------------

def validation_appointment(appointment):
    from models.appointment import Appointment
    if not isinstance(appointment,Appointment):
        raise ValueError(' appointment must be an Appointment')

#---------person validation------------
def validation_phone(phone):
    if not re.match(r'^09[0-9]{9}$',phone):
        raise ValueError('Invalid phone number')

#---------doctor validation------------
def validation_specialty(specialty):
    if not isinstance(specialty,str):
        raise ValueError(' specialty must be an string')

def validation_licence(licence):
    if not isinstance(licence,int):
        raise ValueError(' licence must be an integer')
    if len(str(licence)) != 10:
        raise ValueError(' licence must be 10 digits')

def validation_experience(experience):
    if not isinstance(experience,int):
        raise ValueError(' experience must be an integer')

def validation_doctor(doctor):
    from models.doctor import Doctor
    if not isinstance(doctor,Doctor):
        raise ValueError(' doctor must be an Doctor')

#---------patient validation------------
def validation_disease(disease):
    if not isinstance(disease,str):
        raise ValueError('disease must be an string')


def validation_birth_date(birth_date):
    if not isinstance(birth_date,date):
        raise ValueError(' birth_date must be an date')
    if date.today() < birth_date:
        raise ValueError('date must be in the past')

def validation_patient(patient):
    from models.patient import Patient
    if not isinstance(patient,Patient):
        raise ValueError(' patient must be an Patient')