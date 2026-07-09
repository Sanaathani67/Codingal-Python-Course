#M2 L2 A1 - Write a program to calculate the sum of the first N natural numbers.
sum=0
n=int(input("enter a number uptonwhich u want to find the sum"))
for i in range(1,n+1):
    sum=i+sum
    print(sum)