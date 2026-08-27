class Laptop:
    def __init__(self):
        self.__price=40000

    def sell(self):
        print(f"THis laptop can be sold at rs.{self.__price}")

    #setter method-to update private attribute's value
    def setPrice(self, amount):
        self.__price+= amount
#____________________________________________________________________

dell=Laptop()
dell.sell()

#i want to increase/decrease of laptop
#we cannot directly change the value of a private property
#dell.__price+=10000 #NOT POSSIBLE


dell.setPrice(10000)
dell.sell()