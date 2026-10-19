from hospital.tools.validation import *


class Appointment:
    def __init__(self, appointment_id, doctor, patient, appointment_datetime):
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.appointment_datetime = appointment_datetime

    def get_appointment_id(self):
        return self.__appointment_id

    def set_appointment_id(self, appointment_id):
        validation_id(appointment_id)
        self.__appointment_id = appointment_id

    def get_appointment_datetime(self):
        return self.__appointment_datetime

    def set_appointment_datetime(self, appointment_datetime):
        validation_datetime(appointment_datetime)
        self.__appointment_datetime = appointment_datetime


    def get_patient(self):
        return self.__patient

    def set_patient(self, patient):
        validation_patient(patient)
        self.__patient = patient

    def get_doctor(self):
        return self.__doctor

    def set_doctor(self, doctor):
        validation_doctor(doctor)
        self.__doctor = doctor

    def __repr__(self):
        return f'Appointment({self.appointment_id},{self.doctor},{self.patient},{self.appointment_datetime})'

    appointment_id = property(get_appointment_id, set_appointment_id)
    appointment_datetime= property(get_appointment_datetime, set_appointment_datetime)
    doctor = property(get_doctor, set_doctor)
    patient = property(get_patient, set_patient)