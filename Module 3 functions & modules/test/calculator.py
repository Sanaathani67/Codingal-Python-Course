def add (a,b):
    return a+b

def subtract (a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide (a,b):
    return a/b

while True:
    
    print("+.addition")
    print("-.subtraction")
    print("*.multiplication")
    print("/.division")
    print(".=exit")
    
    choice=input("enter either +,-,*,/,. = ")
    if choice==".":
        print("thx for using the calculator")
        break

    try:
        num1=float(input("enter a number: "))
        num2=float(input("enter a number: "))
    except ValueError:
        print("invalid number")
        continue

    if choice=="+":
        ans=add(num1,num2)
        print("answer=",ans)

    elif  choice=="-":
        ans=subtract(num1,num2)
        print("Answer=",ans)

    elif  choice=="*":
        ans=multiply(num1,num2)
        print("Answer=",ans)       

    elif  choice=="/":
        try:
            ans=divide(num1,num2)
            print("Answer=",ans) 
        except ZeroDivisionError:
            print("DO NOT ENTER '0'FOR THE 2ND NUMBER!")
            continue
    else:
        print("invalid choice ,only +,-,*,/")      

    print("\n ")
    