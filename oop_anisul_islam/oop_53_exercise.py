class TriangleArea:
    def __init__(self,base,height) -> None:
        self.base = base 
        self.height = height
    def calculate_area(self):
        area = 0.5*self.base*self.height
        return area
    
t1 = TriangleArea(10,20)
print(t1.calculate_area())
t2 = TriangleArea(20,30)
print(t2.calculate_area())


"""

perfectly done 4
"""