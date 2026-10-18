from service.person_service import PersonService
from models.person import Person

class PersonController:
    def __init__(self):
        self.person_service = PersonService()

    def save_person(self,national_id, name,family, phone, address):
        try:
            person = Person(national_id, name, family, phone, address)
            self.person_service.save_person(person)
            return "Saved person"
        except Exception as e:
            print(e)
            return "Error saving person"

    def delete_by_national_id(self,national_id):
        try:
            self.person_service.delete_by_national_id(national_id)
            return "Deleted person"
        except Exception as e:
            print(e)
            return "Error deleting person"

    def find_by_national_id(self,national_id):
        try:
            return self.person_service.find_by_national_id(national_id),"Found person"
        except Exception as e:
            print(e)
            return "Error finding person"

    def find_all(self):
        try:
            return self.person_service.find_all()

        except Exception as e:
            print(e)
            return "Error finding all persons"