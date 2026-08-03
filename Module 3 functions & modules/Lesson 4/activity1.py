try:
    n=int(input("enter a number: "))
    print("the user entered",n)
except ValueError as error:
    print("i asked u to enter a NUMBER ,not garbage!")  
    print(error)  