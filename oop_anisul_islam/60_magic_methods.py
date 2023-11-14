#video:https://www.youtube.com/watch?v=AcWqcjTcxuI&list=PLgH5QX0i9K3rz5XqMsTk41_j15_6682BN&index=61


class Bike:
    def __init__(self,name, color) -> None:
        self.name = name
        self.color = color
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.color == other.color
    
    def __str__(self) -> str:
        return f"Name = {self.name}, Color = {self.color}" 
    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")
        
bike1 = Bike("Yamaha R15", "Blue")
bike2 = Bike("Yamaha R15", "Blue")


print(bike1==bike2)







