sum=0
goals=[1, 2, 0, 5, 3, 12]
print("original list : ",goals)

for item in goals :
    sum=sum+item
print(sum)    
avg=sum/len(goals)
print(avg)

#find the min amd max goals scored in a single game
goals.sort()

print(goals)
print("the minimum goals scored in a game is",goals[0])
print("the maximum goals scored in a game is",goals[-1])