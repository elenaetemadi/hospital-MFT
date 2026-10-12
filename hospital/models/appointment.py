from doctor import Doctor
from patient import Patient
from datetime import datetime, date, time


class Appointment:
    def __init__(self, appointment_id, doctor, patient, date_time):
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time

    def get_appointment_id(self):
        return self.__appointment_id

    def set_appointment_id(self, appointment_id, doctor, patient, date_time):
        if isinstance(doctor, Doctor) and isinstance(patient, Patient) and isinstance(date_time, datetime):
            self.__appointment_id = appointment_id

    def __repr__(self):
        return f'Doctor({self.doctor},{self.patient},{self.date_time},{self.date_time})'

    def book(self, appointment_id, doctor, patient, date_time):
        if isinstance(doctor, Doctor) and isinstance(patient, Patient) and isinstance(date_time, datetime):
            print('booked')

    def cancel(self, appointment_id):
        print('cancel')