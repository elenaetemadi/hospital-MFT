
class PatientDa:
    def __init__(self,patient_list,appointment_list):
        self.patient_list = patient_list
        self.appointment_list = appointment_list

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

    def get_medical_history(self, patient_id):
        patient=self.find_by_patient_id(patient_id)
        return patient.disease
