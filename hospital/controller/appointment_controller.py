
from models.appointment import Appointment

class AppointmentController:
    def __init__(self,appointment_service):
        self.appointment_service = appointment_service

    def save_appointment(self,appointment_id, doctor, patient, appointment_datetime):
        try:
            appointment=Appointment(appointment_id, doctor, patient, appointment_datetime)
            self.appointment_service.save_appointment(appointment)
            return "saved appointment successfully"
        except Exception as e:
            print(e)
            return "Error Saving appointment"

    def delete_appointment(self,appointment_id):
        try:
            self.appointment_service.delete_appointment(appointment_id)
            return "deleted appointment successfully"

        except ValueError as e:
            return str(e)

        except Exception as e:
            print(e)
            return "Error Deleting appointment"

    def find_by_appointment_id(self,appointment_id):
        try:
            return self.appointment_service.find_by_appointment_id(appointment_id),"found appointment successfully"

        except ValueError as e:
            return str(e)

        except Exception as e:
            print(e)
            return "Error finding appointment"

    def find_all_appointments(self):
        try:
            return self.appointment_service.find_all_appointments()
        except Exception as e:
            print(e)
            return "Error finding all appointments"

    def find_doctor(self,name,family):
        try:
            return self.appointment_service.find_doctor(name,family)

        except ValueError as e:
            return str(e)

        except Exception as e:
            print(e)
            return "Error finding appointment with this doctor"

    def find_patient(self,name,family):
        try:
            return self.appointment_service.find_patient(name,family)

        except ValueError as e:
            return str(e)

        except Exception as e:
            print(e)
            return "Error finding appointment for this patient"

    def find_patient_appointments(self, patient_id):
        try:
            return self.appointment_service.find_patient_appointments(patient_id)
        except Exception as e:
            print(e)
            return "Error finding patient appointments"

    def find_today_appointments(self, license):
        try:
            return self.appointment_service.find_today_appointments(license)
        except Exception as e:
            print(e)
            return "Error finding today's appointments"