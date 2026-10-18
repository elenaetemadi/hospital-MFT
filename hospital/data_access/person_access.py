class PersonDa:
    def __init__(self):
        self.person_list=[]

    def save_person(self,person):
        self.person_list.append(person)

    def delete_by_national_id(self,national_id):
        for persons in self.person_list:
            if persons.national_id == national_id:
                self.person_list.remove(persons)
                return
        else:
            raise ValueError('national id does not exist')

    def find_by_national_id(self,national_id):
        for person in self.person_list:
            if person.national_id == national_id:
                return person
        else:
            raise ValueError('Person not found')

    def find_all(self):
        return self.person_list
