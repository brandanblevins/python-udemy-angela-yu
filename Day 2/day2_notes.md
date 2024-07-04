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

