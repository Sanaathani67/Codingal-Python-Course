tuplex = ("hello", 42, 3.14, True)
print("Step 1 - Mixed Data Types:", tuplex)

tuplex = (10, 20, 50, 40, 50, 60)
print("Step 2 - Six Integers:", tuplex)

tuplex = tuplex + (9,)
print("Step 3 - Added 9:", tuplex)

tuple1 = (10, 50, 20, 50, 30, 50, 40)
count_50 = tuple1.count(50)
print("Step 4 - Count of 50 in tuple1:", count_50)

tuplex = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Step 5 - Long Tuple for Slicing:", tuplex)

slice1 = tuplex[3:5]
print("Step 6 - Slice tuplex[3:5]:", slice1)

slice2 = tuplex[:6]
print("Step 7 - Slice tuplex[:6]:", slice2)