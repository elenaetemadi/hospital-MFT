from hospital.service.doctor_service import *
from hospital.models.doctor import Doctor

class DoctorController:
    def __init__(self):
        self.doctor_service = DoctorService()

    def save_doctor(self,national_id, name,family,phone, address, specialty, license, experience):
        try:
            doctor=Doctor(national_id, name, family, phone, address, specialty, license, experience)
            self.doctor_service.save_doctor(doctor)
            return "saved Doctor successfully"
        except Exception as e:
            print("e")
            return "Error Saving doctor"

    def delete_by_license(self,license):
        try:
            self.doctor_service.delete_by_license(license)
            return "deleted doctor successfully"
        except Exception as e:
            print("e")
            return "Error Deleting doctor"

    def find_by_license(self,license):
        try:
            self.doctor_service.find_by_license(license)
            return "found doctor successfully"
        except Exception as e:
            print("e")
            return "Error finding doctor"

    def examine(self):
        try:
            self.doctor_service.examine()
            return "examined doctor successfully"
        except Exception as e:
            print("e")
            return "Error examining doctor"

    def prescribe(self):
        try:
            self.doctor_service.prescribe()
            return "prescribed doctor successfully"
        except Exception as e:
            print("e")
            return "Error prescribing doctor"
