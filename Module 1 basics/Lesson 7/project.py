character=input("enter a character : ")
ascii_value=ord(character)
print(ascii_value)
if ascii_value in range(97,123):
    print("lower case alphabet")
elif ascii_value in range(65,91):
    print("upper case alphabet")
elif ascii_value in range(48,58):
    print("Digit")
elif ascii_value in range(32):
    print("space")
else:
    print("special character")  