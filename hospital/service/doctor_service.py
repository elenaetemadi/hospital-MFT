from models.appointment import Appointment
from models.doctor import Doctor


class DoctorService:
    def __init__(self,doctor_da,appointment_service):
        self.data=doctor_da
        self.appointment_service=appointment_service

    def save_doctor(self, doctor):
        for doctors in self.data.doctor_list:
            if doctor.license==doctors.license or doctor.national_id==doctors.national_id:
                raise ValueError("national id/license is already exists")

        self.data.save_doctor(doctor)

    def delete_by_license(self, license):
        self.data.delete_by_license(license)

    def find_by_license(self, license):
        return self.data.find_by_license(license)

    def examine(self,license,appointment_id):
        appointments=self.appointment_service.find_all_appointments()
        for appointment in appointments:
            if (appointment.appointment_id==appointment_id and appointment.doctor.license==license):
                self.appointment_service.delete_appointment(appointment_id)
                return "Patient examined successfully"
        else:
            raise ValueError("no appointment found for this doctor")

    def prescribe(self):
        return self.data.prescribe()

    def find_all_doctors(self):
        return self.data.find_all_doctors()

    def find_todays_appointments(self,license):
        return self.appointment_service.find_today_appointments(license)