from hospital.data_access.doctor_access import *

class DoctorService:
    def __init__(self):
        self.data=DoctorDa()

    def save_doctor(self, doctor):
        for doctors in self.data.doctor_list:
            if doctor.license==doctors.license:
                raise ValueError("license is already exists")

        self.data.save_doctor(doctor)

    def delete_by_license(self, license):
        self.data.delete_by_license(license)


    def find_by_license(self, license):
        return self.data.find_by_license(license)

    def examine(self):
        self.data.examine()

    def prescribe(self):
        self.data.prescribe()

    def find_all_doctors(self):
        return self.data.find_all_doctors()
