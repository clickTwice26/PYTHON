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
t1 = Triangle(20,30)
t1.area()
t2 = Rectangle(20,30).area()
