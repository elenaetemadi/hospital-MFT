#--------------test doctor successfully-----------
from controller.person_controller import PersonController
from models import appointment
from models.doctor import Doctor

doctor1=Doctor(1123456742,'mohsen','mohammadi','09107242144','tehran','radiology',1231231234,10)
doctor2=Doctor(1234567890,'sara','mehri','09101112525','shiraz','gyn',1212121213,11)
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


#--------------test patient controller successfully-----------
from controller.patient_controller import PatientController
from service.patient_service import PatientService
#
#
birthdate1=date(2007,7,27)
birthdate2=date(1990,5,25)
birthdate3=date(1995,11,13)
#
patientcontroller = PatientController()
print(patientcontroller.save_patient(4984486053,'elena','etemadi','09121652424','shiraz',1020304050,'flu',birthdate1))
print(patientcontroller.save_patient(4934486053,'sina','sohrabi','09121162434','isfahan',2020302450,'cancer',birthdate2))
print(patientcontroller.save_patient(4982286053,'hamed','zand','09122262424','rasht',3023404050,'diabetes',birthdate3))
# print('.'*10)
# print(patientcontroller.find_all_patient())
# print('.'*10)
# print(patientcontroller.find_by_patient_id(2020302450))
# print(patientcontroller.find_by_patient_id(6020302450))
# print('.'*10)
# print(patientcontroller.delete_by_patient_id(3023404050))
# print(patientcontroller.delete_by_patient_id(3020102450))
# print('.'*10)
#
# print(patientcontroller.book_appointment(1020304050))
# print(patientcontroller.book_appointment(1120304050))
# print('.'*10)
#
# print(patientcontroller.cancel_appointment())
# print('.'*10)
#
# print(patientcontroller.get_medical_history(2020302450))
# print(patientcontroller.get_medical_history(1020304050))
# print(patientcontroller.get_medical_history(5020302450))