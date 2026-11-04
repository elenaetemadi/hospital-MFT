from models.person import Person


class AppointmentDa:
    def __init__(self):
        self.appointment_list=[]

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
        doctors_list=[]
        for appointments in self.appointment_list:
            if appointments.doctor.family == family and appointments.doctor.name == name:
                return appointments
        else:
            raise ValueError("appointment not found")


    def find_patient(self,name,family):
        for appointments in self.appointment_list:
            if appointments.patient.family == family and appointments.patient.name == name:
                return appointments
        else:
            raise ValueError("appointment not found")

