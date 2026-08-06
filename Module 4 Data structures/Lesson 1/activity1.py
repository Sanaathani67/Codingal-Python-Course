numbers=[12, 24, 67, 69, 13, 676]
print(numbers)
print(type(numbers))
print(len(numbers))

print("1st item in list is",numbers[0])
print("last item in list is",numbers[-1])

print("from 2nd item to 4th item",numbers[1:4])#slice

list2=numbers *3
print(len(list2))