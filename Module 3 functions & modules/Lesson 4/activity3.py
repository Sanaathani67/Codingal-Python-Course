while True:
    try:
        coin=int(input("insert a coin(only 1,2,5,10): "))
    except ValueError:
        print("enter a valid'NUMBER'")
        continue

    if coin!=1 and coin!=2 and coin!=5 and coin!=10:
        print("Invalid coin try again!\n")
        continue 