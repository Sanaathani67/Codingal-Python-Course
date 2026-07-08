# M2 L1 A1

# ACTIVITY 1: STUDENT CAN TAKE EXAM UNDER TWO CONDITIONS:

# Take the required input for attendance
attendance=float(input("enter an attendance percentage ="))
# - Student should have attendance >= 75%

# - Check if attendance matches above criteria
if attendance>=75:
    print("Allowed!")
else:
    mc=input("do you have a medical certificate?(plz enter 'y'or'n')")
    if mc=="y":
        print("Allowed!")
    else:
        print("Not Allowed")   
# - Then Print "Allowed"

# - If attendance is low, Student should have a medical certificate

# - Take input for medical certificate

# - Check if student replied Yes or No

# - If Yes, Print "Allowed"

# - Else No, Print "Not Allowed"