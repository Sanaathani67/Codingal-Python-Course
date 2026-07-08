# M2 L1 A3

# ACTIVITY 3 - CUSTOMIZE YOUR FOOD DELIVERY ORDER

# 1) Display a menu asking the user to select a food category:

# - 1 for Biryani

# - 2 for Pizza
print("select the type of food u want to order ")
print("1.Pizza")
print("2.Biriyani")
# 2) Take the user’s input and store it in `choice`.
choice= input("enter either'1' or '2'")
print(type(choice))

# 3) If `choice` is 1 (Biryani):
if choice == "1":
    print("type of pizza? (1 -veg,2 -chicken)")
    pizza_type =input("enter 1 or 2 ")
    if pizza_type=="1":
        print(" ur veg pizza is on the way!")
    else:
        print("ur chicken pizza is on the way!")    


else:
    print("not pizza")
# a) Show Biryani options (Veg / Chicken)

# b) Take the user’s input for Biryani type and store it in `choice2`

# c) If `choice2` is 1, print "Your order is on the way: Veg Biryani"

# Else, print "Your order is on the way: Chicken Biryani"

# 4) Else if `choice` is 2 (Pizza):

# a) Show pizza options (Paneer / Chicken)

# b) Take the user’s input for pizza type and store it in `choice3`

# c) If `choice3` is 1, print "Your order is on the way: Paneer Pizza"

# Else, print "Your order is on the way: Chicken Pizza"

# 5) Else (if `choice` is not 1 or 2):

# Print "Wrong choice!"