# M1 L6 A12

# 1) Store values in `a`, `b`, and `c`.
a=67
b=69
c=0
# 2) Check an AND condition using `a and b and c`:
if a and b and c:
    print("all are true")
# - This becomes True only if all three values are treated as True.

# - If the condition is True, print the “all true” message.

# - Otherwise, print the “at least one false” message.

# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.

# 4) Check an OR condition: `a > 0 or b > 0`
if a>0 or b>0:
    print("either of them is +ve")
# - If at least one of them is greater than 0, print the “either is greater than 0” message.
else :
    print("none are +ve")
# - Otherwise, print the “no number is greater than 0” message.

# 5) Check another OR condition: `b > 0 or c > 0`

# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.
if not (a==b):
    print("a is not equal to b")