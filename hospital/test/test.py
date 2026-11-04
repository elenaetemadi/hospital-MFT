#--------------test doctor successfully-----------
# from controller.person_controller import PersonController
# from models import appointment
# from models.doctor import Doctor
# from models.patient import Patient
#
# doctor1=Doctor(1123456742,'mohsen','mohammadi','09107242144','tehran','radiology',1231231234,10)
# doctor2=Doctor(1234567890,'sara','mehri','09101112525','shiraz','gyn',1212121213,11)
#
#print(doctor1)

#--------------test doctor successfully-----------
# from models.patient import Patient
from datetime import date
#
# birthdate1=date(2007,7,27)
# birthdate2=date(2005,11,5)
#
# parient1=Patient(1203405661,'elena','etemadi','09120143784','tehran',1231231234,'cold',birthdate1)
# parient2=Patient(1203405661,'sahel','ebrahimi','09120145784','tehran',1234231234,'flu',birthdate2)
#
# print(parient1)
# print(parient2)

#--------------test appointment successfully-----------
from models.appointment import Appointment
from datetime import datetime

#datetime1=datetime(2026,10,29,13,30,00)
#datetime2=datetime(2026,11,19,10,45,00)
#appointment1=Appointment(1203405661,doctor1,parient1,datetime1)
#appointment2=Appointment(1243405661,doctor2,parient2,datetime2)
#
# print(appointment1)
# print(appointment2)
#
# #--------------test hospital successfully-----------
# from models.hospital import Hospital
#
# hospital1 = Hospital('mehr','tehran',doctor1,parient1,appointment1)
# hospital2 = Hospital('iran','tehran',doctor2,parient2,appointment2)
# print(hospital1)
# print(hospital2)

# #--------------test person successfully-----------
from models.person import Person
#person1=Person(2121036730,'saba','sharifi','09129423477','tehran')
#person2=Person(2321036730,'arash','bayat','09125423477','tehran')

#--------------test person data successfully-----------

#from hospital.data_access.person_access import PersonDa
# person_da1=PersonDa()
# person_da1.save_person(person1)
# person_da1.find_all()

#--------------test person controller successfully-----------

# from controller.person_controller import PersonController
# from service.person_service import PersonService
# #
# personcontroller=PersonController()
# print(personcontroller.save_person(2121036730, 'saba', 'sharifi', '09129423477', 'tehran'))
# print(personcontroller.save_person(2321036730, 'arash', 'bayat', '09125423477', 'tehran'))
# print(personcontroller.find_all())
# print(personcontroller.delete_by_national_id(2121036730))
# print(personcontroller.delete_by_national_id(2121036731))
# print(personcontroller.find_by_national_id(2321036730))
# print(personcontroller.find_all())

#--------------test doctor controller successfully-----------
# from controller.doctor_controller import DoctorController
# from service.doctor_service import DoctorService
#
# doctorcontroller = DoctorController()
# print(doctorcontroller.save_doctor(2121036730, 'saba', 'sharifi', '09129423477', 'tehran','psychiatry',2121036731,10))
# print(doctorcontroller.save_doctor(2321036730, 'arash', 'bayat', '09125423477', 'tehran','urology',2121036734,5))
# print(doctorcontroller.find_all_doctors())
# print(doctorcontroller.find_by_license(2121036734))
# print(doctorcontroller.find_by_license(2121036737))
#
# print(doctorcontroller.delete_by_license(2121036734))
# print(doctorcontroller.delete_by_license(2121036737))
#
# print(doctorcontroller.find_all_doctors())

#--------------test appointment controller successfully-----------
# from controller.appointment_controller import AppointmentController
# from service.appointment_service import AppointmentService
#
# date_times1=datetime(2026,12,14,13,30)
# date_times2=datetime(2027,12,14,17,15)
# date_times3=datetime(2026,10,14,18,15)
# date_times4=datetime(2027,12,24,10,30)
# bith_date1=date(1990,12,2)
# bith_date2=date(2001,10,14)
# bith_date3=date(1990,5,27)
# doctor1=Doctor(2121036730, 'saba', 'sharifi', '09129423477', 'tehran','psychiatry',2121036731,10)
# doctor2=Doctor(2321036730, 'arash', 'bayat', '09125423477', 'tehran','urology',2121036734,5)
# patient1=Patient(4980486053,'sina','alipour','09129423478', 'tehran',1212121212,'flu',bith_date1)
# patient2=Patient(4980484053,'roya','alizadeh','09129429478', 'rasht',1212123212,'flu',bith_date2)
#
# appointmentcontroller = AppointmentController()
#
# print(appointmentcontroller.save_appointment(1234567890,doctor1,patient1,date_times1))
# print(appointmentcontroller.save_appointment(1314151617,doctor2,patient2,date_times2))
# print(appointmentcontroller.save_appointment(1234567890,doctor1,patient1,date_times3))
# print(appointmentcontroller.save_appointment(1214567890,doctor2,patient2,date_times4))
# print('.'*50)
# print(appointmentcontroller.find_all_appointments())
# print('.'*50)
# print(appointmentcontroller.find_by_appointment_id(1214567890))
# print(appointmentcontroller.find_by_appointment_id(1214568890))
# print('.'*50)
# print(appointmentcontroller.delete_appointment(1214567890))
# print('.'*50)
# print(appointmentcontroller.find_all_appointments())
# print('.'*50)
# print(appointmentcontroller.delete_appointment(9214567890))
# print('.'*50)
# print(appointmentcontroller.find_doctor('arash','bayat'))
# print('.'*50)
# print(appointmentcontroller.find_patient('sina','alipour'))





