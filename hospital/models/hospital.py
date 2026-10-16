from tools.validation import validation_patient,validation_appointment,validation_doctor,validation_name,validation_address
from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment

class Hospital:
    def __init__(self, name, address, doctors, patients, appointments):
        self.name = name
        self.address = address
        self.doctors = Doctor.doctors
        self.patient = patients if patients is not None else []
        self.appointments = Appointment.appointments

    def get_patient(self):
        return self.patient

    def set_patient(self, patient):
        validation_patient(patient)
        for p in self.patient:
            if p.get_patient_id() == patient.get_patient_id():
                raise ValueError("Patient id already exists")
        self.patient.append(patient)

    def get_appointment(self):
        return self.appointments

    def set_appointment(self, appointment):
        validation_appointment(appointment)
        self.appointments.append(appointment)

    def get_doctors(self):
        return self.doctors

    def set_doctors(self, doctor):
        validation_doctor(doctor)
        self.doctors.append(doctor)

    def get_name(self):
        return self.name

    def set_name(self, name):
        validation_name(name)
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        validation_address(address)
        self.address = address

    patient = property(get_patient, set_patient)
    appointment = property(get_appointment, set_appointment)
    doctors = property(get_doctors, set_doctors)
