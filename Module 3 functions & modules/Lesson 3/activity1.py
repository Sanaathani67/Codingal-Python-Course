def calculate_change (paid,price):
    change=paid-price
    return change


snack_price=25

print("welcome to snack vending machine")
print(f"the snack costs rs.{snack_price}")
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


    if total_money_inserted>=snack_price:
        print("you have fully paid the amount!")
        break

change_due=calculate_change(total_money_inserted,snack_price)

if change_due==0:
    pass
else:
    print(f"here's ur change: rs.{change_due}")
