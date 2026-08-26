class Parent:
    def __init__(self, real_estate, eye_colour, height):
        self.eye_colour=eye_colour
        self.height=height
        self.real_estate=real_estate

    def properties(self):
        print(f"eye_colour: {self.eye_colour}")
        print(f"real_estate: {self.real_estate}")
        print(f" height: {self.height}")

class Kid(Parent):
    def __init__(self, name, age, real_estate, eye_colour, height):
        self.name=name
        self.age=age
        #here im calling the constructor of parent class, super=parent
        super().__init__(real_estate, eye_colour, height)

    def properties(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        super().properties()

    def fav_hobby(self, hobby):
        print(f"{self.name} loves {hobby}")

#_______________________________________________________________________________-

sanaathani=Kid("Sanaathani", 12, "5 houses","Brown", "5ft")
sanaathani.properties()
            
print(f"{sanaathani.name} inherited {sanaathani.real_estate}")

print("Is Kid a subclass of Parent?", issubclass(Kid, Parent))

sanaathani.fav_hobby("playing football")