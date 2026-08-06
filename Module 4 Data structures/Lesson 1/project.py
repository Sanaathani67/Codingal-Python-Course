marks = [78, 85, 92, 67, 88, 74]

print("marks list:", marks)
print("Type:", type(marks))

print("number of marks:", len(marks))

print("first mark:", marks[0])
print("last mark:", marks[-1])

print("first three marks:", marks[0:3])
print("reversed marks list:", marks[::-1])

print("checking first and last digit of each mark:")
for mark in marks:
    mark_str = str(mark)
    print("mark:", mark, "first digit:", mark_str[0], "last digit:", mark_str[-1])

total = 0
for mark in marks:
    total += mark

average = total / len(marks)

sorted_marks = sorted(marks)
smallest = sorted_marks[0]
largest = sorted_marks[-1]

print("Summary")
print("Total Marks:", total)
print("Average Marks:", average)
print("Smallest Mark:", smallest)
print("Largest Mark:", largest)




fruits = ["apple", "banana", "apple", "guava", "apple", "pineapple"]

search = input("Search for a fruit(only apple banana guava pineapple): ")

count = 0

for fruit in fruits:
    if fruit == search:
        count = count + 1

print(search, "comes", count, "times in the list.")
