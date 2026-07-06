# M1 L7 A3

#Objective: Write a program to show students' grades by entering five subject marks 
subject_1=int(input("enter a number -"))
subject_2=int(input("enter a number -"))
subject_3=int(input("enter a number -"))
subject_4=int(input("enter a number -"))
subject_5=int(input("enter a number -"))

#  then calculating average marks and grades. 
avg=(subject_1+subject_2+subject_3+subject_4+subject_5)/5
print(avg)

# If the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2
if avg in range (91,101):
    print("a1")
elif avg in range(81,91):
    print("a2")    
elif avg in range(71,81):
    print("b1") 
elif avg in range(61,71):
    print("b2") 
elif avg in range(51,61):
    print("c1")
elif avg in range(41,51):
    print("c2")
else:
    print("F")                             