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
You can also reverse the single and double quotes in this example and get the same thing. The point is the alternation of the type of quotes.

Another option is backslashes: print("She said: \"Hello\" and then left.")
The backslashes tell the computer to ignore the double quotes and keep them as text. It's meant to be printed exactly as it is.

Examples that all work:

```
print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")
```

My example to add:

```
print('I want to quote someone like this "I\'m quoting them", and that is that.')
```

Had to use the backslash to deal with the apostrophe for `I'm`.


### String manipulation and code intelligence

Example hello world: print("Hello, world!\nHello, world!")

The use of `\n` separates the lines within the same string. You don't want gaps between the `\n`, unless you are trying to add space.


String concatenation: print("Hello" + "Angela")
Use a `+` to combine strings.

String concatenation is taking those separate strings of characters and merging them into one.

**In Python programming, spaces are very important. For example, putting a tab in front of a print function produces an indentation error.**

Code intelligence is a feature within Replit. I already had it turned on. It helps you understand what is going wrong with your code (for example, red squiggly line).


### Debugging practice (string manipulation)

Debug the following code to make it print like the output example:

```
# Fix the code below 👇

print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
```

My attempt:

```
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
```

The tricky part was making the `"+"` part appear in the output. It also needed an opening quote in the first line, a deletion of the tab/indentation in the third line, and a deletion of one of the opening curls in the fourth line.


### Input function

Instead of using something like: print("What is your name?")
to collect a user's name.

We'll use the input function:

```
input("What is your name?")
```

When you use this function, the cursor stays active at the end of the line in the output. The program pauses to give the user the opportunity to enter their name. As opposed to print(), which just ends the execution.

You can start to use the entries to the input function, like:

```
print("Hello " + input("What is your name?"))
```

This prompts the entry of the name in the console, and then outputs `Hello [name]` after the user enters the name.

**To comment in Python code, add the `#` in front of the text.**

### Coding exercise (input function)

For Auditorium, the input function works a bit differently. You enter input() in the code, and then put the actual input in the `Input` section. For example:

```
num1 = int(input())
num2 = int(input())

print(num1 * num2)
```

Another example to work through:

```
num1 = int(input())
num2 = int(input())

print(6)

Explanation:

Without changing the code, try clicking submit.

If a student didn't complete the coding exercise, then the extra tests should catch this.

For example in this case 6 is the correct answer for the visible inputs. But behind the scenes when you submit the code we are also passing in 5 and 5.

5 x 5 = 25

while

2 x 3 = 6

So the only way for the student to pass all the tests in the evaluation is to write the correct code.

This is how we ensure you're doing the right things and test your understanding of the programming concepts. It's like having a teacher next to you checking your code.
```

To fix the above, specify exactly what you want to print with the use of `num1` and `num2`:

```
num1 = int(input())
num2 = int(input())

print(num1 * num2)
```

The following are my tests with my inputs and the Auditorium outputs:

```
print("Howdy " + input() + "!")

print("What is " + input() + "?")

print("Answer:" + input())

Inputs:
Joe
2 plus 2
4!

Outputs:
Howdy Joe!
What is 2 plus 2?
Answer:4!
```

Final coding exercise of this lesson: 
figure out how to pull in the inputs and calculate the number of letters in the names that I input. Code must be able to handle any name that is presented.

To do this, use: numOfLetters = len("Angela")
`len()` calculates the number of characters around any piece of text.

My first attempt:

```
name = input()

numOfLetters = len(name)

print(numOfLetters)
```

Result: my code worked for all three test cases. Jack = output of 4. Philipp = output of 7. Ernest Hemingway = output of 16.
My logic was basically that you have to set a constant based on the input so that you could pass that into len().
This was the best way to ensure that, no matter which name is inputted, len() will be able to calculate the characters.

Angela Yu method:
She did it a very different way.

```
print(len(input()))
```

Her logic: first, add the input() function to bring in the input. Then, put it inside the len() function. And finally, put both inside the print() function to output the len function's calculation of the input() characters.

### Variables

Our previous lesson on the input function:

```
input("What is your name?")
```

There wasn't a way to actually capture the input.

But if you give it a name like so:

```
name = input("What is your name?")
```

You can capture it and use the print function to output the captured entry.

As the name variable suggests, it can be changed. For example:

```
name = "Jack"

print(name)

name = "Angela"

print(name)
```

Jack is printed with the first print function, but then Angela is printed with the second print function. The variable changed.

### Coding exercise (variables)

Instructions:

```
This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.

Write a program that switches the values stored in the variables a and b.

Warning . You don't need to print anything. The print statement is already in the template code. However, your program should work for different inputs. e.g. any value of a and b.

Example Input 1
29
41
Example Output 1
a: 41
b: 29
Example Input 2
Hello
World
Example Output 2
a: World
b: Hello
```

My first attempt was wrong. I simply tried to capture the inputs again like so:

```
b = input()
a = input()
```

My second attempt was also wrong. You can't hard code the variables, the test cases will fail:

```
a = "41"
b = "29"
```

The answer is to set a third variable, and then rearrange the variables now that there is a now value temporarily holding the a value.

```
a = input()
b = input()

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)
```

Takeaway from Angela: variables allow you to store values like boxes when you are moving.


### 


