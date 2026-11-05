from models import appointment
from models.person import Person


class AppointmentDa:
    def __init__(self,appointment_list):
        self.appointment_list=appointment_list

    def save_appointment(self,appointment):
        self.appointment_list.append(appointment)

    def delete_appointment(self,appointment_id):
        for appointments in self.appointment_list:
            if appointments.appointment_id == appointment_id:
                self.appointment_list.remove(appointments)
                return
        else:
            raise ValueError("appointment id does not exist")

    def find_by_appointment_id(self,appointment_id):
        for appointments in self.appointment_list:
            if appointments.appointment_id == appointment_id:
                return appointments
        else:
            raise ValueError("appointment not found")

    def find_all_appointments(self):
        return self.appointment_list

    def find_doctor(self,name,family):
        result=[
            appointment for appointment in self.appointment_list
            if appointment.doctor.family == family
            and appointment.doctor.name == name
        ]
        if not result:
            raise ValueError("appointment not found")

        return result

    def find_patient(self,name,family):
        result = [
            appointment for appointment in self.appointment_list
            if appointment.patient.family == family
            and appointment.patient.name == name
        ]
        if not result:
            raise ValueError("appointment not found")

        return result
