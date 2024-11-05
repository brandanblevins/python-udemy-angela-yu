# Day 3

## Overview

Learn about:

- Conditional statements
- Logical operators
- Code blocks
- Scope

## Control flow with `if / else` and conditional operators

Depending on a particular condition, we do either a or b. In Python, it looks something like this:

```
if condition:
    do this
else:
    do this
```

Flow chart sample: https://viewer.diagrams.net/index.html?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%201#R1VfbcpswEP0apk%2FJAAJfHmM7aR%2FSjlt3ps2jYm1ArUCukC%2Fk67sywqDgJM7Eub0w6Ggl7Z49uwKPjLPNZ0UX6VfJQHihzzYemXhhOIhCfBqgrICIkApIFGcVFDTAjN%2BCBX2LLjmDwjHUUgrNFy44l3kOc%2B1gVCm5ds1upHBPXdAEOsBsTkUX%2FcWZTm1YYb%2FBvwBP0vrkoDesZjJaG9tIipQyuW5B5NwjYyWlrt6yzRiE4a7mpVp3cc%2FszjEFuT5kwTQf3Pz8rmYwjVc%2FVmxzyf%2FJExtGocs6YGAYvx1KpVOZyJyK8wYdKbnMGZhdfRw1NpdSLhAMEPwDWpc2mXSpJUKpzoSdRYdV%2BdusP%2B2RsAauEDjxT%2F1%2BXCOTjT2jGpXt0RQUz0CDsmAVh3H%2BXnosVMilmsMDnNQyoyoB%2FYBdvEsiih8keqNKXKdAUM1Xrh%2FUyjDZ2dmlZ0rRsmWwkDzXRWvnqQHQwBYUIbagbD0FcdzOOr5UO9ajlmsNtFXGE1QyfGOVREHUVon%2FQQQSHUMgHQUEkSuAoe%2FuULllFzXKeKrQer3X15nlYkXF0rJje6tpbT2aoXBGid4m0w%2Bw52ceuehIU6Uyu15ilKN1yjXMFnSbzDVeT67A7GGgNGwe1kQ3h%2FWCoO%2ByVF9b6%2BauCHoWS1v3xN2ktdPe4vjpFJK3KNUj1lZ4YG3dk5eDa%2BtZJIcdnc7QYd2V4o7Y4HE53nAhxlJItV1LWAwDZtpeoZX8C62ZQXhNsDqPI2DiCjjco99wj36jl9Jv1KF2TPNPpgPg5yE8j%2BEj8EV8l6499T7ovyJd8T663gtZYb%2F%2Fvtiqz2%2FR9U12aMKAtcsFFTzJ8X2OgZsPipGhheNPwpmdyDhjVSuFgt%2FS6%2B1WppnaWxb3jUdePDF7YfcsqkZ6JJoHd%2B4gMuywTPaUcPhiLHev8SsoPjzN%2BC%2F7KM%2FRcXjGYfNfWH1cNT%2FX5Pw%2F#%7B%22pageId%22%3A%22EfRIRFBmyNyY66Nj34vM%22%7D


Example:

```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you ride.")
```

Indentation is important for an `if / else` in Python. It needs to follow the format of the example above with the actions indented from the if and else.

*Important equal sign callout*
One `=` sign means you're assigning value to a variable. When you have two `==` signs, you are checking whether the values are equal.


You can use `>` and `<` in combination with `=` to indicate greater/less than or equal to.

## Modulo operator

What is the modulo operator? It looks like the `%` sign, but it's not. It goes between two numbers, so a binary operator, and it works out what is the remainder after division.

```
10 % 5
```

This works as `10 divided by 5 = 2`.


```
10 % 3
```
This works out to be `1`, because that's what is remaining after the division.


## Nested `if` statements and `elif` statements

Use a nested `if / else` statement, once the first condition has passed, we can check for another condition. And then we can have another if/else statement inside.

```
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
```

Example flow chart: https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D


### Elif

You can add as many `elif` conditions as you want.

```
if condition1:
    do this
elif condition2:
    do this
else:
    do this
```


## Coding challenge: BMI calculator with interpretations

Learning objective: Use `if else` and `elif` to upgrade the BMI calculator to give interpretations.

Original challenge:

```
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
```

Instructions:

```
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"

Refer to this graphic for help:
```

My attempt:

```
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi >= 25:
    print("overweight")
else:
    print("normal weight")
```

My code passed the test on the first attempt.


## Multiple `if` statements in succession

Example flow chart: https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%204#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1aoRTeFOb2SJO7ofMnhTCneCEboHowF2A%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D

Use multiple `if` statements to check whether each condition is true. This is unlike an `elif` where only one option will be carried out.

```
if condition 1:
    do A
if condition 2:
    do B
if condition 3:
    do C
```

*Watch the indentation*
Note again that indentation is going to matter greatly to the example being built.


## Coding challenge: Leap year calculator

See file leapyear.py for my attempt.

Angela did this in a much cleaner manner with nested if/else statements:

```
# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
```

Instructions:

```
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.

This is how you work out whether if a particular year is a leap year.

on every year that is divisible by 4 with no remainder

except every year that is evenly divisible by 100 with no remainder

unless the year is also divisible by 400 with no remainder

If english is not your first language or if the above logic is confusing, try using this flow chart .

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

Warning your output should match the Example Output format exactly, including spelling an punctuation.

Example Input 1
2400
Example Output 1
Leap year
Example Input 2
1989
Example Output 2
```

## Coding challenge: Pizza order practice


Instructions:

```
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.
```

Starting code:

```
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
```


## Logical operators

Example flow chart: https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day%203%20Logical%20Operators.drawio#R7VtZc9o6FP41zH2iY0teH0uWZpqkQy%2BZ29CXOwYrthNjUVkQyK%2BvjGWwLbEFL6HTzCSxjyVhfec7myQ68GKy%2BEKcqX%2BPXRR2gOIuOvCyA4CqAYP9SyTLVGJqXOCRwOWNNoJB8Ia4UOHSWeCiuNCQYhzSYFoUjnEUoTEtyBxC8Gux2RMOi586dTwkCAZjJxSlPwKX%2BqnUAuZGfoMCz88%2BWTXs9MnEyRrzmcS%2B4%2BLXnAhedeAFwZimV5PFBQoT8DJc0n7XW56uX4ygiB7SoR9ZTw%2FfyQD19fm%2Fc3dxF%2FzCXT6NmC6zCSOXzZ%2FfYkJ97OHICa820h7Bs8hFyagKu9u0ucN4yoQqEz4jSpdcmc6MYiby6STkT9kLk%2BVj0v%2BTAUEmGDJBV%2FmkmHomuVzwz0jvlvm7PiLBBFFEuFBEgwMU4xkZox0QZKxyiIfojnZ62i7BJ%2FcBHOsvCLO3IUvWgKDQocG8yB%2BH09Bbt%2BNdPxPiLHMNpjiIaJwbuZ8IWANuUZABthqR25Oq63mts4t0xOwu92ob0YoZR7DEbpklmqrlWaJ8TIJotRBEYICqFQlgK8UR0vfknTbMOJZohtE8zzgWcyeccXS4b01cm%2BFMGHF6Hl0pU1GZz5904LVATeLjyWjGZtl79QOKBlNnpd1XFp%2BKBNvKiDkiFC126jB7qppFlLKw9bqJFarBZX4uTpSVlld7DuPjIYRtmOr7bQscaFtq1bZ1EshA4OmAzYCKVFwDq%2B6n41MQhhc4xGTVF7o6stzE7cWU4BeUe2KBEWTWWQ2BYZHAQMJfIOGvVhd%2FNQHaCyf6J%2FEALD1EpyFcAV5QKcIlsXfLrAeuy682%2BL%2F%2FzaXPLvk%2BvOl71zdexsRzMXddNHfptD6WuesyTn4URgKzZMENUlLuqhUBrm9YgInNjhaxcMLAi9j1mGGRZG29BIOAVWKf%2BYNJ4LopgVEcvDmj1VAJhXkqw8bVex39MhmLcTZO6VsRzFYp0ENbQBlK%2FCSoDWUxVxqi%2BOxhBpa2F2etJpylnkiMR2143FwttK6OD6mEDvLUuzzwXk9tVO2p5dUIUJKZ55kBgV4cZEvd847aRA6I8lfx%2BXZWWyFa%2FtZ%2FzbLQzm4tgVKGP3%2B8PfT6PwfImj8%2BPAS9STtZKloE9DF3Pdzoid1tNJPcFFaO2laoFMLWMuJdb52LiskyepsrMcASAoQiSYQlqYNeW23Wsk9qhsD1JADHrlaqsKh8zSpthpTzCRvual9c3tzbWy8XUzXnIoYkKWUq1HTRBBuuRu3i%2Bgi0RBu0a1pOkiJlCkjdoThOHK6%2FKuElecO5lUxqGfMD%2FV5tJRNoJVN%2BvwerPJPdsnMHyhFKL6ugZrdhbXEb4iZw84tYejl6t%2B051vRpJ3qrzUTvyuuEd0VvXTkuekPNOiF6l3s3Hb3tLWYoiUVN26FmfLD4LVnmVEFXtc4%2BakNV8Hi6iLXeZNxWoYg1A1rBJPnDpnb%2BoB%2BQKpmNpkqyTH6rD1D2%2BwBhs9gYW2j0VNpejnCUqMB1Yn%2FtXCqAVzeL8AKJ91Bl%2BK6PSJwCsH3%2F%2BGI8erfgFvwKlvfPN8v%2BfVekdBtR%2FaD4vGvZJ7885M%2FnXfx0iYKv9n%2Bz5a06uDNesnnWncPqalHDh2awRx8%2BsuSZcmWnj3ZgLcRlsZxpOiwbWnthWQqVaFafPYYHUJIlCKXLfnVxLeLcooVuvm9BsYpoITXyViqSg3zXLp%2B013dVfrD2JJBbCRDZXkW2IXHkXgWofrPiJI2aH0qjorN6dSJ%2BpjRMPNKIZbbG6lzp1MfMi5x0qlTIwJTVjzwDq8BLlQ%2FqrkNyPulSbNFNWXW5Ka1VC1pbzTD3pIXdvl2u7swMSDz%2FliZG4lnjoxKjpi0FlnZtDNlhbaWmNEoKrFj9%2FQlnuMo4r9fXGjjDtcuacjA%2F%2BCgxQ0ydpPMoSMeIVzFBW5wXrVmeWoDblKSpKrCz1aZGiC3uNPwBR0ABLEVaCa8rOgPKbjdfDEzr283XK%2BHVbw%3D%3D#%7B%22pageId%22%3A%22DZ4nxZ1rhDQOUQN3S9Ux%22%7D


Logical operators: `and`, `or`, and `not`.

`and`: everything in a line of code has to be true. If anything is not true, everything becomes false. Example: `a > 10 and a < 13`

`or`: evaluates whether either option in a line of code is true.

`not`: reverses a condition. If it's `false`, it becomes `true`. If `true`, it becomes `false`. Example: `not a < 0` if it is false outputs as true.

We're going to incorporate this logic into our rollercoaster example.


## Quiz 4

Q1: What will the following code evaluate to? `not 5 == 5`
Answer: False

Q2: What will the following code evaluate to? `False or True or False`
Answer: True

Q3: What will the following code print?
```
a = 5
b = 7

if a > b and a != b:
    print("A")
elif not a >= b and a != b:
    print ("B")
else:
    print("C")
```
Answer: B


# Day 3 project: Treasure Island

Basically create a game using the flowchart that I've uploaded to this folder. 

My version is: treasureislandgame.py

