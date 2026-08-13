my_set={1, 2, 3, 3, 4, 5, 5, 5}
print(my_set)



groceries={"apple" ,"apple", "banana", "banana"}
print(groceries)

print(type(groceries))

groceries.add("apple")

print(groceries)

groceries.add("orange")

print(groceries)

votes={"Sanaathani", "Maryam", "Maryam", "Maryam", "Maryam", "Sanaathani"}
print(votes)

ur_fav_colours={"black", "purple", "blue"}
frnd_fav_colours={"black", "pink", "white"}

common_colours=ur_fav_colours.intersection(frnd_fav_colours)
print(common_colours)

all_colours=ur_fav_colours.union(frnd_fav_colours)
print(all_colours)

import array as arr

fruit_counts=arr.array("w", "ate")
print("count of fruits stored as an array: ", fruit_counts)

fruit_counts=arr.array("i",[3, 4, 9, 2] )
print("count of fruits stored as an array: ", fruit_counts)

fruit_counts.append(67)
print(fruit_counts)

fruit_counts.insert(0,67)
print(fruit_counts)

count_of_67=fruit_counts.count(67)
print(count_of_67)

fruit_counts.reverse()
print(fruit_counts)