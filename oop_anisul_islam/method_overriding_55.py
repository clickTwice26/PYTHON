class Phone:
    def __init__(self) -> None:
        print("I am in Phone class")
class Samsung(Phone):
    #init method chole esheche phone er
    def __init__(self) -> None:
        super().__init__()
        print("I am in Samsung class") #method overriding
test = Samsung()