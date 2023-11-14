
class Student:
    roll = ""
    gpa  = ""
    
    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
    
    
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.roll}")
rahim = Student()
# print(isinstance(rahim,Student))
rahim.roll = 101
rahim.gpa = 3.7
rahim.display()
karim = Student()
karim.roll = 102
karim.gpa = 3.33
karim.display()