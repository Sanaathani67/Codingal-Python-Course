# 3 food categorie
#for each category show 4 flavours
#display the price for each flavour
#show ur order is on the way and show the bill
# if user enters invalid nos show invalid choice
print("select the type of ice cream  u want to order != ")
print("1.scoop")
print("2.cone")
print("3.sundae")

choice= input("enter either'1' or '2' or '3=")
if choice == '1':
    print("choose the flavour of scoop(1.chocolate,2.vanilla,3.splish splash,or 4.mint)=")
    scoop_flavour=input("enter 1,2 ,3 or 4 =")
    if scoop_flavour == "1":
        print("price is 100rs.ur order is on the wayrun once more to order more!")
    elif scoop_flavour == "2":
        print("price is 100rs.ur order is on the way!run once more to order more")
    elif scoop_flavour == "3":
        print("price is 100rs.ur order is on the way!run once more to order more")
    elif scoop_flavour == "4":
        print("price is 100rs.ur order is on the way!run once more to order more")
    else:
        print("invalid!")
elif choice =="2":
    print("choose the flavour of cone(1.cookie,2.coffee,3.cotton candy,or 4.mango)=")
    cone_flavour=input("enter 1,2 ,3 or 4 =")
    if cone_flavour == "1":
        print("price is 150rs for cookie.ur order is on the way!run once more to order more")
    elif cone_flavour == "2":
        print("price is 150rs for coffee.ur order is on the way!run once more to order more")
    elif cone_flavour == "3":
        print("price is 150rs for cotton candy.ur order is on the way!run once more to order more")
    elif cone_flavour == "4":
        print("price is 150rs for mango.ur order is on the way!run once more to order more")
    else:
        print("invalid")
elif choice =="3":
    print("choose the type of sundae(1.DBC,2.unicorn sprinkle,3.mango mania,or 4.bluberry splash)=")
    sundae_flavour=input("enter 1,2 ,3 or 4 =")
    if sundae_flavour == "1":
        print("price is 200rs for DBC.ur order is on the way!run once more to order more")
    elif sundae_flavour == "2":
        print("price is 200rs for unicorn sprinkle.ur order is on the way!run once more to order more")
    elif sundae_flavour == "3":
        print("price is 200rs for mango mania.ur order is on the way!run once more to order more")
    elif sundae_flavour == "4":
        print("price is 200rs for blueberry splash.ur order is on the way!run once more to order more")
    else:
        print("invalid")
   
else:
    print("invalid choice of numbers,choose again!")