question = int(input("How many points did you score? "))

question2 = int(input("How many minutes did you play? "))

math = question % question2

if math == 0:
    print("This is even!")
else:
    print("This is odd!")