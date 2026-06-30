# M1 L4 A3

# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
math=int(input("enter a score-"))
english=int(input("enter a score-"))
science=int(input("enter a score-"))
hindi=int(input("enter a score-"))

# Store each mark in its own variable.

# 2) Add all 4 subject marks and store the total in `sum`.
sum=math+english+science+hindi
# 3) Print the total marks stored in `sum`.
print(sum)
# 4) Calculate the percentage:
perc=(sum/320)*100
print(perc)
# - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)

# - Multiply the result by 100

# Store the final value in `perc`.

# 5) Print the percentage stored in `perc`.