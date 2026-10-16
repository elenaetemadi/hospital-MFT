from models.person import Person
from tools.validation import validation_specialty, validation_id,validation_experience


class Doctor(Person):
    doctors=[]
    def __init__(self, national_id, name, phone, address, specialty, license, experience,doctors=None):
        super().__init__(national_id, name, phone, address)
        validation_specialty(specialty)
        validation_id(license)
        validation_experience(experience)
        self.specialty = specialty
        self.license = license
        self.experience = experience
        Doctor.doctors.append(self)

    def __repr__(self):
        return f'Doctor({self.name},{self.address},{self.specialty},{self.experience})'

    def get_license(self):
        return self.license

    def set_license(self, license):
        validation_id(license)
        for doctor in Doctor.doctors:
            if doctor is not self and doctor.license==license:
                raise ValueError('License already exists')
        else:
            self.license = license

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        validation_experience(experience)
        self.experience = experience

    def get_specialty(self):
        return self.specialty

    def set_specialty(self, specialty):
        validation_specialty(specialty)
        self.specialty = specialty


    def examine(self):
        print("The doctor examined the patient")

    def prescribe(self):
        print("The doctor prescribed the patient")

    license = property(get_license, set_license)
    experience = property(get_experience, set_experience)
    specialty = property(get_specialty, set_specialty)