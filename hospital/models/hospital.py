from appointment import Appointment
from doctor import Doctor
from patient import Patient


class Hospital:
    def __init__(self, name, address, doctors, patients, appointments):
        self.name = name
        self.address = address
        self.doctors = doctors if doctors else []
        self.patient = patients if patients else []
        self.appointments = appointments

    def get_patient(self):
        return self.patient

    def set_patient(self, patient):
        if isinstance(patient, Patient):
            self.patient.append(patient)

    def get_appointment(self):
        return self.appointments

    def set_appointment(self, appointment):
        if isinstance(appointment, Appointment):
            self.appointments.append(appointment)

    def get_doctors(self):
        return self.doctors

    def set_doctors(self, doctor):
        if isinstance(doctor, Doctor):
            self.doctors.append(doctor)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    patient = property(get_patient, set_patient)
    appointment = property(get_appointment, set_appointment)
    doctors = property(get_doctors, set_doctors)
