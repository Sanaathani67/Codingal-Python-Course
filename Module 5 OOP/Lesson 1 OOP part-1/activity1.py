#class definition
#usually class names start with a capital letter
class Dog:
    species="Canic lupus familiaris"

#this is called a constructor function
#this function is called everytime u create an object
    def __init__(self, name, breed ):
        self.name=name
        self.breed=breed
#__________________________________________________

#create an object from Dog class
#not a function call, we r creating an object
my_dog=Dog("Togo","German Shepard")
# print(my_dog)
# print(type(my_dog))

#my_dog=oject,species=property
print(my_dog.species)
print(my_dog.name)

ur_dog=Dog("Tommy","pug")
print(ur_dog.species)
print(ur_dog.name)

print(f"My dog's name is {my_dog.name} & he is a {my_dog.breed}")
print(f"Ur dog's name is {ur_dog.name} & he is a {ur_dog.breed}")