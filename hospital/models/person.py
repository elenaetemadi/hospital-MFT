from tools.validation import validation_id, validation_name, validation_phone, validation_address

class Person:
    def __init__(self, national_id, name,family, phone, address):
        self.national_id = national_id
        self.name = name
        self.family = family
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f'{self.national_id} {self.name} {self.family} {self.phone} {self.address}'
    def get_national_id(self):
        return self.__national_id

    def set_national_id(self, national_id):
        validation_id(national_id)
        self.__national_id = national_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        validation_name(name)
        self.__name = name

    def get_family(self):
        return self.__family

    def set_family(self, family):
        validation_name(family)
        self.__family = family

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        validation_phone(phone)
        self.__phone = phone

    def get_address(self):
        return self.__address

    def set_address(self, address):
        validation_address(address)
        self.__address = address

    national_id = property(get_national_id, set_national_id)
    name = property(get_name, set_name)
    family = property(get_family, set_family)
    phone = property(get_phone, set_phone)
    address = property(get_address, set_address)

