items=["pencil", "eraser", "protractor"]
#find the items starting with the letter 'p' and add them to another list
p_items=[]#starting letter == p add it to p_items
#p_items.append(something)

for element in items:
    if element[0]=="p":
        p_items.append(element)

print(p_items)    






p_items=[element for element in items if element [0]=="p"]
print(p_items)

r_items=[element for element in items if element [-1]=="r"]
print(r_items)

stock=[10, 7, 4]

#{"pencil": 10,"eraser": 7, "protractor": 4}
#DICTIONARY COMPREHENSION
inventory={element:count for element, count in zip(items, stock)}

print(inventory)
print(list(zip(items, stock)))

customer_request=input("enter the stationery item u want to buy: ")

if customer_request not in inventory or inventory[customer_request]==0:
    print("Out of stock . come again next week!")

    exit()

prices=[20, 5, 30]
#increase all prices by 10 rs

increased_prices=[p+10 for p in prices]
print(increased_prices)

markup_prices=list(map(lambda p:p+10, prices))
print(markup_prices)

markup_prices=list(map(lambda p:p*2, prices))
print(markup_prices)