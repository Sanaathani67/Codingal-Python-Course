print("Welcome to the ATM cash dispenser!")
print("Dispensing cash one customer at a time")
notes=[500, 200, 100, 50, 20, 10, 5, 2, 1]

customers_served=0

total_cash_dispensed=0

dispensing=True

while dispensing:

    name=input("enter customer's name: ")
    amount=int(input(f"Hello {name} enter withdrawal amount"))

    remaining=amount
    i=0

    #inner while loop
    while i<len(notes):
        count=remaining// notes[i]
        if count>0:
            print(f"{count}x₹{notes[i]} notes = {count*notes[i]}")

            remaining=remaining-(count*notes[i])

        i+=1

    customers_served+=1
    total_cash_dispensed+=amount

    again=input("Next customer?yes or no :")
    if again=="no":
        dispensing=False

print(f"\nCustomers served : {customers_served}")

print(f"Total dispensed : {total_cash_dispensed} units")

print("ATM session closed. Goodbye!")



