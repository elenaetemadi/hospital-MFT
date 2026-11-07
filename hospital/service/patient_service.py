
from data_access.patient_access import *

class PatientService:
    def __init__(self,patient_da,appointment_service):
        self.data=patient_da
        self.appointment_service=appointment_service

    def save_patient(self,patient):
        for patients in self.data.patient_list:
            if patient.patient_id == patients.patient_id or patient.national_id == patients.national_id:
                raise ValueError("This patient id/national id  already exists")

        self.data.save_patient(patient)

    def find_by_patient_id(self,patient_id):
        return self.data.find_by_patient_id(patient_id)

    def delete_by_patient_id(self,patient_id):
        return self.data.delete_by_patient_id(patient_id)

    def find_all_patient(self):
        return self.data.find_all_patient()

    def find_patient_appointment(self,patient_id):
        return self.appointment_service.find_patient_appointment(patient_id)

    def get_medical_history(self,patient_id):
        return self.data.get_medical_history(patient_id)
