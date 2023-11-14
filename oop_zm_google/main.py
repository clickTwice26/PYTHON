
class Person:
    def __init__(self, person_name:str, year_of_birth:int, ht_inches:int=None) -> None: #class properties #constructor
        self.__name = person_name
        self.__date_of_birth = year_of_birth
        self.__height = ht_inches
        self.abc = None
    def get_year_of_birth(self):
        return self.__date_of_birth
    def return_details(self):

        return f"""\tName: {self.__name}\n\tDate of birth: {self.__date_of_birth}\n\tHeight: {self.__height if self.__height is not None else 'Invalid'}
        """
    def set_name(self, new_name):
        if self.__has_any_number(new_name):
            print("Sorry person name can't have number")
            return
        else:
            self.name = new_name
    def __has_any_number(self, string):
        return "0" in string

a_person = Person("Giyan", "asd", "123")


person_list = [Person("Giyan", 1990), Person("Nobita", 1994, 22), Person("Giyan", 1943), Person("Giyan", 1988)]

# print(person_list)

for person in person_list:
    if person.get_year_of_birth() >= 1990:
        print(person.return_details())

# print(b_person.get_name())
