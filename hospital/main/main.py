from view.view import HospitalView

from data_access.hospital_access import HospitalDa
from data_access.patient_access import PatientDa
from data_access.doctor_access import DoctorDa
from data_access.appointment_access import AppointmentDa

from service.patient_service import PatientService
from service.doctor_service import DoctorService
from service.appointment_service import AppointmentService
from service.hospital_service import HospitalService

from controller.patient_controller import PatientController
from controller.doctor_controller import DoctorController
from controller.appointment_controller import AppointmentController
from controller.hospital_controller import HospitalController



hospital_data = HospitalDa()


patient_data = PatientDa(hospital_data.patient_list)
doctor_data = DoctorDa(hospital_data.doctor_list)
appointment_data = AppointmentDa(hospital_data.appointment_list)


appointment_service = AppointmentService(appointment_data,patient_data,doctor_data)
patient_service = PatientService(patient_data, appointment_service)
doctor_service = DoctorService(doctor_data,appointment_service)
hospital_service = HospitalService(hospital_data)


patient_controller = PatientController(patient_service)
doctor_controller = DoctorController(doctor_service)
appointment_controller = AppointmentController(appointment_service)
hospital_controller = HospitalController(hospital_service)

# Run View
view = HospitalView(patient_controller,doctor_controller,appointment_controller,hospital_controller)

view.window.mainloop()