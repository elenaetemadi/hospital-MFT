from hospital.data_access.person_access import *


class PersonService:
    def __init__(self):
        self.data=PersonDa()

    def save_person(self,person):
        for persons in self.data.person_list:
            if person.national_id == persons.national_id:
                raise ValueError('national id already exists')

        self.data.save_person(person)

    def delete_by_national_id(self,national_id):
        self.data.delete_by_national_id(national_id)


    def find_by_national_id(self,national_id):
        return self.data.find_by_national_id(national_id)


    def find_all(self):
        return self.data.find_all()
