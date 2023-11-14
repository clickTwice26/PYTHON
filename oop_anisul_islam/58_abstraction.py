"""
Object Oriented Programming

1.Class
2.Object
3.Inheritance
4.Abstraction
5.Encapsulation
6.Polymorphism

"""
from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self, dim1, dim2) -> None:
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod 
    def area(self):
        # print("Shape has no area")
        pass
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("The area of Triangle is {}".format(area))
class Rectangle(Shape):
    def area(self):
        area = self.dim1*self.dim2
        print("The area of the rectangle is {}".format(area))
        
s1 = Shape(10, 20)
s1.area()
t1 = Triangle(20,30)
t1.area()
t2 = Rectangle(20,30).area()
