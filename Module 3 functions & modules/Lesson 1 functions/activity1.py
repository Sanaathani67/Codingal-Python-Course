# def greet(name):
#     print("goodmorning,",name)

# greet("sanaathani")
# greet("shirin")

def greet_customer():
    print("welcome to the lemonade stand!")
    print("fresh lemonade available here!")

greet_customer()

price_per_cup =int(input("enter the price per cup : "))
cups_sold =int(input("how many cups do u want? : "))

def calculate_total(p,c):
    total=p*c
    return total

my_total_bill= calculate_total(price_per_cup,cups_sold)
print("total cost: ",my_total_bill)

def thank_you_message(cups):

    if cups >= 5:

        return "Wow, big order! Thanks so much for your support!"

    else:

        return "Thanks for stopping by the stand!"

# PART 11: Call thank_you_message and store the value it returns

closing_message = thank_you_message(cups_sold)
print(closing_message)