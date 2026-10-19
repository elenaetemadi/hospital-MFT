from hospital.models.person import Person
from hospital.tools.validation import *

class Doctor(Person):
    def __init__(self, national_id, name,family,phone, address, specialty, license, experience):
        super().__init__(national_id, name,family, phone, address)
        self.specialty = specialty
        self.license = license
        self.experience = experience

    def __repr__(self):
        return f'Doctor({self.national_id},{self.name},{self.family},{self.phone},{self.address},{self.specialty},{self.license}{self.experience})'

    def get_license(self):
        return self.__license

    def set_license(self, license):
        validation_id(license)
        self.__license = license

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        validation_experience(experience)
        self.__experience = experience

    def get_specialty(self):
        return self.__specialty

    def set_specialty(self, specialty):
        validation_specialty(specialty)
        self.__specialty = specialty

    license = property(get_license, set_license)
    experience = property(get_experience, set_experience)
    specialty = property(get_specialty, set_specialty)