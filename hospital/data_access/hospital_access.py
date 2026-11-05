from models.hospital import Hospital


class HospitalDa:
    def __init__(self):
        self.hospital_list=[]
        self.patient_list=[]
        self.appointment_list=[]
        self.doctor_list=[]

    def find_all_patient(self):
        return self.patient_list

    def find_all_doctor(self):
        return self.doctor_list

    def find_all_appointment(self):
        return self.appointment_list