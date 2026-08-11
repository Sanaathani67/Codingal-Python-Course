habit_info = ("Exercise", True, 7, 30)

weekly_habits = (1, 0, 1, 1, 0, 1, 0)

print("Number of days:", len(weekly_habits))

print("Monday:", weekly_habits[0])
print("Thursday:", weekly_habits[3])

print("First 3 days:", weekly_habits[0:3])
print("Days 6 and 7:", weekly_habits[5:7])

weekly_habits = weekly_habits + (1,)
print("Updated weekly habits:", weekly_habits)

completed = weekly_habits.count(1)
missed = weekly_habits.count(0)

print("Completed days:", completed)
print("Missed days:", missed)

completed_loop = 0
missed_loop = 0

for day in weekly_habits:
    if day == 1:
        completed_loop += 1
    else:
        missed_loop += 1

print("Completed days using loop:", completed_loop)
print("Missed days using loop:", missed_loop)

if completed_loop > missed_loop:
    print("Great job! You completed more days than you missed.")
elif completed_loop == missed_loop:
    print("Good effort! You completed and missed the same number of days.")
else:
    print("Keep going! Try to complete more days next week.")