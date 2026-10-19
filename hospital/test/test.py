#--------------test doctor successfully-----------
from hospital.controller.person_controller import PersonController
from hospital.models import appointment
from hospital.models.doctor import Doctor

doctor1=Doctor(1123456742,'mohsen','mohammadi','09107242144','tehran','radiology',1231231234,10)
doctor2=Doctor(1234567890,'sara','mehri','09101112525','shiraz','gyn',1212121213,11)
#
#print(doctor1)

#--------------test doctor successfully-----------
from hospital.models.patient import Patient
from datetime import date

birthdate1=date(2007,7,27)
birthdate2=date(2005,11,5)

parient1=Patient(1203405661,'elena','etemadi','09120143784','tehran',1231231234,'cold',birthdate1)
parient2=Patient(1203405661,'sahel','ebrahimi','09120145784','tehran',1234231234,'flu',birthdate2)
#
# print(parient1)
# print(parient2)

#--------------test appointment successfully-----------
from hospital.models.appointment import Appointment
from datetime import datetime

datetime1=datetime(2026,10,29,13,30,00)
datetime2=datetime(2026,11,19,10,45,00)
appointment1=Appointment(1203405661,doctor1,parient1,datetime1)
appointment2=Appointment(1243405661,doctor2,parient2,datetime2)
#
# print(appointment1)
# print(appointment2)
#
# #--------------test hospital successfully-----------
# from hospital.models.hospital import Hospital
#
# hospital1 = Hospital('mehr','tehran',doctor1,parient1,appointment1)
# hospital2 = Hospital('iran','tehran',doctor2,parient2,appointment2)
# print(hospital1)
# print(hospital2)

# #--------------test person successfully-----------
from hospital.models.person import Person
person1=Person(2121036730,'saba','sharifi','09129423477','tehran')
person2=Person(2321036730,'arash','bayat','09125423477','tehran')

#--------------test person data successfully-----------

#from hospital.data_access.person_access import PersonDa
# person_da1=PersonDa()
# person_da1.save_person(person1)
# person_da1.find_all()

#--------------test person controller successfully-----------

# from hospital.controller.person_controller import PersonController
# from hospital.service.person_service import PersonService
#
# personcontroller=PersonController()
# print(personcontroller.save_person(2121036730, 'saba', 'sharifi', '09129423477', 'tehran'))
# print(personcontroller.save_person(2321036730, 'arash', 'bayat', '09125423477', 'tehran'))
# print(personcontroller.find_all())
# print(personcontroller.delete_by_national_id(2121036730))
# print(personcontroller.find_by_national_id(2321036730))
# print(personcontroller.find_all())
