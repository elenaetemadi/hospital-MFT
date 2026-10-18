from tools.validation import *
from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment

class Hospital:
    def __init__(self, name, address, doctors, patients, appointments):
        self.name = name
        self.address = address
        self.doctors = doctors if doctors is not None else []
        self.patient = patients if patients is not None else []
        self.appointments = appointments if appointments is not None else []

    def __repr__(self):
        return f'Hospital( {self.name},{self.address},{self.doctors},{self.patient},{self.appointments})'

    def get_patient(self):
        return self.__patient

    def set_patient(self, patient):
        validation_patient(patient)
        self.__patient = patient

    def get_appointment(self):
        return self.__appointments

    def set_appointment(self, appointment):
        validation_appointment(appointment)
        self.__appointments = appointment

    def get_doctors(self):
        return self.__doctors

    def set_doctors(self, doctor):
        validation_doctor(doctor)
        self.__doctors = doctor

    def get_name(self):
        return self.__name

    def set_name(self, name):
        validation_name(name)
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        validation_address(address)
        self.__address = address

    patient = property(get_patient, set_patient)
    appointment = property(get_appointment, set_appointment)
    doctors = property(get_doctors, set_doctors)
    address = property(get_address, set_address)
    name_ = property(get_name, set_name)