n=int(input("enter a numerator : "))
d=int(input("enter a denominator : "))
if n%d==0:
    print(f"{n} is divisible by {d}")
else:
    print(f"{n} is not divisible by {d}")