fruits = ["apple", "banana", "apple", "guava", "apple", "pineapple"]

search = input("Search for a fruit: ")

count = 0

for fruit in fruits:
    if fruit == search:
        count = count + 1

print(search, "comes", count, "times in the list.")

