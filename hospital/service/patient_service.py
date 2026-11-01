
from data_access.patient_access import *

class PatientService:
    def __init__(self):
        self.data=PatientDa()

    def save_patient(self,patient):
        for patients in self.data.patient_list:
            if patient.patient_id == patients.patient_id:
                raise ValueError("The patient already exists")

        self.data.save_patient(patient)

    def find_by_patient_id(self,patient_id):
        return self.data.find_by_patient_id(patient_id)

    def delete_by_patient_id(self,patient_id):
        return self.data.delete_by_patient_id(patient_id)

    def find_all_patient(self):
        return self.data.find_all_patient()

    def book_appointment(self,patient_id):
        return self.data.book_appointment(patient_id)

    def cancel_appointment(self):
        self.data.cancel_appointment()

    def get_medical_history(self,patient_id):
        return self.data.get_medical_history(patient_id)
