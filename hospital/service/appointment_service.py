from models.appointment import Appointment
from datetime import date


class AppointmentService:
    def __init__(self, appointment_da, patient_da, doctor_da):
        self.data = appointment_da
        self.patient_data = patient_da
        self.doctor_data = doctor_da

    def save_appointment(self, appointment):
        for appointments in self.data.appointment_list:
            if appointments.appointment_id == appointment.appointment_id:
                raise ValueError("appointment id already exists")

        self.data.save_appointment(appointment)

    def book_appointment(self, appointment_id, patient_id,license, appointment_datetime):

        patient = self.patient_data.find_by_patient_id(patient_id)
        doctor = self.doctor_data.find_by_license(license)

        appointment = Appointment(appointment_id, doctor, patient, appointment_datetime)
        self.save_appointment(appointment)
        return appointment

    def delete_appointment(self, appointment_id):
        return self.data.delete_appointment(appointment_id)

    def find_by_appointment_id(self, appointment_id):
        return self.data.find_by_appointment_id(appointment_id)

    def find_all_appointments(self):
        return self.data.find_all_appointments()

    def find_doctor(self, name, family):
        return self.data.find_doctor(name, family)

    def find_patient(self, name, family):
        return self.data.find_patient(name, family)

    def find_patient_appointments(self, patient_id):
        patient = self.patient_data.find_by_patient_id(patient_id)

        result= [
            appointment for appointment in self.data.appointment_list
            if appointment.patient is patient
        ]
        return result

    def find_today_appointments(self, license):
        doctor = self.doctor_data.find_by_license(license)

        result= [
            appointment for appointment in self.data.appointment_list
            if appointment.doctor is doctor
            and appointment.appointment_datetime.date() == date.today()
        ]
        return result