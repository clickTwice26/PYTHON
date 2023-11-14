def student(*details):
    print(details)
student("101","Anis", 3.7)

class Student:
    roll = ""
    gpa  = ""
rahim = Student()
# print(isinstance(rahim,Student))
rahim.roll = 101
rahim.gpa = 3.7
print(f"Roll: {rahim.roll}, GPA: {rahim.gpa}")
karim = Student()
karim.roll = 102
karim.gpa = 3.33
print(f"Karims Roll:{karim.roll}, GPA: {karim.gpa}")