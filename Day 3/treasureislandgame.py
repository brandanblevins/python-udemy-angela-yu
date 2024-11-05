print("Welcome to Treasure Island! Your mission is to find the treasure.")

left_or_right = str(input("Do you want to take the left path or the right path? Type left or right: "))

if left_or_right == "left":
    swim_or_wait = str(input("Good choice! Now, do you want to swim across the lake or wait here? Type swim or wait:"))
else:
    print("You fell into a hole! GAME OVER!")

