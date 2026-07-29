price_before_discount=float(input("enter the price of item before discount : "))
discount_perc=float(input("enter the discount percentage : "))
def calculate_total_bill(price,discount):
    total=price -(discount/100)*price
   
    return total


total_bill=calculate_total_bill(price_before_discount,discount_perc)
print(total_bill)