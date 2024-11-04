print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? Enter: S, M, or L ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Enter: Y or N ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Enter: Y or N ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0

if size == "s":
    if add_pepperoni == "y":
        if extra_cheese == "y":
            bill += 18
    elif add_pepperoni == "n":
        if extra_cheese == "y":
            bill += 16
    else:
        bill += 15
elif size == "m":
    if add_pepperoni == "y":
        if extra_cheese == "y":
            bill += 24
    elif add_pepperoni == "n":
        if extra_cheese == "y":
            bill += 21
    else:
        bill += 20
else:
    if add_pepperoni == "y":
        if extra_cheese == "y":
            bill += 29
    elif add_pepperoni == "n":
        if extra_cheese == "y":
            bill += 26
    else:
        bill += 25

print(f"Your final bill is: ${bill}.")
