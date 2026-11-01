
class PatientDa:
    def __init__(self):
        self.patient_list = []

    def save_patient(self, patient):
        self.patient_list.append(patient)

    def find_by_patient_id(self, patient_id):
        for patient in self.patient_list:
            if patient.patient_id == patient_id:
                return patient

        else:
            raise ValueError('patient_id does not exist')

    def delete_by_patient_id(self, patient_id):
        for patient in self.patient_list:
            if patient.patient_id == patient_id:
                self.patient_list.remove(patient)
                return

        raise ValueError('patient does not exist')

    def find_all_patient(self):
        return self.patient_list

    def book_appointment(self, patient_id):
        for patient in self.patient_list:
            if patient.patient_id == patient_id:
                my_patient = patient
                print(f"The patient booked the appointment for {my_patient}")
                return
        else:
            raise ValueError('patient_id does not exist')

    def cancel_appointment(self):
        print("The patient cancelled the appointment")

    def get_medical_history(self, patient_id):
        for patient in self.patient_list:
            if patient.patient_id == patient_id:
                return patient.disease
        else:
            raise ValueError('patient_id does not exist')