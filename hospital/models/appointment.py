
from tools.validation import validation_id, validation_doctor,validation_patient,validation_date


class Appointment:
    appointments=[]
    def __init__(self, appointment_id, doctor, patient, date):
        validation_id(appointment_id)
        validation_patient(patient)
        validation_date(date)
        validation_doctor(doctor)
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.date = date
        Appointment.appointments.append(self)

    def get_appointment_id(self):
        return self.appointment_id

    def set_appointment_id(self, appointment_id):
        validation_id(appointment_id)
        for appointment in Appointment.appointments:
            if appointment is not self and appointment.appointment_id == appointment_id:
                raise ValueError('appointment_id already exists')
        else:
            self.appointment_id = appointment_id

    def __repr__(self):
        return f'Appointment({self.appointment_id},{self.doctor},{self.patient},{self.date})'

    def cancel(self, appointment_id):
        for appointment in Appointment.appointments:
            if appointment.appointment_id == appointment_id:
                Appointment.appointments.remove(appointment)
                print('cancel')
                break
        else:
            raise ValueError('appointment_id does not exist')