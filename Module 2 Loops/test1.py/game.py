secret =27
i=1
while i<=5:
    guess=int(input("guess the secret number : "))
    if guess==secret:
        print("congratulations! u guessed the secret number!")
        break 
    distance = abs(secret - guess)
    if distance <=3:
        print("ur guess is  🔥hot!")
    elif distance <=7:
        print("ur guess is  🌡️warm")
    elif distance <=12:
        print("ur guess is 🥶cold!")
    else:
        print("ur guess is 🧊ice cold!")

    for life in range (5-i):
        print("❤️")
    i=i+1

if i == 6:
    print("uh oh u ran out of tries (the secret number was 27!)")
