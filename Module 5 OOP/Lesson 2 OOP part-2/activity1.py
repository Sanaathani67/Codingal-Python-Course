class Calculator:
    #this is called imm after object is created
    def __init__(self, a, b):
        print("Object of class calculator is being created now! in constructor method")
        self.a=a
        self.b=b
    #a funtion that is defined in a class is called a method
    def add(self):
        return self.a +self.b#self represents the object ur using
    def subtract(self):
        return self.a-self.b
    def __del__(self):#when the program ends
        print("Object is now being destroyed! in destructor method")
    #_______________________________________________________________

calc=Calculator(10, 50)
print("The a property holds:", calc.a)
print("The b property holds:", calc.b)

print(calc.add())
print(calc.subtract())

print("Prgrm ends here!")