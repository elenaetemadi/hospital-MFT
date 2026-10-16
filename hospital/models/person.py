from tools.validation import validation_id, validation_name, validation_phone, validation_address

class Person:
    persons=[]
    def __init__(self, national_id, name, phone, address):
        validation_id(national_id)
        validation_name(name)
        validation_phone(phone)
        validation_address(address)
        self.national_id = national_id
        self.name = name
        self.phone = phone
        self.address = address
        Person.persons.append(self)

    def get_national_id(self):
        return self.national_id

    def set_national_id(self, national_id):
        validation_id(national_id)
        for person in self.persons:
            if person is not self and person.national_id == national_id:
                raise ValueError("national id already exists")
        else:
            self.national_id = national_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        validation_name(name)
        self.name = name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        validation_phone(phone)
        for person in self.persons:
            if person.phone == phone:
                raise ValueError("phone already exists")
        else:
            self.phone = phone

    def get_address(self):
        return self.address

    def set_address(self, address):
        validation_address(address)
        self.address = address

    national_id = property(get_national_id, set_national_id)
    name = property(get_name, set_name)
    phone = property(get_phone, set_phone)
    address = property(get_address, set_address)

