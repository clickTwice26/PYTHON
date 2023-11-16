
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
            self.__name = new_name
    def __has_any_number(self, string):
        return "0" in string
    def get_name(self):
        return self.__name
class Student(Person):
    def __init__(self,person_name, year_of_birth,email_id, student_id):
        super().__init__(person_name, year_of_birth)
        self.id = student_id
        self.email_id = email_id
    def return_details(self):
        return f"Name:{self.get_name()} Email: {self.email_id}"
    def __str__(self):
        return self.return_details()

    # def __repr__(self):
    #     return "Representation"
# person = Student("Giyan", 1000, "testing@gmail.com", "123123")
# print(person.return_details())
# print(person)
# person.set_name("Nabita")
# print(person.return_details())
class Teacher(Person):
    def __init__(self, person_name, year_of_birth, department):
        super().__init__(person_name, year_of_birth)
        self.dept = department


new_person_list = [
    Person("Zukernine", 1990),
    Student("S", 2000,"testing@gmail.com","12323"),
    Teacher("Teachers", 1990,  "CSE")
]
for p in new_person_list:
    print(p.return_details())



class PlainClass:
    pass
abc = PlainClass()
abc.age = 30
abc.name = "Movie"
print(abc.age)