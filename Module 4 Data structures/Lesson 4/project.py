snack_box1 = {"popcorn", "muffin", "strawberries", "popcorn", "granola"}
snack_box2 = {"muffin", "pretzels", "strawberries", "pretzels"}

print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)

snack_box1.add("banana")
print("Snack Box 1 after adding banana:", snack_box1)

shared_snacks = snack_box1.intersection(snack_box2)
print("Snacks in both boxes:", shared_snacks)

import array as arr
snack_counts = arr.array('i', [7, 4, 6, 2])

print("Snack counts array:", snack_counts)

snack_counts.insert(0, 3)
snack_counts.append(8)
print("Snack counts after adding items:", snack_counts)

count_of_6 = snack_counts.count(6)
print("Number of times 6 appears:", count_of_6)

snack_counts.reverse()
print("Reversed snack counts array:", snack_counts)

print("")
print("SNACK BOX SUMMARY")
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)
print("Shared snacks:", shared_snacks)
print("Final snack counts:", snack_counts)