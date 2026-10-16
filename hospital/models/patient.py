from models.person import Person
import random
from tools.validation import validation_id, validation_disease,validation_birthdate
from models.appointment import Appointment

class Patient(Person):
    def __init__(self, national_id, name, phone, address, patient_id, disease, birth_date):
        super().__init__(national_id, name, phone, address)
        validation_id(patient_id)
        validation_disease(disease)
        validation_birthdate(birth_date)
        self.patient_id = patient_id
        self.disease = disease
        self.birth_date = birth_date

    def __repr__(self):
        return f'Patient({self.name},{self.address},{self.disease},{self.birth_date})'

    def get_patient_id(self):
        return self.patient_id

    def set_patient_id(self, patient_id):
        validation_id(patient_id)
        self.patient_id = patient_id

    def get_disease(self):
        return self.disease

    def set_disease(self,disease):
        validation_disease(disease)
        self.disease=disease

    def get_birth_date(self):
        return self.birth_date

    def set_birth_date(self, birth_date):
        validation_birthdate(birth_date)
        self.birth_date = birth_date

    def book(self, doctor, date):
        Appointment(random.randint(10000000,99999999),doctor,self,date)
        print("The patient booked the appointment")

    def cancel_appointment(self,patient_id):
        for appointment in Appointment.appointments:
            if appointment.patient.patient_id == patient_id:
                Appointment.appointments.remove(appointment)
        print("The patient cancelled the appointment")

    def get_medical_history(self):
        return self.disease

    patient_id = property(get_patient_id, set_patient_id)
    disease=property(get_disease,set_disease)
    birth_date = property(get_birth_date,set_birth_date)