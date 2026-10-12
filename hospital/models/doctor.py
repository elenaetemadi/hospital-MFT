from person import Person

class Doctor(Person):
    def __init__(self, national_id, name, phone, address, specialty, license, experience):
        super().__init__(national_id, name, phone, address)
        self.specialty = specialty
        self.license = license
        self.experience = experience

    def __repr__(self):
        return f'Doctor({self.name},{self.address},{self.specialty},{self.experience})'

    def get_license(self):
        return self.__license

    def set_license(self, license):
        self.__license = license

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience

    def get_specialty(self):
        return self.__specialty

    def set_specialty(self, specialty):
        self.__specialty = specialty


    def examine(self):
        print("The doctor examined the patient")

    def prescribe(self):
        print("The doctor prescribed the patient")

    license = property(get_license, set_license)
    experience = property(get_experience, set_experience)
    specialty = property(get_specialty, set_specialty)