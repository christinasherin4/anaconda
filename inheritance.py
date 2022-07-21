class Mammal:
    def bark(self):
        print("bark")

class Dog(Mammal):
    pass

    
class Cat(Mammal):
    def be_annoying(self):
        print("annoying")
   
   
cat1 = Cat()
cat1.be_annoying()
dog1 = Dog()
dog1.bark()
