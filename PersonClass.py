
class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__phone)


class Customer(Person):

    def __init__(self, name, address, phone, cust_number, mailing_list):
        Person.__init__(self, name, address, phone)

        self.__cust_number = cust_number
        self.__mailing_list = mailing_list

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__phone)
        print(self.__cust_number)
        print(self.__mailing_list)
