from datetime import date, timedelta

from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from models.hospital import Hospital


print("\n--- Testing Patient ---")

patient = Patient(
    "12345678", "Ali Ahmadi", "09123456790", "Tehran",
    "23456789", "Flu", date(2000, 5, 10)
)

print(patient)
print(patient.get_patient_id())
print(patient.get_disease())
patient.set_disease("Cold")
print(patient.get_disease())
print(patient.get_birth_date())


print("\n--- Testing Doctor ---")

doctor = Doctor(
    "87654321", "Sara Ahmadi", "09123456864", "Tehran",
    "Cardiology", "34567890", 5
)

print(doctor)
print(doctor.get_license())
print(doctor.get_experience())
print(doctor.get_specialty())

doctor.examine()
doctor.prescribe()


print("\n--- Testing Appointment ---")

appointment = Appointment(
    "45678901",
    doctor,
    patient,
    date.today() + timedelta(days=1)
)

print(appointment)
print(appointment.get_appointment_id())
print(Appointment.appointments)


print("\n--- Testing Hospital ---")

hospital = Hospital("Mehr Hospital", "Tehran", [], [], [])

hospital.set_patient(patient)

print(hospital.get_name())
print(hospital.get_address())
print(hospital.get_patient())
print(hospital.get_doctors())
print(hospital.get_appointment())


print("\n--- Testing Cancel Appointment ---")

patient.cancel_appointment()
print(Appointment.appointments)
