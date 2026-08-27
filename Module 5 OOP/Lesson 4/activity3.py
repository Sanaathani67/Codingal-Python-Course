class Coordinate:
    def __init__(self, x, y):#(2, 5)
        self.x=x
        self.y=y

    def __str__(self):
        return f"( {self.x}, {self.y} )"

#----------------------------------------------------------------



point1=Coordinate(2, 5)
print(point1)

point2=Coordinate(10,9)
print(point2)
