import random

while True:
    player = input("enter rock, paper or scissors > ")

    if player != "rock" and player != "paper" and player != "scissors":
        print("invalid choice!")
        continue

    opponent = random.randint(1, 3)

    if opponent == 1:
        opponent = "rock"
    elif opponent == 2:
        opponent = "paper"
    else:
        opponent = "scissors"

    print(f"You chose {player}")
    print(f"The opponent chose {opponent}")

    if opponent == player:
        print("It's a tie!")
    elif player == "rock" and opponent == "scissors":
        print("You win! The bot lost.")
    elif player == "paper" and opponent == "rock":
        print("You win! The bot lost.")
    elif player == "scissors" and opponent == "paper":
        print("You win! The bot lost.")
    else:
        print("The bot won! You lost.")

    while True:
        again = input("Do you want to play again (y or n)? > ")

        if again == "y":
            break
        elif again == "n":
            print("thx for playing♥")
            exit()   # stops the whole program,did research coz code didnt stop!
        else:
            print("invalid choice! choose again (only 'y' or 'n')")