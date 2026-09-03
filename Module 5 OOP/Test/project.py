# QUIZ CLASS

# Write a program to create a quiz related to multiple fruits using object-oriented programming in Python.
#  Create a class that consists of -1. 
# a constructor with a dictionary of fruits and respective colours2. 
# a function to execute the quiz. Here, the fruit will be chosen at random from the dictionary. 
# Then ask the user to enter the colour of that fruit. 
# Evaluate the answer and display the result accordingly

import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {
            "Apple": "Red",
            "Banana": "Yellow",
            "Orange": "Orange",
            "Grapes": "Green",
            "Mango": "Yellow",
            "Watermelon": "Green",
            "Strawberry": "Red"
        }

    def execute_quiz(self):
        fruit = random.choice(list(self.fruits.keys()))
        answer = input(f"What is the colour of {fruit}? ")

        if answer.strip().lower() == self.fruits[fruit].lower():
            print("Correct! Well done.")
        else:
            print(f"Wrong! The correct colour is {self.fruits[fruit]}.")

quiz = FruitQuiz()
quiz.execute_quiz()