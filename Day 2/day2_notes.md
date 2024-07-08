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

## Number manipulation and F strings in Python



