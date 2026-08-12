prefs={
    "Sanaathani": "Pizza",
    "Dhruvanth": "Fried chicken",
    "Maryam": "PIzza",
    "Ronaldo": "Biriyani"
}

prefs["Abhishek"]="sea food"

#print(prefs)

prefs["Ronaldo"]="Pizza"

#print(prefs)

for name, food in prefs.items():
    print(f"{name} likes to eat {food}")
#print(prefs.items())


print("no.of keys in dict=", len(prefs))


prefs.pop("Dhruvanth")

print(prefs)
