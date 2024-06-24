# Day 1

## Overview

Learn about:

- Printing
- Inputting
- Commenting
- Debugging
- String Manipulation
- Variables


## First exercise

Create a band name generator. It will ask:

- What's the name of the city your grew up in?
- What's your pet's name?


## Notes

### Print function (output)

Print function = print()
Inside parentheses is where you define what you want to print.

Classic `hello world`in Python = print("Hello, world!")

The double quotes around the words within the parentheses tells the computer that it isn't code. Aka a `string`, or string of characters. The double quotes tell the computer the beginning and ending of the string.

Error messages: If you forget a closing quote, for example, you get an error like this:

```
File "main.py", line 3
    print("Hello, world!)
                        ^
SyntaxError: EOL while scanning string literal
```

Stay attuned to the color of your code (syntax highlighting). With the missing quote, the code editor highlights everything, as opposed to when it is properly coded, which colors the code as expected.

### Exercise - print function

Take the following recipe and turn it into output, exact replica:

```
1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes.
```

My first attempt:

```
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
```

Test case passed.

Explanation: Simply need five print statements to output the five lines of the recipe.

### Print modifiers

Add print modifiers to achieve a specific need.

For example: print("She said: "Hello" and then left.")

When the computer sees the double quotes around `Hello`, it thinks the string has ended, and the word `Hello` is a command.

To solve this: print('She said: "Hello" and then left.')
Alternate the use of single and double quotes.
In Python, we can define a string (piece of text) using either a single quote or a double quote.
