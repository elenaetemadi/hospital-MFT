class Person:
    def __init__(self, national_id, name, phone, address):
        self.__national_id = national_id
        self.name = name
        self.phone = phone
        self.address = address

    def get_national_id(self):
        return self.__national_id

    def set_national_id(self, national_id):
        self.__national_id = national_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    national_id = property(get_national_id, set_national_id)
    name = property(get_name, set_name)
    phone = property(get_phone, set_phone)
    address = property(get_address, set_address)

