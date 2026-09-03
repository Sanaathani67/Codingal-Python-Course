class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())


class Car:
    def __init__(self, color):
        self.colour = color

my_car = Car("red")


class Counter:
    count = 0

    def __init__(self):
        Counter.Counter += 1