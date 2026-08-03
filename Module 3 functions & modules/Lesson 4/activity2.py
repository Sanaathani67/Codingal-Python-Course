try:
    num1=int(input("enter a number : "))
    num2=int(input("enter a number : "))
    result = num1 / num2
    print("division result: ",result)

except ValueError:
    print("please enter 2 NUMBERS!")

except ZeroDivisionError:
    print("please do not enter '0' for the 2nd number")

else:
    print('no exceptions found!')

finally:
    print("this block always runs no matter what!")