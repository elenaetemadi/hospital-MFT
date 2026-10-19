class DoctorDa:
    def __init__(self):
        self.doctor_list = []

    def save_doctor(self, doctor):
        self.doctor_list.append(doctor)

    def delete_by_license(self, license):
        for doctor in self.doctor_list:
            if doctor.license == license:
                self.doctor_list.remove(doctor)
                return
        else:
            raise ValueError('license does not exist')

    def find_by_license(self, license):
        for doctor in self.doctor_list:
            if doctor.license == license:
                return doctor
        else:
            raise ValueError('doctor not found')

    def examine(self):
        print("The doctor examined the patient")

    def prescribe(self):
        print("The doctor prescribed the patient")


    def find_all_doctors(self):
        return self.doctor_list

