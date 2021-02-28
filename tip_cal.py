print("Welcome to the tip calculator")

total_bill = input("What was the total bill?  ")
tip = input("what percentage tip would you like to give? 10, 12, or 15?  ")
no_of_people = input("How Many people to split: ")
tip_int = int(tip)
total_bill_int = int(total_bill)
no_of_people_int = int(no_of_people)
total_bill_tip_cal = total_bill_int + total_bill_int*tip_int/100
amt_paid_per_person = round(total_bill_tip_cal / no_of_people_int, 2)
print(f"Each Person should pay: {amt_paid_per_person}")

