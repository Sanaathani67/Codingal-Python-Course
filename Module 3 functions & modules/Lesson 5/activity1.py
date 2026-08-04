import random

secret_number=random.randint(1,100)

print("Guess the number ,its between 1 and 100!")

while True:
    guess=int(input("enter ur guess here:> "))

    if guess == secret_number:
        print("U WON THE GAME!!")
        break
    else:
        print("you guessed WRONG!!")