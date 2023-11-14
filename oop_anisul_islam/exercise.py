"""
t1: base = 10 height = 20
t2: base = 20 height = 30
eder area ber kore dibi
using class with calculate_area() function

"""
class area:
    def __init__(self,base,height) -> None:
        self.base = base
        self.height = height
    def calculate_area(self):
        triangle_area = 0.5 * self.base * self.height
        print(f"triangle_area_ = {triangle_area}")
t1 = area(10,20)
t1.calculate_area()
t2 = area(20,30)
t2.calculate_area()
        