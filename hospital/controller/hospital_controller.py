

class HospitalController:
    def __init__(self,hospital_service):
        self.hospital_service = hospital_service

    def find_all_patient(self):
        return self.hospital_service.find_all_patient()

    def find_all_doctor(self):
        return self.hospital_service.find_all_doctor()

    def find_all_appointment(self):
        return self.hospital_service.find_all_appointment()