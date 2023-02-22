
class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def print_person(self):
        print('Name:', self.__name)
        print('Address:', self.__address)
        print("Phone:", self.__phone)


class Customer(Person):

    def __init__(self, name, address, phone, cust_number, mailing_list):
        Person.__init__(self, name, address, phone)

        self.__cust_number = cust_number
        self.__mailing_list = mailing_list

    def print_person(self):

        Person.print_person(self)
        print('Customer Number:', self.__cust_number)
        if self.__mailing_list:
            print("On Mailing list: Yes")
        else:
            print("On Mailing list: Yes")
