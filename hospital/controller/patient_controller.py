
from models.patient import Patient

class PatientController:
    def __init__(self,patient_service):
        self.patient_service = patient_service

    def save_patient(self,national_id, name, family,phone, address, patient_id, disease, birth_date):
        try:
            patient=Patient(national_id, name, family,phone, address, patient_id, disease, birth_date)
            self.patient_service.save_patient(patient)
            return "patient saved successfully"
        except Exception as e:
            print(e)
            return "Error saving patient"

    def find_by_patient_id(self,patient_id):
        try:
            return self.patient_service.find_by_patient_id(patient_id),"patient found successfully"

        except ValueError as e:
            return str(e)

        except Exception as e:
            print(e)
            return "Error finding patient"

    def delete_by_patient_id(self,patient_id):
        try:
            self.patient_service.delete_by_patient_id(patient_id)
            return "deleted patient successfully"

        except ValueError as e:
            return str(e)

        except Exception as e:
            print(e)
            return "Error Deleting patient"

    def find_all_patient(self):
        try:
            return self.patient_service.find_all_patient()

        except Exception as e:
            print(e)
            return "Error finding all patient"

    def book_appointment(self,patient_id):
        try:
            self.patient_service.book_appointment(patient_id)
            return "booked successfully"

        except ValueError as e:
            return str(e)

        except Exception as e:
            print(e)
            return "Error booking patient"

    def cancel_appointment(self):
        try:
            self.patient_service.cancel_appointment()
            return "Canceled successfully"

        except ValueError as e:
            return str(e)

        except Exception as e:
            print(e)
            return "Error Canceling patient"

    def get_medical_history(self,patient_id):
        try:
            return self.patient_service.get_medical_history(patient_id)

        except ValueError as e:
            return str(e)

        except Exception as e:
            print(e)
            return "Error getting medical history"
