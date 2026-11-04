from data_access.appointment_access import *

class AppointmentService:
    def __init__(self):
        self.data=AppointmentDa()

    def save_appointment(self,appointment):
        for appointments in self.data.appointment_list:
            if appointments.appointment_id == appointment.appointment_id:
                raise ValueError("appointment id already exists")
        self.data.save_appointment(appointment)

    def delete_appointment(self,appointment_id):
        return self.data.delete_appointment(appointment_id)

    def find_by_appointment_id(self,appointment_id):
        return self.data.find_by_appointment_id(appointment_id)

    def find_all_appointments(self):
        return self.data.find_all_appointments()

    def find_doctor(self,name,family):
        return self.data.find_doctor(name,family)

    def find_patient(self,name,family):
        return self.data.find_patient(name,family)

