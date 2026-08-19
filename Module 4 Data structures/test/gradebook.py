students={
    "Sanaathani":99,
    "Maryam":97,
    "Shirin": 98,
    "Samara":97,
    "rahul":46
}
total=0
for name, score in students.items():
    total=total+score

average=total/len(students)
print("The average score is: ",average)

highest=max(students.values())
lowest=min(students.values())
print("the highest score is: ",highest)
print("the lowest score is: ",lowest)

top_student = max(students, key=students.get)
low_student= min(students, key=students.get)

print(low_student)
print(top_student)

search=input("Enter a student name: ")
print(f"the score of{search}",students.get(search,"INVALID INPUT!"))