def greet_customer():
    print("Welcome to the Art Supplies Store!")
    print("Find everything you need for your next masterpiece!")

greet_customer()

price_per_item = float(input("Enter the price per art item: "))
items_bought = int(input("How many art items do you want? "))

def calculate_total(price, items):
    total = price * items
    return total

my_total_bill = calculate_total(price_per_item, items_bought)
print("Total Cost:", round(my_total_bill, 2))

amount_paid = float(input("Enter the amount paid:"))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, my_total_bill)

def thank_you_message(items):
    if items >= 5:
        return "Wow, thanks for stocking up on art supplies!"
    else:
        return "Thanks for shopping with us!"

closing_message = thank_you_message(items_bought)

print("\n----- Art Supplies Receipt -----")
print("Price per item: ", round(price_per_item, ))
print("Items purchased:", items_bought)
print("Total cost: ", round(my_total_bill, ))
print("Amount paid: ", round(amount_paid, ))
print("Change due: ", round(change_due, ))

