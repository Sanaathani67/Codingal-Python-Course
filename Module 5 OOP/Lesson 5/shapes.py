from abc import ABC, abstractmethod

#ABC- abstract base class/abstract parent class

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

#--------------------------------------------------------

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
            print("Area of a circle =", 22/7*self.radius*self.radius)

#--------------------------------------------------------------------


class Rectangle(Shape):
    def __init__(self, l, b):
        self.length=l
        self.breadth=b

    def area(self):
        print("Area of a rectangle =",self.length*self.breadth)


#=--------------------------------------------------------



#without implementing area()method for these 2 child classes,
#we were not able to create the objects for them

c=Circle(5)
c.area()

r=Rectangle(10, 20)
r.area()