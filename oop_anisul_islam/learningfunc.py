class StudentReg:
    def __init__(self, name, school):
        self.name = name
        self.school = school
    def registration(self):
        print(f"Hi {self.name}, Your details sucessfully submited")
    def id_card(self):
        print(f"Hello {self.name}, Id card printed")
    def bye(self):
        print(f"Bye {self.name}, Your registration completed")
        
    
    # request.post(url, details)

munu = StudentReg("Golumulu", "DIU")
munu.registration()
munu.id_card()
munu.bye()


