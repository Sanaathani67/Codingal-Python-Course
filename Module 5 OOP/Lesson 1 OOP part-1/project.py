class Footballer:
    sport="FOOTBALL"

    def __init__(self, name, good, club, country ):
        self.name=name
        self.good=good
        self.club=club
        self.country=country
#__________________________________________________

#create an object from Dog class
#not a function call, we r creating an object
p1=Footballer("Cristiano Ronldo", "rlly good", "Al-Nassr FC", "Portugal")
# print(player)
# print(type(player))

#my_dog=oject,species=property

p2=Footballer("Belingham", " is good", "EFL Championship", "England")
print(p2.name)
print(p2.good)

p1=Footballer("Cristiano Ronldo", " is rlly good", "Al-Nassr FC", "Portugal")
print(p1.name)
print(p1.good)
print(f"Player 1's name is {p1.name} & he is a {p1.good} player!")
print(f"Player 2's name is {p2.name} & he is a {p2.good} player!")