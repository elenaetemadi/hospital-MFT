
class HospitalService:
    def __init__(self,hospital_da):
        self.data=hospital_da

    def find_all_patient(self):
        return self.data.find_all_patient()

    def find_all_doctor(self):
        return self.data.find_all_doctor()

    def find_all_appointment(self):
        return self.data.find_all_appointment()