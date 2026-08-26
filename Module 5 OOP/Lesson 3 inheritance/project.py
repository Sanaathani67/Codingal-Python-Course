class Vehicle:
    def __init__(self, fuel, max_speed):
        self.fuel = fuel
        self.max_speed = max_speed

    def show_details(self):
        print("Fuel:", self.fuel)
        print("Max Speed:", self.max_speed, "km/h")

class Car(Vehicle):

    def __init__(self, model, seats, fuel, max_speed):
        self.model = model
        self.seats = seats
        super().__init__(fuel, max_speed)

    def show_details(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        super().show_details()

    def fuel_type(self, fuel):
        print(self.model, "uses", fuel)

my_car = Car("City Rider", 5, "petrol/diesel", 180)

my_car.show_details()
my_car.fuel_type("petrol/diesel")

print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))