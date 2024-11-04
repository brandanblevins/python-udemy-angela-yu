print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? Enter: S, M, or L ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Enter: Y or N ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Enter: Y or N ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0

if size == "s":
    if extra_cheese == "y":
        if add_pepperoni == "y":
            bill += 18
    elif extra_cheese == "n":
        if add_pepperoni == "y":
            bill += 17
    else:
        bill += 15
elif size == "m":
    if extra_cheese == "y":
        if add_pepperoni == "y":
            bill += 24
    elif extra_cheese == "n":
        if add_pepperoni == "y":
            bill += 23
    else:
        bill += 20
else:
    if extra_cheese == "y":
        if add_pepperoni == "y":
            bill += 29
    elif extra_cheese == "n":
        if add_pepperoni == "y":
            bill += 28
    else:
        bill += 25

print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${bill}.")
