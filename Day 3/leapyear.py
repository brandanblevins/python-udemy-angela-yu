# Which year do you want to check?
year = int(input("What year do you want to try? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

leap = year % 4
not_leap = year % 100
leap_exception = year % 400

if leap != 0:
  print("Not leap year")
elif not_leap != 0:
  print("Leap year")
elif leap_exception == 0:
  print("Leap year")
else:
  print("Not leap year")
