#Hierarchical Inheritance

class Shape:
    def __init__(self, dim1, dim2) -> None:
        self.dim1 = dim1
        self.dim2 = dim2
        
    def area(self):
        print("I am area method of shape class")
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("The area of Triangle is {}".format(area))
class Rectangle(Shape):
    def area(self):
        area = self.dim1*self.dim2
        print("The area of the rectangle is {}".format(area))
        
        
#multilevel inheritance
class A:
    def display1(self):
        print("I am inside A class")
class B(A):
    def display2(self):
        print("I am inside B class")
class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")
        
        

#multiple_inheritance
class A:
    def display1(self):
        print("I am inside A class")
class B:
    def display2(self):
        print("I am inside B class")
class C(A, B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")
testing = C()
# testing.display1()
# testing.display2()
testing.display3()
