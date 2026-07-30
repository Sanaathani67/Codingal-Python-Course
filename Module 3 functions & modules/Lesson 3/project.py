def calculate_change (paid,price):
    change=paid-price
    return change


ticket_price=25

print("welcome to the parking ticket payment helper!")
print(f"the ticket costs rs.{ticket_price}")
print("accepted coins: 1,2,5,10\n")

total_money_inserted=0
number_of_coins_inserted=0

#infinite loop,it will only stop if we "break"
while True:
    coin=int(input("insert a coin(only 1,2,5,10): "))

    if coin!=1 and coin!=2 and coin!=5 and coin!=10:
        print("Invalid coin try again!\n")
        continue 

    total_money_inserted=total_money_inserted+coin
    number_of_coins_inserted=number_of_coins_inserted+1

    print(f"Inserted {coin}.Total collected so far={total_money_inserted}")


    if total_money_inserted>=ticket_price:
        print("you have fully paid the amount!")
        break

    print("\n===== PAYMENT SUMMARY =====")
print("Ticket Price:", ticket_price)
print("Coins Inserted:", number_of_coins_inserted)
print("Total Paid:", total_money_inserted)
print("Change Given:", calculate_change )
print("===========================")
print("Parking ticket payment complete!")


change_due=calculate_change(total_money_inserted,ticket_price)

if change_due==0:
    pass
else:
    print(f"here's ur change: rs.{change_due}")

