print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? Enter: S, M, or L ").lower() # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Enter: Y or N ").lower() # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Enter: Y or N ").lower() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill += 0

if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print(f"Your final bill is: ${bill}.")
