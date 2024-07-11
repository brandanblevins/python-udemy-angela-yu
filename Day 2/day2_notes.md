# Day 2

## Overview

Learn about:

- Data types
- Numbers
- Operations
- Type Conversion
- f-Strings

The final project is going to be building a tip calculator.

## Primitive data types

The code `print(len(12352))` crashes. It's the wrong data type. It's an integer, not a string.

Data types include:

- String: Just a string of characters. `"hello"`. As long as characters are wrapped in double quotes, even if it's numbers, the system treats it as a string.
- Integer: To declare an integer data type, just write the numbers without anything else. `123`
- Float: Short for a floating point number. Basically an integer with decimal place. `3.14159`
- Boolean: Only two possible values: `True` and `False`. No quotation marks around them.

The code `print("Hello"[0])` returns an `H` because it's the first character in the string. The code `print("Hello"[4])` returns the `o`.

The code `print (123 + 345)` adds the numbers, whereas `print("123" + "345")` concatenates the strings to give you `123345`.

Quiz: What does the following code print?

```
street_name = "Abbey Road"
print(street_name[4] + street_name[7])
```

I got the correct answer, which is `yo`.

## Type error, type checking, and type conversion

You can only concatenate strings, not integers.

Use the function `type()` to figure out the data type of something (type checking). For example, the code `print(type(123))` returns `<class 'int'>`.

Type conversion: convert the data type of something. For example, to convert the `123` integer into a string, enter `str(123)`.
This code `print(type(str(123)))` returns `<class 'str'>` because the data type was converted to a string.

As another example of type conversion, the code `print(str(70) + str(100))` returns `70100` because strings are concatenated, not added.

## Coding exercise (data types)

Instructions:

```
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.

The last line of your program should print the result.
```

My first attempt:

```
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

print(two_digit_number[0] + two_digit_number[1])
```

Result: Wrong on all test cases. I should have used the print() function and type() function to figure out the data type of `two_digit_number`.

My second attempt:

```
print(int(two_digit_number[0]) + int(two_digit_number[1]))
```

Result: Correct on all test cases.

Angela coded it in a different way. Readability is key here, not optimizing for the least number of lines.

```
two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit + second_digit

print(two_digit_number)
```

## Mathematical operations in Python

Add: 3 + 5
Subtract: 7 - 4
Multiply: 3 * 2
Divide: print(6 / 3)
When dividing things, you almost always end up with a floating point number. Use the type(function) to see that it is a float, not an integer.

Exponent (raise a number to a power): 2 ** 2 

When you have more than one operation on the same line of code, there is an order of operation.
PEMDAS = 1) Parentheses, 2)Exponents, 3) Multiplication, Division (equally important) 4) Addition, Subtraction (equally important)
Things also happen in order from left to right.

print(3 * 3 + 3 / 3 - 3)
This gives you `7` (technically `7.0`).

Question: how can you change this line of code so that the result would be `3`?

My answer: print(3 * (3 + 3 / 3 - 3))

Angela's answer: print(3 * (3 + 3) / 3 - 3)

## Coding exercise (BMI calculator)

Instructions:

```
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

BMI Wikipedia Page

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.

Example Input 1
1.75
80
means: weight = 80 and height = 1.75

Example Output 1
26
Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837
```

Starting code:
```
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
```

My first attempt:
```
BMI = print(weight / height * (height ** height))
```

Result: a TypeError; `TypeError: unsupported operand type(s) for /: 'str' and 'str'`.

My second attempt:
```
print(weight / height ** height)
```

Result: another TypeError; `TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'`.

My third attempt:
```
convertHeight = height ** height

bmi = (float(weight) / float(convertHeight))

print(bmi)
```

Result: the same TypeError.

This StackOverflow answer seems to get at what I'm doing wrong: https://stackoverflow.com/questions/44411502/unsupported-operand-types-for-or-pow-str-and-int-with-python3
I need to convert the input to an acceptable type to apply mathematical operators.

My fourth attempt:
```
convertHeight = float(height)

convertWeight = float(weight)

print(convertWeight / (convertHeight ** convertHeight))
```

Test result: the inputs `1.65` and `72` gave an answer of `31.512581978186624`. That's the BMI.

Actual result: my code failed all test cases.

My fifth attempt (troubleshooting):
```
convertHeight = float(height)

print(convertHeight)

convertWeight = float(weight)

print(convertWeight)
```

Result: this code does print the expected inputs of `1.65` and `72.0`. So my problem is now with the mathematical operators.

My sixth attempt:
```
convertHeight = float(height)

convertWeight = float(weight)

exponentHeight = convertHeight ** convertHeight

print(convertWeight / exponentHeight)
```

Result: the same as before; the inputs `1.65` and `72` gave an answer of `31.512581978186624`. This isn't going to work for the test cases.
I think the problem is that I was trying to find an exponent? Looking at the task more closely, that's not what was needed for the height.

My seventh attempt:
```
convertHeight = float(height)

convertWeight = float(weight)

print(convertWeight / (convertHeight * convertHeight))
```

Test result: this gives an answer of `26.44628099173554`.

Actual result: all test cases failed again. It looks like converting to a float is the problem?

My eighth attempt:
```
convertHeight = int(height)

convertWeight = int(weight)

print(convertWeight / (convertHeight * convertHeight))
```

Result: `ValueError: invalid literal for int() with base 10: '1.65'`.

Literally nothing works. The output of the test cases is an integer, but the test will not accept integers.

My ninth attempt:
```
convertWeight = float(weight)

convertHeight = float(height)

bmi = convertWeight / (convertHeight * convertHeight)

convertBmi = int(bmi)

print(convertBmi)
```

Test result: this gave an output of `26`. Feels wrong, but it seems to work.

Actual result: all three test cases passed. It was just a matter of converting the BMI to an integer.

Angela's explanation:
```
height = input()
weight = input()
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)
```

I still don't understand the need to convert to an integer at the end. But my logic is in line with Angela's explanation.
The way I was using the exponent operator was wrong.

## Number manipulation and F strings in Python

**Number manipulation**

Use the round() function to round numbers.

The code `print(round(8 / 3))` turns into `3`.

You can also specify the number of digits to round it to. 

The code `print(round(8 / 3, 2))` turns into `2.67`. The `, 2` tells the system to round to two digits.

Use `//` to do division based on rounding. This turns the number into an integer, whereas the single division sign delivers a floating point number.

The code `print(round(8 // 3)` turns into `2` without having to conver it into an integer.

If you save a calculation as a variable, you can continue to perform operations.

```
result = 4 / 2
result /= 2
print(result)
```
Delivers `1.0` as the result.

Another example:

```
score = 0
score += 1
print(score)
```
Delivers `1` as the result.

This is useful when you have to manipulate a value based on a previous value.

**F strings**

Instead of taking a bunch of different data types and combining them with plus signs, you can use an f-string.

Add an f in front of the string.

Example:
```
score = 0
height = 1.8
isWinning = True

f"Your score is {score}"
```
Delivers `Your score is 0`. you can add the other variables inside the same string without having to do the " " + " " stuff.

## Coding exercise (life in weeks; f-strings and mathematical operations)

Instructions:
```
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
56
Example Output
You have 1768 weeks left.
```

Starting code:
```
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
```

My first attempt:
```
age_integer = int(age)

age_in_weeks = age_integer * 52

total_weeks = 90 * 52

weeks_left = total_weeks - age_in_weeks

print(f"You have {weeks_left} weeks left.")
```

Result: Delivers the output `You have 3900 weeks left` for the input `15`. My code passes all three test cases.

Angela got there in a more efficient way:
```
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")
```

## Day 2 project: Tip calculator

We are going to code a tip calculator that asks for the amount of the bill, the number of people contributing, and the percentage tip.
This should be rounded to 2 decimal places.

Instructions:
```
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
```

My first attempt:

```
bill_amount = input("How much was the bill?")

convert_bill = round(bill_amount, 2)

number_of_people = input("How many people are paying?)

convert_people = int(number_of_people)

tip_percentage = input("What percentage tip would you like to leave? 10, 12, or 15")

convert_tip = int(tip_percentage)

calculate_individual_contribution = ((convert_bill / convert_people) * 1.12)

money_per_person = round(calculate_individual_contribution, 2)

print(f"You should each contribute {money_per_person} to the bill. This includes the tip.")
```

Result: error; I forgot to add the closing quote to one of the input functions:
```
  File "main.py", line 14
    number_of_people = input("How many people are paying?)
                                                         ^
SyntaxError: EOL while scanning string literal
```

Result after correcting error: another error, but this time after entering an answer for the first input:
```
How much was the bill?200
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    convert_bill = round(bill_amount, 2)
TypeError: type str doesn't define __round__ method
```

I'm going to try to wrap the first input function in float()

Result after change: the code ran through each of the inputs and deliver an answer for the output
```
How much was the bill? 150
How many people are paying? 5
What percentage tip would you like to leave? 10, 12, or 15 12
You should each contribute 33.6 to the bill. This includes the tip.
```

My final code after some cleanup:
```
bill_amount = float(input("How much was the bill? "))

convert_bill = round(bill_amount, 2)

number_of_people = input("How many people are paying? ")

convert_people = int(number_of_people)

tip_percentage = input("What percentage tip would you like to leave? 10, 12, or 15 ")

convert_tip = int(tip_percentage)

calculate_individual_contribution = ((convert_bill / convert_people) * 1.12)

money_per_person = round(calculate_individual_contribution, 2)

print(f"You should each contribute {money_per_person} to the bill. This includes the tip.")
```

Angela code:
```
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: {final_amount} dollars")
```
Output:
```
Welcome to the tip calculator!
What was the total bill? $153.45
How much tip would you like to give? 10, 12, or 15?15
How many people to split the bill?5
Each person should pay: 35.29 dollars
```

The reason why the amount for the original calculation is 33.6 and not 33.60 is a formatting issues, not a rounding problem.

Use this code `final_amount = "{:.2f}".format(bill_per_person)` to address the formatting issue.

So I did a few things wrong in my code:

1. My code was inefficient. She converted data types by wrapping functions around the input function.
2. I hard coded the tip percentage as 12% per the instructions, but she actually accounted for the different tip amounts in the calculation.
3. I shouldn't mention the tip as a percentage because the program isn't going to run properly if the users enter the `%` symbol.


Angela final solution:
```
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")
```

