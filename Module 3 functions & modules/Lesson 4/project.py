valid = False

while not valid:
    try:
        # Step 2: Get input
        data = input("Enter bill amount, discount percentage, and number of people (comma separated): ")

        # Step 3: Split and convert
        bill_amount, discount_percent, people = data.split(",")
        bill_amount = float(bill_amount)
        discount_percent = float(discount_percent)
        people = int(people)

        # Step 4: Validate input
        if bill_amount <= 0:
            raise ValueError("Bill amount must be greater than 0.")
        if discount_percent < 0:
            raise ValueError("Discount percentage cannot be negative.")
        if people < 0:
            raise ValueError("Number of people cannot be negative.")

        # Step 5: Calculate discount
        discount = bill_amount * (discount_percent / 100)
        final_bill = bill_amount - discount

        # Step 6: Divide final bill
        amount_per_person = final_bill / people

    except ValueError as e:
        print("Value Error:", e)

    except ZeroDivisionError:
        print("Zero Division Error: Number of people cannot be 0.")

    else:
        print("\n----- Shopping Discount Summary -----")
        print(f"Original Bill: {bill_amount:.2f}")
        print(f"Discount: {discount:.2f}")
        print(f"Final Bill: {final_bill:.2f}")
        print(f"Each Person Pays: {amount_per_person:.2f}")
        valid = True

    finally:
        print("Attempt completed.\n")