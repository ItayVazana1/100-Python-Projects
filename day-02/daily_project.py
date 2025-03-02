# Tip calculator

print("Welcome to my tip calculator!")
total_bill = float(input("First , what was the bill?\n$"))
tip_percentage = int(input("And how much tip would you like to give?\ninsert number( 0% / 10% / 12% / 15% ):"))
total_bill = total_bill + (total_bill*0.01*tip_percentage)
count_of_people = int(input("How many people to slip the bill?"))
print(f"Got it! so each person should pay : ${round(total_bill/count_of_people,2)}")
print(f"If you don't have any penny's , so each person should pay : ${round(total_bill/count_of_people)}")
