class Phone:
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")
class Samsung(Phone):
    
    
    def call(Phone.call):
        print("This is extra")
    def photo(self):
        print("You can take photo")
        
        
s = Samsung()
s.message()
s.call()
print(issubclass(Phone,Samsung))