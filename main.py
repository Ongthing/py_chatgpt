# (1). Variable = A container for value behaves as the value that is contains
# A variable is a name that stores data in memory. it acts like a container for values.
#  in python, you create a variable by assigning a value to a name using the = operator

x = 10 # x stores the value 10
name = 'bro' # name stores the string 'dude'

# 0. Rules for Naming Variable
# 1. Must start with a number
# 2. Cannot start with a number
# 3. can contain letters, numbers, and underscores
# 4. Case-sensitive (age and Age are different)
# 5. Cannot use python keywords(e.g., class, if , def)

name = "dude"
age = 21
height = 250.5

print(name)
print(age)
print(height) # Output: Ongthing 21 250.5

# Using Variables in f-Strings (strings Formatting)
# python allows inserting variables into string using f-strings.

name = "bro"
age = 25
print(f"My name is {name} and I am {age} years old")


# Declaring a Variable in python
# You don't need to declare the type of a variable explicitly. python automatically assigns the data type based on the value

# Assigning values to variables

x = 10 # Integer
y = 3.14 # Float
name = "Dude" # String
is_active = True # Boolean

print(x)
print(y)
print(name)
print(is_active)

# 4.Valid Variable Names:  ✓
my_variable = 10
_name = 'Ongthing'
age123 = 25
myVar = "Hello"

# Invalid Variable Names:

# 1number = 5 # Cannot start with a number
#
# my-variable = 10 # Cannot contain hyphens (-), use underscore (_)
#
# if = "Hello" # Cannot use python keywords


# Variable Type Checking
# You can check the type of a variable using type():


x = 100 # Integer
print(type(x)) # Output: <class 'int'>

name = "Bro" # String(Text)
print(type(name)) # Output: <class 'str'>

price = 19.99 # Float(Decimal number)
print(type(price)) # Output: <class 'float'>

is_active = True # Boolean (True/False)
print(type(is_active))  # Output: <class 'bool'>

# Changing variable Type(type casting)
# python allows converting one data type into another using:

# int() - Converts to integer
# float() - Converts to floating-point
# str() - Converts to string
# list() - Converts to list
# tuple() - Converts to tuple




a = 10 # Integer
b = str(a) # Convert to string
c = float(a) # Convert to float

print(b,type(b)) # Output: '10' <class 'str'>
print(c,type(c)) # Output: '10.0' <class 'float'>

# More on type casting (converting data types)
# python automatically converts data types when needed, but sometimes you need manual conversion

# ✓ Implicit Conversion (python does it automatically):

a = 5
b = 2.5
result = a + b # int + float - float
print(result) # Output: 7.5

# ✓ Explicit Conversion (Manual type casting)

x = "100"
y = int(x) # Converts string "100" to integer "100" to integer 100
print(y + 10)  # Output: 110

num = 10
text = str(num) # Converts integer to string
print(text + " apples") # Output: 10 apples

# Using Variables in Operations
# Variables can be used in calculations.

a = 10
b = 5
sum = a + b
print(sum) # Output: 15

# Deleting a Variable
# you  delete a variable using del.

x = 50
del x # Deletes the variable
#print(x)  Error: NameError: name 'x' is not defined

# Updating Variable

count = 10
count += 1
print(count) # Output: 11

# String Manipulation
# You can combine variables of the same type.

first_name = "Ongthing"
last_name = "Marma"
full_name = first_name+" "+last_name
print("Hello "+full_name) # Output: Hello Ongthing Marma

# Adding Number:
a = 5
b = 10
total = a + b
print(total) # Output: 15

# Note: if you try to combine a string and a number directly, python will give an error. You must convert them using str()
# Example

age = 25
print("I am " +str(age) + "Years old")
# Updating Variable Expression

price_per_items = 20
quantity = 10
total_price = price_per_items * quantity
print("Total: ",total_price) # Output 200

# Swapping Variable

a, b = 5, 10
a, b = b, a # Swaps the values
print(a, b) # Output: 10 5

a = 5
b = 10
a,b = b,a
print("a: ",a)
print("b: ",b)  # Output: 5 10

# You can also unpack a list or tuple into multiple variable:

number = [1, 2, 3]
x, y , z = number
print(x, y, z) # Output: 1 2 3

# Multiple assignment / Assigning multiple variables
# allow us to the design multiple variable at the same time in one line of code
# python allows assigning multiple variable in one line.

name, age, attractive = "Ongthing",21,True
print(name)
print(age)
print(attractive)
# Output: Ongthing 21 True

Bro = Ongthing = Dude = 30
print(Bro)
print(Ongthing)
print(Dude) # Output: 30 30 30

a, b, c = 5, 10, 15
print(a, b, c) # Output: 5 10 15

# Assigning the same value to multiple variables

x = y = z = 20
print(x, y, z) # Output: 20 20 20


# Changing Variable values
# A variable's value can be changed anytime

x = 10
x = 20 # Now x stores 20
print(x)

#  Constants in python
# A constant is a variable that should not change. python does not have built-in constants,
# but by convention, we use uppercase names to indicate constants
PI = 3.14159
GRAVITY = 9.8

#  Checking if a Variable Exists
# you can check if a variable exists using globals() or locals().

x = 10
print("x" in globals()) # Output: True
print("y" in globals()) # Output: False

#  Using isinstance() to Check Variable Type
# the isinstane () function checks if a variable belongs to a specific data type

y = 100
print(isinstance(y, int)) # Output: True
print(isinstance(y, str)) # Output: False

# (2).Input
# what is input() in python?
# The input() function in python is used to take user input from the keyboard. it allows the user to enter
# data while the program

# 1. Basic input Example

name = input("Enter your name: ")
# Taking integer input
age = int(input("Enter your age: "))
# Taking Float input
height = float(input("How tall are you: "))

print("Hello, " + name + "!")
print("You are", age, "years old")
print("You are", height, "cm tall")

# integer input
age = int(input("Enter your age: "))

print("Next year, you will be", age + 1, "years old")

# Input with Calculation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)


# Taking Multiple Inputs at Once
# Space-Separated input
# We can use split() to take multiple values from a single input.

x, y = input("Enter two numbers: ").split()
x, y = int(x), int(y) # Convert to integer
print("Sum: ", x + y)

# Comma-Separated input

x, y, z = map(float, input("Enter three numbers separated by commas: ").split(","))
print("Average: ", (x + y + z) / 3)


# (3). string method
# 1. lower() - convert to lowercase
# Converts all characters to lowercase

text = "HELLO WORLD"
print(text.lower()) # Output: hello world

# 2. upper() - Convert to Uppercase

text = "hello world"
print(text.upper()) # Output: HELLO WORLD

# 3. title() - Convert to Title case
# Capitalizes the first letter of each world

text = "hello world"
print(text.title()) # Output: Hello World

# 4. capitalize() - Capitalize First Letter
# Only the first letter of the string becomes uppercase

text = "hello world"
print(text.capitalize()) # Output: Hello World

# 5. Removing Spaces and Characters
# strip() - Remove Leading and Trailing Spaces

text = " hello world "
print(text.strip()) # Output: "hello world"

# 6. istrip() - Remove Left Spaces

text = " hello world "
print(text.istrip()) # Output: "hello world"

# 7. rstrip() - Remove Right Spaces

text = " hello world "
print(text.rstrip()) # Output: hello world

# 8. Checking String Content
# startswith() - Check if string starts with a word

text = "python is great"
print(text.startswith("python")) # Output: True
print(text.startswith("java")) # Output: False

# 9. endswith() - check if string ends with a world

text = "Python is great"
print(text.endswith("great")) # Output: True
print(text.endswith("Python")) # Output: False

# 10. isalpha() - check if string contains only letters

text = "HelloWorld"
print(text.isalpha()) # Output: True

text = "Hello123"
print(text.isalpha()) # Output: False

# 11. isdigit () - check if string contains only numbers

text = "12345"
print(text.isdigit()) # Output: True

text = "123abc"
print(text.isdigit()) # Output: False

# 12. isalnum() - Check if string contains letter and numbers

text = "Hello123"
print(text.isalnum()) # Output: True

text = "Hello 123"
print(text.isalnum()) # Output: False (Because of space)

# 13. isspace()- check if string is only spaces

text = "   "
print(text.isspace()) # Output: True

text = "Hello world"
print(text.isspace()) # Output: False

# 14. Finding and Replacing in strings
# find()- find a substring in a string
# Returns the index position of the first occurrence.

text = "Python is fun"
print(text.find("is")) # Output: 7
print(text.find("Java")) # Output: -1 (Not found)

# 15. replace()- Replace a word in a string

text = "I love Java"
print(text.replace("Java", "Python")) # Output: I love Python

# 16. Splitting and Joining string
# split() - split a string into a list
# splits by spaces or a specific character

text = "apple,banana,orange"
print(text.split(",")) # Output: ['apple', 'banana', 'orange']

# 17. join()- Join a list into a string

words = ['Hello', 'World']
print(" ".join(words)) # Output: Hello world

# 18. String formating
# format()-format strings dynamically

name = "bro"
age = 25
print("My name is {} and I am {} years old.".format(name,age))
# Output: My name is bro and I am 25 years old.

# 19. f-strings- Modern Formatting (python 3.6+)

name = "bro"
age = 25
print(f"My name is {name} and I am {age} years old. ")
# Output: My name is bro and I am 25 years old.

# 20. Counting and checking characters
# count()- count occurrences of a word

text = "banana apple banana"
print(text.count("banana")) # Output: 2

# 21. len()- Get the length of a string

text = "Hello"
print(len(text)) # Output: 5

# Changing case for special conditions
# swapcase()- Swap Upper and Lower Case

text = "Hello World"
print(text.swapcase()) # Output: hELLO wORLD

# 22. casefold()- Case-insensitive comparisons
# More aggressive than lower(), used for international characters

text = "strabe"
print(text.casefold()) # Output: strasse

# 23. Padding and Centering strings
# center()- center a string with padding

text = "Hello"
print(text.center(10, "-")) # Output: __Hello___

# 24. ljust()- Left align with padding

text = "Hello"
print(text.ljust(10, "-")) # Output: Hello------

# 25. rjust()- Right Align with padding

text = "Hello"
print(text.rjust(10, "-")) # Output: ------Hello

# 26. Checking prfix and suffix
# startwith() - Does string start with a word

text = "Python is awesome"
print(text.startswith("Python")) # Output: True

# 27. endswith()- Does string end with a word

text = "Learn Python"
print(text.endswith("Python")) # Output: True


# Math function
# importing the math module
# before using advanced math functions, import the math module

# basic math functions
# 1. math.ceil(x)- Round Up
# returns the smallest integer greater than or equal to x.

import math
print(math.ceil(4.2)) # Output: 5
print(math.ceil(7.8)) # Output: 8

# 2. math.floor(x)-Round Down
# returns the largest integer less than or equal to x.

print(math.floor(4.9)) # Output: 4
print(math.floor(7.1)) # Output: 7

# 3. math.trunc(x)-Remove decimal part
# Removes the decimal part and returns only the integer

print(math.trunc(5.7)) # Output: 5
print(math.trunc(-3.9)) # Output: -3

# 4. round(x, n) -Round to n Decimal places
# Rounds x to n decimal places.

print(round(3.14159, 2)) # Output: 3.14
print(round(2.567, 1)) # Output: 2.6

# 5. Power and Logarithms
# math.pow(x, y) - Power Function
# Returns x raised to the power y.

print(math.pow(2, 3)) # Output: 8.0
print(math.pow(5, 2)) # Output: 25.0

# 6. math.sqrt(x)- Sqaure Root
# returns the square root of x

print(math.sqrt(16)) # Output: 4.0
print(math.sqrt(25)) # Output: 5.0

# 7. math.exp(x) - Exponential function
# Returns e^x(where e = 2.718)

print(math.exp(2)) # Output: 7.38905609893065

# 8. math.log(x) - Natural Logarithm (Base e)
# returns the log of x to base e (in x)

print(math.log(10)) # Output: 2.302585092994046

# math.log10(x) - Logarithm base 10
# returns the log of x to base 10.
print(math.log10(100)) # Output: 2.0

# math.log2(x) - Logarithm Base 2
# Returns the log of x to base 2.

print(math.log2(8)) # Output: 3.0

# 9. Trigonometric Functions
# math.sin(x), math.cos(x), math.tan(x)
# Returns sine, cosine, and tangent of x (in radians)

print(math.sin(math.radians(30))) # Output: 0.5
print(math.cos(math.radians(60))) # Output: 0.5
print(math.tan(math.radians(45))) # Output: 1.0

# 10. math.asin(x), math.acos(x), math.atan(x)
# inverse sine, cosine, and tangent(gives result in radians)
print(math.degrees(math.asin(0.5))) # Output: 30.0
print(math.degrees(math.acos(0.5))) # Output: 60.0
print(math.degrees(math.atan(1))) # Output: 45.0

# 11 math.radians(x) and math.degrees(x)
# convert between degrees and radians.

print(math.radians(180)) # Output: 3.141592653589793
print(math.degrees(math.pi)) # Output: 180.0

# 12. Factorial and GCD (Greatest Common Divisor)
# math.factorial (x) - Factorial
# computes x! (factorial of x)

print(math.factorial(5)) # Output: 120 (5! = 5x4x3x2x1)

# math.gcd(a, b) - Greatest common divisor
# finds the largest number that divides both a and b

print(math.gcd(12, 18)) # Output: 6

# 13. Random Number Functions (Using random Module)
# python's random module helps generate random numbers.
# Returns a random integer between a and b.

import random
print(random.randint(1, 10)) # Output: random number between 1 and 10

# 14. random.random() - random float between 0 and 1

print(random.random()) # Output: random number between 0.0 and 1.0


# 15. random.uniform(a, b) - Random float between a and b

print(random.uniform(1, 10)) # Output: Random float between 1 and 10

# 16. random.choice(list) - Random element from a list

colors = ["red","blue", "green"]
print(random.choice(colors)) # Output: Randomly chosen color

# 17. random.shuffle(list) - shuffle a list

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers) # Output: Randomly shuffled list


# Indexing and slice notation
# python allows positive indexing (left to right) and negative (right to left)

text = "HELLO"
print(text[0]) # Output: H
print(text[-1]) # Output: O

# Basic string slicing syntax
# string[start:end:step]

# start --- The index where slicing starts(included)
# end ---- The index where slicing stops (not included)
# step --- The step size (optional default is 1)

# Basic slicing Example
# ✓ slice a substring

text = "PYTHON"
print(text[0:3]) # Output: PYT
#(indexs 0, 1, 2)
print(text[2:5]) # Output: THO
# (Indexes 2, 3, 4)

# ✓ Omitting start or End index

text = "PYTHON"
print(text[:4]) # Output: PYTH
# from start to index 3)
print(text[2:]) # Output: THON
# (from index 2 to end)

# ✓ Full string copy)

text = "PYTHON"
print(text[:]) # Output: PYTHON
# (full string)

# Negative indexing in slicing
# ✓ Slice using negative indexes

text = "PYTHON"
print(text[-4:-1]) # Output: YTH
# (indexes -4, -3, -2)

# ✓ slice from negative index to end

text = "PYHON"
print(text[-3:]) # Output: HON
# indexes -3 to end)

# ✓ slice from start to a negative index

text = "PYTHON"
print(text[:-2]) # Output: PYT
# ( from start to index -3)

# Using step in slicing
# ✓ Skip characters with step

text = "PYTHON"
print(text[0:6:2]) # Output: PTO
# (every 2nd character)

# ✓ Reverse a string

text = "PYTHON"
print(text[::-1]) # Output: OHT
# (indexes 4,3,2)

# note string[start:end] , string[:end] , string[start:] , string[::step], string[::-1] reverses the string

# Python if statement
# The if statement in python is used for decision-making. it checks a condition and executes the code block only
# if the condition is True.

# ✓ Basic if statement
# if condition:
    # code runs if condition is True

age = 18
if age >= 18:
    print("You are eligible to vote.")
# You are eligible to vote.

# ✓ if-else Statement
# The else block runs if the if condition is False.

# if condition:
    # Runs if condition is True
# else:
    # Runs if condition is False

age = 16
if age >=18:
    print("You can vote.")
else:
    print("You cannot vote.")
# Output: You cannot vote.

# ✓ if-elif-else(Multiple Conditions)
# Use elif(short for "else if") to check multiple conditions.

# if condition1:
    # Runs if condition1 is True.
# elif condition2:
    # Runs if condition2 is True.
# else:
    # Runs if none of the conditions are True.

marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C")
# Output: Grade: B

# ✓ Using if with Logical Operators(and, or, not)
# and (both conditions must be True)

age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter.")
else:
    print("You cannot enter.")
# Output: You can enter.

# ✓ or (At least one condition must be True)

is_sunny = False
has_umbrella = True

if is_sunny or has_umbrella:
    print("You can go outside")
# Output: You can go outside

# ✓ not(Reverses the condition)

is_raining = False
if not is_raining:
    print("Go for a walk.")
# Output: Go for a walk.

# ✓ Short-Hand if (Ternary Operator)
# python allows a one-line if statement

x = 10
print("Positive") if x > 0 else
print("Negative")
# Output: Positive

# While Loop
# A while loop runs as long as a condition is True. It is useful when you don't know in advance
# how many times the loop should run.

# ✓ Basic while Loop

# while condition:
    # code inside loop

count = 1
while count <= 5:
    print(count)
    count += 1 # Increase count by 1
# Output: 1 2 3 4 5
# The loop runs until count is greater than 5.

# ✓ while Loop with else
# If the loop condition becomes False, the else block executes.

x = 3
while x > 0:
    print(x)
    x -= 1
else:
    print("Loop finished!")
# Output: 3 2 1 Loop finished!

# ✓ Infinite Loop (Be careful!)
# if the condition never become False, the loop runs forever

while True:
    print("This is an infinite loop!")
# Note: To stop the loop, press Ctrl + C in the terminal

#  ✓ break Statement (Exit the loop)
# The break statement stops the loop immediately

x = 1
while x <= 5:
    if x == 3:
        break
    print(x)
    x += 1
# Output: 1 2

#  ✓ continue Statement (skip Current Iteration)
# The continue statement skips the rest of the loop and goes to the next iteration

x = 0
while x < 5:
    x += 1
    if x == 3:
        continue # skip printing 3
    print(x)
# Output: 1 2 4 5

# ✓ Using while loop with User input
# A while loop is useful when waiting for user input.

password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access granted!")

# for Loop
# A for loop in python is used to iterate over a sequence (list,tuple,string,range,etc.)
# It executes the loop body once for each item in the sequence.

# ✓ Basic for Loop

# for variable in sequene:
    # code to execute

# ✓ Loop through a list

fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(fruits)
# Output: apple banana cherry
# note: the loop iterates through each element in the list.

# ✓ Using for Loop with range()
# The range() function generates a sequence of numbers.

# ✓ Print numbers from 1 to 5

for i in range(1, 6):
    print(i) # Output: 1 2 3 4 5

# ✓ Using for Loop with strings
# A string is a sequence of characters, so a for loop can loop an iterate over each

text = "PYTHON"
for char in text:
    print(char) # Output: P Y T H O N

# ✓ Using for Loop with else
# The else block runs after the loop completes normally

for i in range(3):
    print(i)
else:
    print("Loop finished!")
# Output: 0 1 2 Loop finished!

# ✓ Using break to Exit a for loop
# The break statement stops the loop immediately

for num in range(1, 6):
    if num == 3:
        break
    pirnt(num) # Output: 1 2

# ✓ Using continue to skip an iteration
# The continue statement skips the rest of the code in the current iteration and moves to the next one.

for num in range(1, 6):
    if num == 3:
        continue # skip 3
    print(num) # Output: 1 2 4 5

# ✓ Nested for loop
# A for loop inside another for loop.

for i in range(1, 3): # outer loop
    for j in range(1, 4): # Inner loop
        print(f"i={i}, j={j}")

# Output: i=1,i=1,i=1,i=2,i=2,i=2,j=1,j=1,j=1,j=2,j=2,j=2

# ✓ Looping through a dictionary
# We can iterate over keys and values in a dictionary.

student = {"name": "Bro", "age": 20, "grade": "A"}
for key, value in student.items():
    print(key, ":", value)
# Output: name: Bro age: 20 grade: A

# ✓ iterating over a list with enumerate()
# The enumerate() function returns both index and value while looping

fruits = ["apple", "banana", "cherry"]
for index, fruits in enumerate(fruits):
    print(index, fruits)
# Output: 0 apple 1 banana 2 cherry

# ✓ Looping in reverse order
# We can loop in reverse using range(start, stop, step)

for i in range(5, 0, -1):
    print(i) # Output: 5 4 3 2 1

# Nested loops
# A nested loop is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop.

# ✓ Basic Nested for loop

# for outer in range(outer_loop_range):
    # for inner in range(inner_loop_range):
        # Code inside inner loop

# ✓ Printing pairs

for i in range(3): # Outer loop runs 3 times
    for j in range(2): # Inner loop runs 2 times per outer loop iteration
        print(f"i={i}, j={j}")
# Output: i=0,i=0,i=1,i=1,i=2,i=2, j=0,j=1,j=0,j=1,j=0,j=1
# How it works:
# ✓ i = 0,inner loops runs for j = 0, 1
# ✓ i = 1,inner loops runs for j = 0, 1
# ✓ i = 2,inner loops runs for j = 0, 1

# ✓ Nested while Loop

i = 1
while i <= 3: # Outer loop
    j = 1
    while j <= 2: # Inner loop
        pirnt(f"i={i}, j={j}")
        j += 1
    i += 1
# Output: i=1,i=1,i=2,i=2,i=3,i=3, j=1,j=2,j=1,j=2,j=1,j=2

# ✓ Nested for loop for Multiplication Table

for i in range(1, 4): # Outer loop (row)
    for j in range(1, 4): # Inner loop(column)
        print(f"{i} x {j} = {i*j}")
    print("_____________") # Separator after each row

# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
#_________

# ✓ Nested loop to print a pattern
# Right- Angle Triangle

row = 5
for i in range(1, row + 1):
    for j in range(i):
        print("*", end=" ") # print * without a new line
    print() # Move to the next line
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# Note: the outer loop controls the number of rows, and the inner loop controls the numbers
# of * printed per row

# ✓ Nested loop with break
# The break statement exits the inner loop only, but the outer loop continues.

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break # Stops inner loop when j == 2
        print(f"i={i}, j={j}") # Output: i=1,i=2,i=3, j=1,j=1,j=1

# ✓ Nested loop with continue
# The continue statement skips the current iteration of the inner loop but continues with the next iteration

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue # skips j=2
        print(f"i={i}, j={j}")
# Output:
# i=1,i=1,i=2,i=2,i=3,i=3, j=1,j=3,j=1,j=3,j=1,j=3

# ✓ Iterating over nested lists
# Accessing Matrix elements

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7,8,9,]
]
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()
# Output: 1 2 3 4 5 6 7 8 9
# Note: The outer loop iterates through rows, and the inner loop iterates through elements in each row

# ✓ Nested loop to create a Number pyramid

row = 5
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Python Loop control statement
# loop control statement change the execution flow of loops (for and while).
# There are three main loop control statements  in python

# ✓ 1 break - Stops the loop immediately
# ✓ 2 continue - Skips the current iteration and moves to the next one
# ✓ pass - Does nothing; used as a placeholder

# ✓ break Statement (Exit the loop early)
# The break statement stops the loop immediately, even if iterations are remaining

# Using break in a for Loop

for num in range(1, 6):
    if num == 3:
        break # Loop exits when num is 3

    print(num) # Output: 1 2
# when num == 3, the break statement stops the loop completely

# Using break in a while Loop

i = 1
while i <= 5:
    if i == 3:
        break # Stops when i is 3
    print(i)
    i += 1 # Output: 1 2

# continue Statement (skip an iteration)
# The continue statement skips the current iteration but does not stop the loop.

# Using continue in a for loop

for num in range(1, 6):
    if num == 3:
        continue # Skips when num is 3
    print(num) # Output: 1 2 4 5

# When num == 3, the continue statement skips printing 3 and moves to the next iteration

# Using continue in a while Loop

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue # Skips when i is 3
    print(i) # Output: 1 2 4 5

# ✓ pass Statement (Do nothing-placeholder)
# The pass statement does nothing. it is used when a statement is required nut no action is needed

# Using pass in a for Loop

for num in range(1, 6):
    if num == 3:
        pass # Does nothing, just a placeholder
    print(num) # Output: 1 2 3 4 5
# Note: pass does not affect the loop execution; it's just a placeholder

# Using pass in a while Loop

i = 1
while i <= 5:
    if i == 3:
        pass # Placeholder, does nothing
    print(i)
    i += 1
# Output: 1 2 3 4 5

# Python List
# A list a mutable (changeable) collection of elements in python. lists can store multiple values of
# different data types (e.g., numbers, strings, booleans).

# ✓ Creating a List

list_name = [item1, item2, ...]

# Creating different lists

numbers = [1, 2, 3, 4, 5] # List of number
fruits = ["apple", "banana", "cherry"] # List of strings
mixed = [1, "hello", 3.5, True] # Mixed data types
empty_list = [] # Empty list

# ✓ Accessing List Elements
# We use indexing (starting from 0) to access elements
fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # First element
print(fruits[1]) # Second element
print(fruits[-1]) # Last element (negative indexing)
# Output: apple banana cherry

# ✓ Changing List elements
# Lists are mutable, meaning we can modify elements.

fruits = ["apple", "banana", "cherry"]

fruits[1] = "mango" # Change banana to mango
print(fruits) # Output: [ 'apple', 'mango', 'cherry']

# ✓ Adding elements to a list
# Using append(add to end)

fruits = ["apple", "banana"]
fruits.append("cherry") # add to the end
print(fruits) # Output: ['apple', 'banana', 'cherry']

# Using insert() (Add specific index)

fruits.insert(1, "mango") # Insert mango at index 1
# Output: ['apple', 'mango', 'banana']

# ✓ Using extend() (Merge two lists)

list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2) # Merge list2 into list1
print(list1) # Output: [1, 2, 3, 4, 5]

# ✓ Removing Elements from a List
# Using remove() (Remove by value)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") # Remove "banana"
print(fruits) # Output: ['apple', 'cherry']

# ✓ Using pop() (Remove by index, Default Last)

fruits = ["apple", "banana", "cherry"]
fruits.pop(1) # Remove item at index 1
print(fruits) # Output: ['apple', 'cherry']

# ✓ Using clear() (Remove all elements)

fruits = ["apple", "banana", "cherry"]
fruits.clear() # Empty the list
print(fruits) # Output: []

# ✓ Looping Through a list
# Using for loop

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) # Output: apple banana cherry
# Using while Loop

fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
# Output: apple banana cherry

# ✓ List slicing
# When can extract a portion of a list using slicing

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6]) # From index 2 to 5
print(numbers[:4]) # From start to index 3
print(numbers[5:]) # From index 5 to end
print(numbers[::2]) # Every second element
print(numbers[::-1]) # Reverse the list

# ✓ Checking if an item exits

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list") # Output: Banana is in the list

# ✓ Using sort(reverse=True)(Descending Order)

numbers.sort(reverse=True)
print(numbers) # Output: [8, 5, 3, 2, 1]

# Using sorted() (Returns a new sorted list without modifying original)

numbers = [5, 3, 8, 1, 2]
sorted_number = sorted(numbers)
print(sorted_number) # Output: [1, 2, 3, 5, 8]

# ✓ Copying a List

fruits = ["apple", "banana", "cherry"]
copy_fruits = fruits.copy()
print(copy_fruits) # Output: ['apple', 'banana', 'cherry']

# Tuple
# A tuple is immutable (unchangeable) collection of ordered elements in python. Tuples are similar to lists
# But cannot be modified once created. Tuples can contain multiple data types, including numbers, strings, or booleans.

# ✓ Creating a tuple

# tuple_name = (item1, item2, item3,....)

#  ✓ Creating different tuples

# Tuple with numbers
numbers = (1, 2, 3, 4, 5)

# Tuple with strings
fruits = ("apple", "banana", "cherry")

# Mixed  data types
mixed = (1, "hello", 3.5, True)

# Empty tuple
empty_tuple = ()

# Single-element tuple (note the trailing comma)
single_element = (5,)

# ✓ Accessing Tuple elements
# Tuple use indexing(starting from 0) to access elements.

fruits = ("apple", "banana", "cherry")
print(fruits[0]) # First element
print(fruits[1]) # Second element
print(fruits[2]) # Last element
print(fruits[-1]) # (negative indexing)
# Output: apple banana cherry

# ✓ Slicing Tuples
# we can extract a portion of a tuple using slicing

numbers = (0, 1, 2, 4, 5, 6, 7, 8, 9)
print(numbers[2:6]) # From index 2 to 5
print(numbers[:4]) # From start to index 3
print(numbers[5:]) # From index 5 to end
print(numbers[::2]) # Every second element
print(number[::-1]) # Reverse the tuple

# ✓ Tuple concatenation and Repetition
# Concatenating tuples(Joining tuples)
# You can join or more tuples using the + operator

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined) # Output: (1, 2, 3, 4, 5, 6)

# Repeating tuples
# You can repeat a tuple multiple times using the * operator

tuple1 = (1, 2, 3)
repeated = tuple1 * 3
print(repeated) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# ✓ Nested tuples
# A tuple can contain another tuple. creating a nested tuple.

nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1]) # Accessing the second tuple(2, 3)
# Output: (2, 3)

# ✓ Tuple methods
# Although tuples are immutable, there are some methods available for them.
# count()- counts occurrences of a specified elements in the tuple.

tuple1 = (1, 2, 3, 1, 1)
print(tuple1.count(1)) # Count how many times '1' appears
# Output: 3

#  ✓ index()- Returns the index of the first occurrence of a specifled element.

tuple1 = (10, 20, 30, 40)
print(tuple1.index(30)) # Find the index of '30'
# Output: 2

# ✓ Tuple immutability
# Unlike lists, tuples are immutable, which means we cannot modify the elements one the tuple is created.

tuple1 = (1, 2, 3)
tuple1[1] = 4 # Error: 'tuple' object does not support item assignment

# ✓ Checking for existence
# You can check if an element exists in a tuple using the in operator.

fruits = ("apple", "banana", "cherry")
if "banana" in fruits:
    print("banana is in the tuple") # Output: banana is in the tuple

# ✓ Tuple Length
# You can find the length of a tuple using the len() function.

fruits = ("apple", "banana", "cherry")
print(len(fruits)) # 3

# ✓ Tuple assignment (Unpacking)
# You can unpack the values of a tuple into individual variables.

coordinates = (1, 2, 3)
x, y, z = coordinates # Unpacking the tuple
print(x, y, z) # Output: 1 2 3

# Set
# A set is a collection of unordered, unique elements. sets are useful when you need to store multiple items without
# duplicates, and order doesn't matter. sets are also mutable, meaning you can add or remove elements.

# ✓ Creating a set
# set_name = {item1, item2, item3, ...)

# ✓ Creating different sets

# set with numbers
numbers = {1, 2, 3, 4, 5}

# set with strings
fruits = {"apple", "banana", "cherry"}

# Mixed data types
mixed = {1, "hello", 3.5, True}

# Empty set (note: an empty set is not just {} but set()
empty_set = set()

# ✓ Accessing set elements
# Note: since sets are unordered, you cannot access elements by index. However, you can loop through the set
# using a for loop

# ✓ Looping through a set
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit) # apple banana cherry
# Note: The order of elements may vary since sets are unordered.

# ✓ Adding elements to a set
# Using add()

fruits = {"apple", "banana"}
fruits.add("cherry") # Add "cherry" to the set
print(fruits) # Output: {'banana', 'apple', 'cherry'}

# ✓ Using update() (Add multiple elements)

fruits = {"apple", "banana", "cherry"}
fruits.update({"cherry", "orange"})
print(fruits) # Output: {'banana', 'apple', 'orange', 'cherry'}

# ✓ Removing elements from a set
# Using remove() (Raises an error if the element is not found)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) # Output: {'apple', 'cherry'}

# ✓ Using discard() (Does not raise an error if the element is not found)

fruits = {"apple", "banana", "cherry"}
fruits.discard("orange") # 'orange' does not exist, no error
print(fruits) # Output: {'banana', 'apple', 'cherry'}

# ✓ Using pop() (Removes and returns an arbitrary element)

fruits = {"apple", "banana", "cherry"}
remove_element = fruits.pop()
print(remove_element)
print(fruits)
# Output: apple {'banana', 'cherry'}

# Note: The element removed is arbitrary, as sets are unordered

#  ✓ Using clear() (Removes all elements)

fruits = {"apple", "cherry", "banana"}
fruits.clear()
print(fruits) # Output: set()

#  ✓ Set operations
# Union(|) - combine elements from two sets(no duplicates)

set1 = {1, 2, 3}
set2= {3, 4, 5}
union_set = set1 | set2
print(union_set) # Output: {1, 2, 3, 4, 5}

# ✓ Intersection (&) - get elements that are in both sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set) # Output: {3}

# ✓ Difference (-)- get elements that are in one set but not the other.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
different_set = set1 - set2
print(different_set) # Output: {1, 2}

# ✓ Symmetric difference (^)- get elements that are in one set or the other, but not both.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_different_set = set1 ^ set2
print(symmetric_different_set) # Output: {1, 2, 4, 5}

# ✓ Set length and membership
# Using len() (Find the number of elements in a set)

fruits = {"apple", "banana", "cherry"}
print(len(fruits)) # Output: 3

# ✓ Using in (Check if an element exists in a set)

fruits = {"apple", "banana", "cherry"}
if "banana" in fruits:
    print("banana is in the set") # Output: banana is in the set

# ✓ Copying set
# Using copy()

fruits = {"apple", "banana", "cherry"}
copied_fruits = fruits.copy()
print(copied_fruits) # Output: {'banana', 'apple', 'cherry'}

# ✓ Set immutability
# sets themselves are mutable(you can add and remove elements), but the elements inside the set must be
# immutable. for example, you cannot add a list to a set, but you can add tuples because they are immutable.

# Of adding an immutable element (tuple)  to a set

my_set = {(1, 2), (3,4)}
print(my_set) # Output: {(1,2), (3, 4)}

# Example of trying to add a mutable element (list) to a set

# This will raise an error
my_set =  {[1, 2], [3, 4]} # TypeError: Unhashable type: 'list'

# ✓ Dictionary
# A dictionary is a collection of key-value pairs in python. it is unordered, mutable, and indexed by keys.
# Each key in a dictionary is unique. and you can use any immutable data type (like numbers, string, or tuple)
# as keys. values can be of any data type.

# ✓ Creating a dictionary

dict_name = {key1: value1, key2: value2, key3: value3,....}

# ✓ Creating different dictionary
# A dictionary with string keys and integer values

student_ages = {"bro": 20, "bob": 22, "charlie": 21}

# A dictionary with mixed data types
student_info = {"bro": [20, "math"], "Bob": [22, "science"]}

# A dictionary with numeric keys
phone_numbers = {1: "123-4567", 2: "987-6543"}

# ✓ Accessing dictionary values
# You can access a value by referencing its key inside square brackets.

student_ages = {"bro": 20, "bob": 22, "charlie": 21}
print(student_ages["bro"]) # Access value for the key "bro"
# Output: 20

# ✓ Using get() method
# You can also use the get() method to access the value of a key. this method will return None if the key is not found.

print(student_ages.get("bob")) # Access value for the key "bob"
print(student_ages.get("eve")) # key not found. return None
# Output: 22 None

# ✓ Adding and updating key-value pairs
# Add or update using square brackets
# You can add a new key-value pair or update the value of an existing key.

student_ages["David"] = 23 # Add new key-value pair
student_ages["Bro"] = 25 # Update existing key-value pair
print(student_ages) # Output: {'bro': 25, 'Bob': 22 'charlie': 21, 'David': 23}

# ✓ Using update() method
# You can use the update() method to add multiple key-value pairs or update existing ones.

student_ages.update({"Eve": 24, "Bro": 26}) # Add or update multiple key-value pairs
print(student_ages) # Output: {'bro': 26, 'Bob': 22, 'charlie': 21, 'David': 23, 'Eve': 24}

# ✓ Removing key-value pairs
# Using pop() method
# The pop() method removes as specified key and returns its value.if the key is not found, it raises an error.

removed_value = student_ages.pop("Bob") # Removes "Bob" and returns its value
print(removed_value)
print(student_ages)
# Output: 22 {'Bro': 26, 'charlie': 21, 'David': 23, 'Eve': 24}

# ✓ Using popitem() method
# The popitem() method removes and returns last inserted key-value pair in the dictionary.

removed_item = student_ages.popitem() # Removes last key-value pair
print(removed_item)
print(student_ages)
# Output: ('eve', 24)
# {'Bro': 26, 'charlie': 21, 'David': 23}

# ✓ Using del statement
# The del statement can be used to delete a key-value pair by specifying the key

del student_ages["charlie"] # Deletes "charlie"
print(student_ages) # Output: {'alice': 26, 'David': 23}

# ✓ Using clear() method
# The clear() method removes all items from the dictionary.

student_ages.clear()
print(student_ages) # Now the dictionary is empty Output: {}

# ✓ Dictionary methods keys()
# Returns a view object of all keys in the dictionary

student_ages = {"Bro": 26, "Bob": 22}
print(student_ages.keys()) # Returns the keys
# Output: dict_keys(["Bro", "Bob"])

# ✓ Values()
# Returns a view object of all values in  the dictionary
print(student_ages. values()) # Returns the values
# Output: dict_values([26, 22])

# ✓ items()
# Returns a view object of all key-value pairs as tuples.
print(student_ages.items()) # Returns key-value pairs
# Output: dict_items([("Bro", 26), ("Bob", 22)])

# ✓ Nested dictionary
# A dictionary can also contain other dictionary as values, allowing for nested data structures

students = {
    "Bro": {"age": 26, "major": "math"},
    "Bob": {"age": 22, "major": "science"}
}
print(students["Bro"]["major"]) # Accessing nested data
# Output: Math

# ✓ Dictionary Comprehension
# You can crate dictionaries using a comprehension technique similar to list comprehension

# Create a dictionary where the key is a number and the value is its square
squares = {x: x**2 for x in range(5)}
print(squares) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ✓ Dictionary iteration
# You can loop through dictionaries using a for loop.

# Iterating over keys and values

student_ages = {"Bro": 26, "Bob": 22}
for key, value in student_ages.items():
    print(f"{key}: {value}")
# Output: Bro: 26 Bob: 22

# ✓ Indexing
# indexing is a method used to access individual elements of a sequence in python, such as strings, lists, tuples, and
# other iterable types. python supports both positive and negative indexing to retrieve elements.

# ✓  Indexing in strings

my_list = "Hello"
print(my_list[0]) # Access the first character 'H'
print(my_list[4]) # Access the last character 'o'
print(my_list[-1]) # Access the last character 'o'(negative indexing)

# ✓ key points about string indexing
# Positive indexing starts at 0 for the first character, 1 for the seconds, and so on
# Negative indexing starts from -1 for the last character, -2 for the seconds last, and so on.

# ✓ Indexing in lists

my_list = [10, 20, 30, 40, 50]
pirnt(my_list[0]) # Access the first elements: 10
print(my_list[3]) # Access the fourth elements: 40
print(my_list[-1]) # Access the last elements: 50

# ✓ Key points about list indexing
# Positive indexing works just like in strings.
# Negative indexing works the same, starting from the last element.

# ✓ indexing in tuple
# Tuple are similar to list but are immutable. You can access elements in a tuple using the same indexing methods.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1]) # Access the second element: 2
print(my_tuple[-2]) # Access the second last elements: 4

# ✓ key points about tuple indexing:
# Positive indexing and negative indexing work just like lists.
# Tuple are immutable. so their values cannot be changed after creation.

# ✓ Slicing in lists

my_list = [10, 20, 30, 40, 50]
print(my_list[1:4]) # Slice from index 1 to index 3: [20, 30, 40]
print(my_list[:3]) # Slice from the beginning to index 2: [10, 20, 30]
print(my_list[::2]) # slice with step 2: [10, 30, 50]

# ✓ Slicing in strings
my_string =  "Hello, World!"
print(my_string[7:12]) # slice from the start to index 7 to 11: 'World'
print(my_string[:5]) # slice from the start to index 4: 'Hello'
print(my_string[::2]) # slice with step 2: 'Hoo ol!'

# ✓ Indexing and slicing in multi-Dimensional lists
# For lists within lists (also known as 2D lists or matrices), you can use multiple indices to access elements.

# ✓ Indexing and slicing in a 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2]) # Access element in the second row, third column: 6
print(matrix[::2]) # Access every second row: [[1, 2, 3], [7, 8,, 9]]
# Output: [[1, 2, 3], [7, 8, 9]]

# ✓ Nested indexing in tuples
# if you have nested tuples (tuples within tuples), you can access the inner elements using indexing.

# ✓ Nested indexing in tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1][0]) # Access element 3 from the second tuple: 3

# ✓ indexing with conditions
# You can combine indexing and conditions to filter or find specific values in lists,strings , or tuples.

# ✓ Indexing with conditions
my_list = [10, 15, 20, 25, 30]
# Find all values greater than 20
filtered_values = [value for value in my_list if value > 20]
print(filtered_values) # Output: [25, 30]

# ✓ Function
# A function in python is a block of reusable code that performs a specific task. Functions allow you to group
# code into one unit, so you can call it when needed without rewriting the same code multiple times.

# ✓ Defining a Function
# To define a function, use the def keyword, followed by the function name, parentheses () (which may include parameters)
# an a colon :. The code inside the function is indented.

def function_name(parameters):
    # Function body
    # code to execute
    return result # Optional

# ✓ Simple function
def greet():
    print("Hello, welcome to python!")
greet() # Calling the function

# ✓ Function parameters
# Functions can accept parameters (also called arguments), which are values you pass to the function when calling it.
# These parameters can used inside the function

def greet(name):
    print(f"Hello, {name}!")
greet("Bro") # Passing an argument "Bro"
# Output: Hello, Bro

# ✓ Return statement
# A function can return a value using the return keyword. This allows you to pass data back to the caller when
# The function is done.

def add(a, b):
    return a + b
result = add(3, 5) # Calling the function and storing the result
print(result) # Output: the returned value
# Output: 8
# Note: if a function does not include a return statement, it returns None by default.

# ✓ Function with multiple parameters
# You can pass multiple parameters to a function, separated by commas.

# Function with multiple parameters
def multiply(x, y):
    return x * y
result = multiply(4, 5)
print(result) # Output: 20

# ✓ Default parameters
# You can assign default values to parameters. These values will be used if the caller does not provide a
# value for those parameters.

# ✓ Function with default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet("Bro") # Uses the passed argument
greet() # uses the default value "Guest"
# Output: Hello, Bro Hello, Guest!

# ✓ Keyword arguments
# You can pass arguments to a function call. This is useful when a function has many parameters.
# And you want to make the call more readable.

# ✓ Keyword arguments
def describe_person(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")
describe_person(age=21, city="Japan", name="Bro")
# Output: Name: Bro, Age: 21, City: Japan

# ✓ Variable Number of arguments
# You can use *args to allow a function to accept a variable number of positional arguments, and **kwargs
# to accept a variable number of keyword arguments.

# ✓ Function with *args
def print_number(*args):
    for num in args:
        print(num)
print_number(1, 2, 3, 4) # Passing multiple arguments Output: 1 2, 3, 4

# ✓ Function with **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Bro", age=21, city="New york")
# Output: name: Bro, age: 25, city: New york


# ✓ Function scope
# Local variable: Variables defined inside a function are local to that function and cannot be accessed outside it.
# Global variable: Variables defined outside any function can be accessed inside functions, but if you modify them inside
# function, you need to use the global keyword

# ✓ Local and global variable
x = 10 # Global variable
def func():
    x = 5 # Local variable
    print("Inside function:", x)
func()
print("Outside function:", x)
# Output: inside function: 5
# Output: Outside function: 10

# ✓ Using global variables inside functions
x = 10 # global variable
def func():
    global x
    x = 5 # Modifying the global variable
    print("Inside function:", x)
func()
print("Outside function:", x)
# Output: Inside function: 5
# Output: Outside function: 5

# ✓ Lambda functions (anonymous functions)
# A lambda function is a small anonymous function that can have any number of arguments, but only one
# Expression. it's typically used for short_term operations.

# lambda arguments: expression

# ✓ Lambda function
add = lambda a, b: a + b
result = add(3, 5)
print(result) # Output: 8

# ✓ Use of lambda with map()
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared) # Output: [1, 4, 9, 16]

# ✓ Recursive function
# A recursive function is a function that calls itself. it is typically used to solve problems that can be broken
# down into smaller subproblems.

# ✓ Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
print(result) # Output: 120

# Important: A base case (condition to stop recursion) is essential to prevent infinite recursion

# ✓ Function Documentation (Docstrings)
# Python allows you to documents your function using docstrings. THese are written inside triple quotes and describe the
# function's purpose, arguments, and return value.

# Function with docstring
def greet(name):
    """
    This function greets the person passed in as a parameter.
    parameters:
    name(str): The name of the person to greet.
    Returns:
    None
    """
    print(f"Hello, {name}!")
greet("Bro")

# ✓  str.format()
# The str.format() method in python is used for string formatting. it allows you to insert placeholders in a string
# and replace them with values dynamically


# ✓  Basic syntax of str.format()
# The basic syntax involves using curly braces {} as placeholders within a string. You can then use the format()
# method to insert values into those placeholders.
"Your string with placeholders {}".format(value)

# ✓ Basic string formatting
name = "bro"
greeting = "Hello, {}".format(greeting)
print(greeting) # Output: Hello, bro
# Here, {} is replaced with the value of the name variable.

# ✓ Multiple placeholders
# You can have multiple placeholders in a string and use format() to replace all of them

# ✓ Multiple placeholders
name = "Bob"
age = 21
sentence = "My name is {} and I am {} years old.".format(name, age)
print(sentence) # Output: My name is Bob and I am 21 years old.
# Explanation
# The first {} is replaced by the value of name.
# The second {} is replaced by the value of age.

# ✓ Positional arguments
# You can specify the order of the arguments explicitly by using indices inside the curly braces.

# ✓ Syntax with positional arguments:
"{} is {} years old.".format(name, age)

# ✓ Using positional arguments
name = "Charlie"
age = 21
sentence = "{} is {} years old.".format(name, age)
print(sentence) # Output: Charlie is 21 years old.
# Explanation
# The format() method places the first argument (name) in the first placeholder and the second argument(age)
# in the second placeholder.

# ✓ Named arguments
# You can also pass arguments by name and reference them by name inside the string
# ✓ Syntax with named arguments:
"Hello, {name}. You are {age} years old.".format(name="Eve", age=40)

# ✓ Using named arguments:
name = "David"
age = 25
sentence = "Hello, {name}. You are {age} years old.".format(name=name, age=age)
print(sentence) # Output: Hello David. You are 25 years old

# Explanation
# The placeholders {name} and {age} are replaced with the values of the corresponding named arguments.

# ✓ Reordering arguments
# You can use the positional index inside the {} to reorder the values.
# ✓ Syntax with reordering
"{1} is {0}'s friend.".format("Bro","Bob")

# ✓ Reordering arguments
sentence = "{1} is {0}'s friend.".format("Bro","Bob")
print(sentence) # Output: Bob is Bro's
# Explanation
# {1} is replaced by the second argument(Bob), and {0} is replaced by the first argument (Bro)

# ✓ Formatting numbers
# You can format numbers in different ways, such as setting the decimal places, adding commas for thousands, etc.

# ✓ Formatting numbers
pi = 3.14159265359
formatted = "The value of pi is {:.2f}.".format(pi)
print(formatted) # Output: The value of pi is 3.14
# :.2f tells python to format the number with 2 decimal places.

# ✓ Padding and alignment
# You can pad strings to make them a specific length and align them(left, right,or center)
# ✓ Syntax with padding and alignment:
"{:<10}".format("Left") # Left-align with a width of 10
"{:>10}".format("Right") # Right-align with a width of 10
"{:^10}".format("Center") # Center-align with a width of 10

Example: Padding and Alignment

left = "{:<10}".format("Left")
right = "{:>10}".format("Right")
center = "{:^10}".format("Center")
print(left)
print(right)
print(center)

# Output:
#
# Left
#      Right
#   Center


# Formatting with Percentages
# You can format numbers as percentages using format().
# Example: Formatting Percentages

percentage = 0.4567
formatted = "The percentage is {:.2%}".format(percentage)
print(formatted)
# Output: The percentage is 45.67%
# Explanation:
# :.2% tells Python to format the number as a percentage with 2 decimal places.

# Using format() with Dictionaries
# You can pass a dictionary to str.format() and reference the dictionary keys inside the string.
# Example: Using Dictionaries with format()

person = {"name": "John", "age": 28}
sentence = "Name: {name}, Age: {age}".format(**person)
print(sentence)# Output: Name: John, Age: 28
# Explanation:
# **person unpacks the dictionary and passes its keys and values as named arguments to the format() method.

# Escaping Curly Braces
# If you need to include literal curly braces { or } in your string, you can escape them by doubling them.
# Example: Escaping Curly Braces
sentence = "This is how you escape curly braces: {{ and }}."
print(sentence)# Output: This is how you escape curly braces: { and }.

# Python Exception Handling
# Exception handling in Python is a mechanism to handle errors gracefully without crashing the program. It allows the program to continue executing even after an error occurs, providing a way to deal with unexpected conditions.
# What is an Exception?
# An exception is an event that disrupts the normal flow of a program. When an error occurs, Python raises an exception, and you can handle it to prevent the program from terminating abruptly.

# Basic Syntax of Exception Handling
# In Python, the basic structure for handling exceptions involves using try, except, else, and finally blocks.
# Syntax:
#try:
    # Code that may cause an exception
#except ExceptionType:
    # Code to handle the exception
#else:
    # Code that runs if no exception occurs
#finally:
    # Code that runs no matter what (optional)

# try Block
# The try block contains code that might raise an exception. If no exception occurs, the code in the try block is executed normally. If an exception occurs, Python jumps to the except block.
#Example: try Block
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")

# except Block
# The except block handles exceptions. If an error occurs in the try block, the code in the except block is executed. You can specify different types of exceptions to handle different errors.
#Example: except Block
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
# Explanation:
# If the user enters a non-numeric input, a ValueError is raised, and the program prints a custom error message.

# Catching Multiple Exceptions
# You can catch multiple exceptions by using multiple except blocks or a single except block that handles several types of exceptions.

# Example: Catching Multiple Exceptions
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result is {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Error! Cannot divide by zero.")

# Explanation:
# The program catches two exceptions: ValueError (if the input is not a number) and ZeroDivisionError (if the user tries to divide by zero).

# else Block
# The else block is executed if no exception occurs in the try block. It's an optional block that can be used to perform actions that should happen when everything goes as planned.
# Example: else Block
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 + num2
except ValueError:
    print("Invalid input! Please enter valid numbers.")
else:
    print(f"The sum of the numbers is: {result}")
# Explanation:
# If no exception occurs, the sum of the two numbers is displayed.

# finally Block
# The finally block is executed no matter what, whether an exception is raised or not. This block is often used for clean-up actions, such as closing files or releasing resources.
# Example: finally Block
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print(content)
finally:
    print("This block is always executed.")
    file.close()  # Closing the file, even if an error occurs
# Explanation:
# The finally block ensures that the file is always closed, whether or not an exception occurs.

# Catching All Exceptions
# If you don't know which exception will be raised, you can catch all exceptions using a generic except block. However, it’s recommended to catch specific exceptions to avoid hiding bugs.
# Example: Catching All Exceptions
try:
    value = 10 / 0
except:
    print("An error occurred!")
# Explanation:
# This catches any exception that might occur, but it doesn’t specify the type of exception.

# Using raise to Raise Exceptions
# You can explicitly raise exceptions in your code using the raise keyword. This is useful when you want to signal an error or enforce certain conditions.
# Example: Using raise
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    else:
        print(f"Your age is {age}.")

try:
    check_age(-5)
except ValueError as e:
    print(e)
# Explanation:
# The check_age() function raises a ValueError if the age is negative.

# Custom Exception Handling
# You can create your own exception classes by subclassing the built-in Exception class. This allows you to define specific error conditions for your application.
# Example: Custom Exception
class NegativeAgeError(Exception):
    def _init_(self, message="Age cannot be negative"):
        self.message = message
        super().__init__(self.message)
def check_age(age):
    if age < 0:
        raise NegativeAgeError
    print(f"Your age is {age}")

try:
    check_age(-2)
except NegativeAgeError as e:
    print(e)
# Explanation:
# The NegativeAgeError is a custom exception that is raised when the age is negative.

# Python File Detection
# File detection in Python is used to check if a file or directory exists before performing operations like reading or writing. This helps prevent errors such as FileNotFoundError.

# Importing the os and pathlib Modules
# Python provides two modules for file detection: os module (older, widely used)
# pathlib module (modern, preferred in newer Python versions)

import os
from pathlib import Path

# Checking if a File Exists
# Using os.path.exists()
# The os.path.exists() function checks if a file or directory exists.

import os
file_path = "example.txt"
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")
# Explanation:
# If example.txt exists, it prints "File exists."
# If not, it prints "File does not exist."
# Using Path.exists() (Recommended)
# The Path.exists() method from the pathlib module works similarly but is more modern and object-oriented.

from pathlib import Path
file_path = Path("example.txt")

if file_path.exists():
    print("File exists.")
else:
    print("File does not exist.")
# Explanation:
# Path("example.txt") creates a file path object.
# exists() checks if the file exists.

# Checking if a Path is a File or Directory
# Sometimes, you may want to check if a path points to a file or a directory.
# Using os.path.isfile() and os.path.isdir()
# os.path.isfile() → Checks if the path is a file.
# os.path.isdir() → Checks if the path is a directory.

import os
path = "example.txt"

if os.path.isfile(path):
    print("It is a file.")
elif os.path.isdir(path):
    print("It is a directory.")
else:
    print("Path does not exist.")

# Using Path.is_file() and Path.is_dir()
# The pathlib module provides similar functions:
# Path.is_file() → Checks if the path is a file.
# Path.is_dir() → Checks if the path is a directory.

from pathlib import Path
path = Path("example.txt")

if path.is_file():
    print("It is a file.")
elif path.is_dir():
    print("It is a directory.")
else:
    print("Path does not exist.")

# Checking if a File is Readable or Writable
# Using os.access()
# The os.access() function checks file permissions:
# os.R_OK → Read permission
# os.W_OK → Write permission

import os
file_path = "example.txt"

if os.access(file_path, os.R_OK):
    print("File is readable.")
else:
    print("File is not readable.")

if os.access(file_path, os.W_OK):
    print("File is writable.")
else:
    print("File is not writable.")

# Explanation:
# This checks if the file can be read or written.

# Checking the File Size
# Using os.path.getsize()
# You can check if a file exists and is not empty by checking its size.

import os

file_path = "example.txt"

if os.path.exists(file_path):
    size = os.path.getsize(file_path)
    if size > 0:
        print(f"File exists and its size is {size} bytes.")
    else:
        print("File is empty.")
else:
    print("File does not exist.")

# Finding All Files in a Directory
# Using os.listdir()
# To list all files in a directory:

import os

directory = "."

files = os.listdir(directory)
print("Files in directory:", files)

# Using Path.glob()
# To list files using pathlib:

from pathlib import Path

directory = Path(".")

files = list(directory.glob("*"))  # Lists all files and folders
print("Files in directory:", files)

# Checking File Extension
# Using os.path.splitext()
# This method extracts the file extension.

import os

file_path = "example.txt"

extension = os.path.splitext(file_path)
print("File extension:", extension)

# Using Path.suffix
# With pathlib, you can use .suffix:

from pathlib import Path
file_path = Path("example.txt")
print("File extension:", file_path.suffix)

# Python Inheritance
# Inheritance is a feature in Object-Oriented Programming (OOP) that allows a class to inherit properties and methods from another class. This helps in code reuse and organization.
# What is Inheritance?
# Inheritance allows a child class (subclass) to acquire properties and behaviors from a parent class (superclass).
# Key Benefits:
# Code reusability
# Establishes a relationship between classes
# Enables extensibility and modularity

# Basic Inheritance Syntax
class Parent:  # Parent Class
    def show(self):
        print("This is the Parent class.")

class Child(Parent):  # Child Class inheriting from Parent
    pass

obj = Child()  # Creating an object of the Child class
obj.show()  # Inherited method from Parent

# Output: This is the Parent class.

# Explanation:
# Parent is the superclass.
# Child is the subclass that inherits the show() method from Parent.

# Overriding Methods in Child Class
# A child class can override a method from the parent class.
class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):  # Overriding the method
        print("This is the Child class.")

obj = Child()
obj.show()  # Calls the overridden method

# Output: This is the Child class.

#Explanation:
# Child overrides the show() method of Parent.
# When show() is called, the method in the Child class is executed.

# Using super() to Call Parent Methods
# The super() function allows a child class to call a method from the parent class.
class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):
        super().show()  # Calling parent method
        print("This is the Child class.")

obj = Child()
obj.show()

# Output: This is the Parent class. This is the Child class.
# Explanation:
# super().show() calls show() from the Parent class.
# Then, show() in the Child class is executed.

# Inheriting the _init_() Constructor
# The _init_() constructor of a parent class can be inherited and extended in a child class.
class Parent:
    def _init_(self, name):
        self.name = name
        print(f"Parent constructor: {self.name}")

class Child(Parent):
    def _init_(self, name, age):
        super()._init_(name)  # Calling Parent constructor
        self.age = age
        print(f"Child constructor: {self.name}, Age: {self.age}")

obj = Child("John", 25)

# Output: Parent constructor: John Child constructor: John, Age: 25
# Explanation:
# super()._init_(name) calls the parent's constructor.
# Child class adds an extra attribute age.

#  Types of Inheritance in Python
# Single Inheritance
# A single child class inherits from a single parent class.
class Parent:
    def show(self):
        print("Parent class.")

class Child(Parent):
    pass

obj = Child()
obj.show()

# Multilevel Inheritance
# A child class inherits from another child class (a chain of inheritance).
class GrandParent:
    def show1(self):
        print("Grandparent class.")

class Parent(GrandParent):
    def show2(self):
        print("Parent class.")

class Child(Parent):
    def show3(self):
        print("Child class.")

obj = Child()
obj.show1()  # Grandparent method
obj.show2()  # Parent method
obj.show3()  # Child method

# Output: Grandparent class. Parent class. Child class.

# Multiple Inheritance
# A child class inherits from multiple parent classes.
class Parent1:
    def show1(self):
        print("Parent1 class.")

class Parent2:
    def show2(self):
        print("Parent2 class.")

class Child(Parent1, Parent2):
    pass

obj = Child()
obj.show1()
obj.show2()

# Output: Parent1 class. Parent2 class.
# Explanation:
# Child inherits from both Parent1 and Parent2.

# Hierarchical Inheritance
# Multiple child classes inherit from the same parent class.
class Parent:
    def show(self):
        print("Parent class.")
class Child1(Parent):
    pass
class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

obj1.show()
obj2.show()

# Output: Parent class. Parent class.
# Explanation:
# Both Child1 and Child2 inherit show() from Parent.

# Hybrid Inheritance
# Combination of multiple inheritance types.
class A:
    def showA(self):
        print("Class A")
class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):
    def showD(self):
        print("Class D")

obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()

# Output: Class A Class B Class C Class D

# Python Method Chaining
# Method Chaining is a technique in Python where multiple methods are called on the same object in a single line. Each method returns the object itself, allowing further method calls.

# 1. Basic Method Chaining
# Let's look at a normal method call vs. method chaining.
# Without Method Chaining:
class Demo:
    def method1(self):
        print("Method 1 executed")
        return self  # Returning the object

    def method2(self):
        print("Method 2 executed")
        return self  # Returning the object

obj = Demo()
obj.method1()
obj.method2()

# With Method Chaining:

class Demo:
    def method1(self):
        print("Method 1 executed")
        return self  # Returning the object

    def method2(self):
        print("Method 2 executed")
        return self  # Returning the object

obj = Demo()
obj.method1().method2()  # Chaining methods

# Output: Method 1 executed Method 2 executed
# Explanation:
# Each method returns self, allowing the next method to be called in the same line.
# This makes the code more compact and readable.

# 2. Implementing Method Chaining with Parameters
# We can pass parameters in method chaining.
class Calculator:
    def _init_(self):
        self.value = 0

    def add(self, num):
        self.value += num
        return self  # Returning self

    def multiply(self, num):
        self.value *= num
        return self  # Returning self

    def show(self):
        print(f"Result: {self.value}")
        return self  # Returning self to continue chaining

calc = Calculator()
calc.add(5).multiply(3).show()
# Output: Result: 15
# Explanation:
# add(5) adds 5 to value (0 → 5).
# multiply(3) multiplies value by 3 (5 × 3 = 15).
# show() prints the final result.

# 3. Chaining String Methods
# Python built-in string methods support method chaining.

text = "  hello world!  "
result = text.strip().upper().replace("WORLD", "PYTHON")
print(result)

# Output: HELLO PYTHON!
# Explanation:
# .strip() removes spaces → "hello world!"
# .upper() converts to uppercase → "HELLO WORLD!"
# .replace("WORLD", "PYTHON") replaces "WORLD" with "PYTHON"

# 4. Method Chaining in Classes with Multiple Methods
class Person:
    def _init_(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")
        return self

    def say_age(self, age):
        print(f"I am {age} years old.")
        return self

    def farewell(self):
        print("Goodbye!")
        return self

person = Person("Alice")
person.greet().say_age(25).farewell()

# Output: Hello, Alice! I am 25 years old. Goodbye!
# Explanation:
# greet() prints "Hello, Alice!".
# say_age(25) prints "I am 25 years old.".
# farewell() prints "Goodbye!".

# 5. Chaining File Operations
# Python file objects support method chaining.
with open("example.txt", "w") as file:
    file.write("Hello, World!").upper()

# ⚠ Note: Not all file operations support chaining. write() does not return the file object, so chaining with .upper() won't work.

# Python super() Function
# The super() function in Python is used in inheritance to call methods from the parent class inside the child class.
# 1. Why Use super()?
# ✔ Access Parent Class Methods
# ✔ Avoid Code Duplication
# ✔ Make Code Maintainable
# ✔ Work with Multiple Inheritance

# 2. Basic Usage of super()
# Example Without super()
class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):
        print("This is the Child class.")
        Parent.show(self)  # Calling Parent method manually

obj = Child()
obj.show()

# Output: This is the Child class. This is the Parent class.
# Problem:
# We manually call Parent.show(self), which is not recommended.
# This makes code hard to maintain if the parent class changes.

# Example Using super()
class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):
        print("This is the Child class.")
        super().show()  # Calling Parent method using super()

obj = Child()
obj.show()
# Output: This is the Child class. This is the Parent class.
# Advantages of super()
# ✔ No need to mention Parent explicitly.
# ✔ Works correctly even if class names change.
# ✔ Useful in multiple inheritance.

# 3. Using super() with _init_() (Constructor)
# When a child class needs to extend the _init_() of the parent class, we use super().
class Parent:
    def _init_(self, name):
        self.name = name
        print(f"Parent Constructor: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super()._init(name)  # Calls Parent __init_()
        self.age = age
        print(f"Child Constructor: {self.name}, Age: {self.age}")

obj = Child("John", 25)
# Output: Parent Constructor: John Child Constructor: John, Age: 25
# Explanation:
# super()._init_(name) calls Parent's constructor first.
# Then, Child's constructor executes.

# 4. Using super() in Multilevel Inheritance
class GrandParent:
    def show(self):
        print("This is the GrandParent class.")

class Parent(GrandParent):
    def show(self):
        print("This is the Parent class.")
        super().show()  # Calls GrandParent's method
class Child(Parent):
    def show(self):
        print("This is the Child class.")
        super().show()  # Calls Parent's method

obj = Child()
obj.show()
# Output: This is the Child class. This is the Parent class. This is the GrandParent class.
# Explanation:
# Child.show() calls super().show(), which executes Parent.show().
# Parent.show() calls super().show(), which executes GrandParent.show().
# The chain continues from Child → Parent → GrandParent.

# 5. Using super() in Multiple Inheritance
class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):  # Multiple Inheritance
    def show(self):
        print("Class C")
        super().show()  # Calls the next class in the order (A)

obj = C()
obj.show()
# Output: Class C Class A
# Explanation:
# super().show() calls A.show(), because the method resolution order (MRO) prioritizes A over B.

# 6. super() with Multiple Methods
class Parent:
    def method1(self):
        print("Method 1 from Parent")

    def method2(self):
        print("Method 2 from Parent")
class Child(Parent):
    def method1(self):
        print("Method 1 from Child")
        super().method1()  # Calls Parent's method1()
        super().method2()  # Calls Parent's method2()

obj = Child()
obj.method1()
# Output:
# Method 1 from Child
# Method 1 from Parent
# Method 2 from Parent

# 7. How super() Works Internally (MRO - Method Resolution Order)
# When multiple classes are inherited, Python follows MRO (Method Resolution Order) to determine which method super() should call.
# To check MRO of a class:
print(Child.__mro__)  # Shows method resolution order
# Example
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)

# Output: (<class '_main.D'>, <class 'main.B'>, <class 'main.C'>, <class 'main_.A'>, <class 'object'>)
# Explanation:
# Python first looks in D, then B, then C, then A, and finally object.

# Python Abstract Class
# In Python, an abstract class is a class that cannot be instantiated and is meant to be inherited by other classes. It contains abstract methods, which must be implemented in the child class.
# We use the ABC (Abstract Base Class) module from the abc library to create abstract classes.

# 1. Why Use Abstract Classes?
# ✔ Ensures Method Implementation – Forces child classes to implement required methods.
# ✔ Provides a Blueprint – Defines a common structure for all subclasses.
# ✔ Avoids Instantiating Incomplete Classes – Prevents creating objects of the parent class.

# 2. Creating an Abstract Class
# We use ABC and @abstractmethod to define abstract classes.
from abc import ABC, abstractmethod  # Import ABC module
class Animal(ABC):  # Abstract class
    @abstractmethod
    def make_sound(self):  # Abstract method
        pass  # No implementation

# obj = Animal()  # ❌ ERROR: Abstract classes cannot be instantiated

# Explanation:
# ABC makes Animal an abstract class.
# @abstractmethod means all subclasses must define make_sound().

# 3. Implementing an Abstract Class
# Child classes must override abstract methods.
class Dog(Animal):  # Inheriting from Animal
    def make_sound(self):  # Implementing abstract method
        print("Woof! Woof!")

class Cat(Animal):  # Another subclass
    def make_sound(self):
        print("Meow! Meow!")

dog = Dog()
dog.make_sound()  # Output: Woof! Woof!

cat = Cat()
cat.make_sound()  # Output: Meow! Meow!

# Explanation:
# Dog and Cat inherit Animal. Each subclass implements make_sound().If a subclass does not implement make_sound(), Python throws an error.

# 4. Abstract Class with a Constructor (_init_())
class Vehicle(ABC):
    def _init_(self, brand):
        self.brand = brand  # Concrete attribute

    @abstractmethod
    def start(self):  # Abstract method
        pass

class Car(Vehicle):
    def start(self):
        print(f"{self.brand} car is starting...")

car = Car("Toyota")
car.start()

# Output: Toyota car is starting...
# Explanation:
# Vehicle has an _init_() constructor.
# Car calls the parent _init_() using super().
# start() must be implemented in Car.

# 5. Abstract Class with Multiple Abstract Methods
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)
print("Area:", circle.area())         # Output: Area: 78.5
print("Perimeter:", circle.perimeter())  # Output: Perimeter: 31.4

# 6. Abstract Class with Both Abstract and Concrete Methods
# Abstract classes can have both abstract and normal (concrete) methods.
class Device(ABC):
    def power_on(self):  # Concrete method
        print("Device is turning on...")

    @abstractmethod
    def operate(self):  # Abstract method
        pass

class Computer(Device):
    def operate(self):
        print("Computer is running software.")

comp = Computer()
comp.power_on()  # Output: Device is turning on...
comp.operate()   # Output: Computer is running software.

# 7. Abstract Class with Class Method (@classmethod)
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

    @classmethod
    def company_info(cls):
        print("This is XYZ company.")

class Manager(Employee):
    def work(self):
        print("Managing the team.")

mgr = Manager()
mgr.work()         # Output: Managing the team.
mgr.company_info() # Output: This is XYZ company.

# 8. Checking if a Class is a Subclass of an Abstract Class
# To check if a class is a subclass of an abstract class:

print(issubclass(Car, Vehicle))  # Output: True
print(issubclass(Dog, Animal))   # Output: True

# To check if an object is an instance of a class:
print(isinstance(car, Vehicle))  # Output: True
print(isinstance(dog, Animal))   # Output: True

# 9. Creating an Abstract Property (@property)
class Product(ABC):
    @property
    @abstractmethod
    def price(self):
        pass

class Laptop(Product):
    def _init_(self, cost):
        self._price = cost

    @property
    def price(self):
        return self._price

laptop = Laptop(1000)
print("Laptop Price:", laptop.price)  # Output: Laptop Price: 1000


# Python - Passing Objects as Arguments
# In Python, we can pass objects as arguments to functions and methods. This allows us to work with objects dynamically inside functions.
# 1. Why Pass Objects as Arguments?
# ✔ Encapsulation – Functions can operate on objects without modifying them directly.
# ✔ Reusability – We can use the same function with different objects.
# ✔ Flexibility – Functions can handle multiple object types.

# 2. Passing an Object to a Function
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

def show_info(obj):  # Function accepting an object
    print(f"Name: {obj.name}, Age: {obj.age}")

p1 = Person("Bro", 25)
show_info(p1)  # Passing object to function
# Output: Name: Bro, Age: 25
# Explanation:
# The show_info() function accepts an object (obj).
# It accesses attributes name and age of the Person object.

# 3. Passing an Object to a Method in Another Class
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

class Showroom:
    def display(self, car_obj):  # Accepting object as argument
        print(f"Car Brand: {car_obj.brand}, Model: {car_obj.model}")

car1 = Car("Toyota", "Corolla")
shop = Showroom()
shop.display(car1)  # Passing object to method
# Output: Car Brand: Toyota, Model: Corolla

# Explanation:
# display() in Showroom accepts a Car object and prints its attributes.
# We pass car1 to display().

# 4. Modifying an Object Inside a Function
# We can modify an object's attributes inside a function.
class Student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks

def update_marks(student_obj, new_marks):
    student_obj.marks = new_marks  # Modifying object attribute
    print(f"{student_obj.name}'s updated marks: {student_obj.marks}")

s1 = Student("John", 85)
update_marks(s1, 95)  # Passing object to function

# Output: John's updated marks: 95
# Explanation:
# The function update_marks() changes marks of s1.
# The object s1 is modified globally since objects are mutable.

# 5. Returning an Object from a Function
# Functions can return objects as results.
class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

def create_employee(name, salary):
    return Employee(name, salary)  # Returning object

emp1 = create_employee("Michael", 5000)
print(f"Employee: {emp1.name}, Salary: {emp1.salary}")
# Output: Employee: Michael, Salary: 5000
# Explanation:
# The function create_employee() creates and returns an object.
# We store the returned object in emp1 and access its attributes.

# 6. Passing an Object List to a Function
# We can pass a list of objects to a function.
class Product:
    def _init_(self, name, price):
        self.name = name
        self.price = price

def show_products(product_list):
    for product in product_list:  # Looping through objects
        print(f"Product: {product.name}, Price: {product.price}")

p1 = Product("Laptop", 800)
p2 = Product("Phone", 500)

products = [p1, p2]  # List of objects
show_products(products)  # Passing list of objects
# Output: Product: Laptop, Price: 800 Product: Phone, Price: 500

# 7. Using Objects Inside Another Class
# One class can accept an object of another class.
class Engine:
    def _init_(self, horsepower):
        self.horsepower = horsepower

class Car:
    def _init_(self, brand, engine_obj):
        self.brand = brand
        self.engine = engine_obj  # Object as an attribute

    def show_details(self):
        print(f"Car Brand: {self.brand}, Engine HP: {self.engine.horsepower}")

engine1 = Engine(150)
car1 = Car("Honda", engine1)  # Passing object as argument
car1.show_details()
# Output: Car Brand: Honda, Engine HP: 150

# Explanation:
# Engine object engine1 is passed to Car.
# Car accesses engine.horsepower.

# Python Walrus Operator (:=)
# The walrus operator (:=) in Python allows you to assign a value to a variable inside an expression. It was introduced in Python 3.8 and is also known as the assignment expression.
# 1. Why Use the Walrus Operator?
# ✔ Reduces Redundant Code – Avoids writing the same expression twice.
# ✔ Improves Readability – Makes the code more concise.
# ✔ Works in Loops, Conditions, and List Comprehensions.

# 2. Basic Syntax of Walrus Operator
x = 10
print(x)  # Normal assignment

print(y := 20)  # Using walrus operator

# Output: 20

# Explanation:
# y := 20 assigns 20 to y and immediately returns y.

# 3. Using Walrus Operator in while Loops
# Without the walrus operator:
number = input("Enter a number: ")
while number != "0":
    print(f"You entered: {number}")
    number = input("Enter a number: ")  # Repeating input()

# With the walrus operator:
while (number := input("Enter a number: ")) != "0":
    print(f"You entered: {number}")

# Advantages:
# ✔ Removes duplicate input() calls.
# ✔ Makes the loop condition and assignment more compact.

# 4. Using Walrus Operator in if Statements
# Without the walrus operator:
name = input("Enter your name: ")
if len(name) > 5:
    print(f"Your name '{name}' is long.")

# With the walrus operator:
if (name := input("Enter your name: ")) and len(name) > 5:
    print(f"Your name '{name}' is long.")

# Advantages:
# ✔ Reduces the need for a separate variable declaration.
# ✔ Makes the condition cleaner.

# 5. Using Walrus Operator in List Comprehensions
# Without the walrus operator:
numbers = [2, 4, 6, 8, 10]
squares = [n*2 for n in numbers if n*2 > 20]
print(squares)

# With the walrus operator:
numbers = [2, 4, 6, 8, 10]
squares = [sq for n in numbers if (sq := n**2) > 20]
print(squares)

# Output: [36, 64, 100]

# Advantages:
# ✔ Saves extra computation by calculating n**2 once.
# ✔ Improves efficiency in list comprehensions.

# 6. Using Walrus Operator in for Loops
# Without the walrus operator:
words = ["apple", "banana", "cherry"]
lengths = {}
for word in words:
    lengths[word] = len(word)
print(lengths)

# With the walrus operator:
words = ["apple", "banana", "cherry"]
lengths = {word: (length := len(word)) for word in words}
print(lengths)

# Output: {'apple': 5, 'banana': 6, 'cherry': 6}

# Advantages:
# ✔ Eliminates the need for a separate loop.
# ✔ Stores word lengths directly inside a dictionary.

# 7. Using Walrus Operator in Function Calls
# Without the walrus operator:
def square(n):
    return n * n

num = 5
result = square(num)
if result > 10:
    print(f"Square of {num} is {result}, which is greater than 10.")

# With the walrus operator:
def square(n):
    return n * n

if (result := square(5)) > 10:
    print(f"Square is {result}, which is greater than 10.")

# Output: Square is 25, which is greater than 10.

# Advantages:
# ✔ Eliminates the need for an extra variable (result).
# ✔ Shortens function calls inside conditions.

# Python Higher-Order Functions
# A higher-order function is a function that takes another function as an argument or returns a function.

# 1. Why Use Higher-Order Functions?
# ✔ Code Reusability – Write reusable functions instead of repeating code.
# ✔ Flexibility – Functions can be passed and modified dynamically.
# ✔ Clean Code – Removes unnecessary loops and conditions.

# 2. Higher-Order Function Taking Another Function as an Argument
# A function can take another function as an argument.

# Example 1: Function Passed as an Argument
def greet(name):
    return f"Hello, {name}!"

def process_function(func, value):
    return func(value)  # Calling the passed function

print(process_function(greet, "Alice"))  # Passing 'greet' function

# Output: Hello, Alice!

# Explanation:
# process_function() accepts a function (func) and a value (value).
# It calls func(value), which is greet("Alice").

# 3. Using Built-in Higher-Order Functions (map, filter, reduce)
# Python has built-in higher-order functions that work with other functions.

# Example 2: map() – Apply a Function to Each Item in a List
def square(n):
    return n * n

numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))  # Applying 'square' function to each item

print(squared_numbers)

# Output: [1, 4, 9, 16]

# ✔ map() applies square to each number in the list.
# ✔ Returns an iterator, so we use list() to get the final result.

# Example 3: filter() – Select Elements Based on a Condition
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))  # Keeping only even numbers

print(even_numbers)
# Output: [2, 4, 6]
# ✔ filter() keeps only elements where is_even(n) returns True.

# Example 4: reduce() – Cumulative Computation
from functools import reduce
def add(a, b):
    return a + b

numbers = [1, 2, 3, 4]
sum_result = reduce(add, numbers)  # Summing up numbers

print(sum_result)
# Output: 10

# ✔ reduce() applies add() to elements cumulatively: (((1+2)+3)+4) = 10.

# 4. Higher-Order Function Returning Another Function
# A function can return another function dynamically.
# Example 5: Function Returning Another Function
def multiplier(n):
    def multiply(x):
        return x * n  # Uses 'n' from outer function
    return multiply  # Returns the inner function

times3 = multiplier(3)  # times3 is now a function that multiplies by 3
print(times3(5))  # 5 * 3 = 15

# Output: 15

# Explanation:
# multiplier(n) returns a function (multiply(x)).
# times3 = multiplier(3) means times3(x) = x * 3.

# 5. Using lambda with Higher-Order Functions
# lambda functions make higher-order functions more concise.

# Example 6: Using lambda in map()
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

# Output: [1, 4, 9, 16]

# ✔ No need to define a separate square() function!

# Example 7: Using lambda in filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Output: [2, 4, 6]

# ✔ The condition is directly inside filter().

# Python Lambda Function
# A lambda function is a small, anonymous function (a function without a name). It is used when you need a short function for a short period.

# 1. Why Use Lambda Functions?
# ✔ Short and Simple – Used for one-liner functions.
# ✔ No Need for def – Can be defined in a single line.
# ✔ Used Inside Other Functions – Works well with map(), filter(), and reduce().

# 2. Basic Syntax of a Lambda Function
# lambda arguments: expression
# ✔ No def keyword
# ✔ Single expression only
# ✔ Returns the result automatically

# 3. Basic Example of a Lambda Function
# Without a lambda function:
def square(n):
    return n * n

print(square(5))  # Output: 25

# With a lambda function:
square = lambda n: n * n
print(square(5))  # Output: 25

# ✔ Both do the same thing, but lambda makes it shorter!
# 4. Using Lambda Function with Multiple Arguments
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10

# ✔ Works like a normal function but is inline.

# 5. Using Lambda Inside Another Function
# Lambda functions are useful inside other functions.
def multiplier(n):
    return lambda x: x * n  # Returns a lambda function

times3 = multiplier(3)  # times3 now multiplies any number by 3
print(times3(5))  # Output: 15

# ✔ Returns a function that multiplies by n.

# 6. Using Lambda with map()
# map() applies a function to each element in a list.

numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x * x, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16]

# ✔ No need for a separate square() function!

# 7. Using Lambda with filter()
# filter() keeps only the elements that match a condition.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6]

# ✔ Keeps only even numbers from the list.

# 8. Using Lambda with reduce()
# reduce() reduces a list to a single value.
from functools import reduce

numbers = [1, 2, 3, 4]
sum_result = reduce(lambda a, b: a + b, numbers)

print(sum_result)  # Output: 10

# Python sort() Method
#The sort() method is used to sort lists in place in Python. It modifies the original list and does not return a new list. It can be used to sort elements in ascending or descending order and also allows sorting with custom criteria using a key.

# 1. Basic Syntax of sort() Method
# list.sort(reverse=False, key=None)
# reverse=False: Sorts in ascending order by default. If set to True, it sorts in descending order.
# key=None: If provided, it's a function that takes an element as input and returns a value to be used for sorting.

# 2. Sorting in Ascending Order (Default)
# The default behavior of sort() is to sort the list in ascending order.
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Sorts the list in ascending order
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]

# Explanation:
# numbers.sort() sorts the list from smallest to largest.
# The original list is modified in place.

# 3. Sorting in Descending Order
# To sort the list in descending order, set the reverse parameter to True.

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)  # Sorts the list in descending order
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]

# Explanation:
# reverse=True sorts the list from largest to smallest.

# 4. Sorting with a Custom Key
# The key parameter allows you to define a custom sorting rule by providing a function that will be applied to each element before sorting.
# Example 1: Sorting Strings by Length

words = ["apple", "banana", "cherry", "date"]
words.sort(key=len)  # Sorts words by their length
print(words)  # Output: ['date', 'apple', 'cherry', 'banana']

# Explanation:
# key=len sorts the list of words based on their length.
# Shorter words come first.

# Example 2: Sorting by a Custom Function
students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
students.sort(key=lambda x: x[1])  # Sorts by the second element (age)
print(students)  # Output: [('Bob', 20), ('Alice', 25), ('Charlie', 30)]

# Explanation:
# key=lambda x: x[1] sorts by the age (second element of each tuple).

# 5. Sorting a List of Dictionaries
# You can also use sort() with dictionaries. Use the key parameter to sort by a specific dictionary value.
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Charlie", "age": 30}]
people.sort(key=lambda x: x["age"])  # Sorts by age
print(people)  # Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

# Explanation:
# key=lambda x: x["age"] sorts the dictionaries by the age key.

# 6. Sorting Lists with Mixed Data Types
# If the list contains mixed types (numbers and strings), sorting may not be directly possible unless we define a sorting strategy.
# Example: Sorting Mixed Data

mixed_data = [1, "apple", 3, "banana", 2]
mixed_data.sort(key=str)  # Sorts by string representation of each element
print(mixed_data)  # Output: [1, 2, 3, 'apple', 'banana']

# Explanation:
# key=str sorts elements by their string representation.

# 7. sorted() vs. sort()
# sort() modifies the list in place.
# sorted() returns a new sorted list without modifying the original list.

numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers)  # Returns a new sorted list
print(sorted_numbers)  # Output: [1, 2, 5, 9]
print(numbers)  # Original list remains unchanged

# Python map() Function
# The map() function is a built-in Python function that applies a function to every item in an iterable (like a list, tuple, etc.) and returns an iterator (which can be converted to a list, tuple, etc.).

# 1. Syntax of map()
# map(function, iterable, ...)
# function: The function to apply to each element of the iterable(s).
# iterable: One or more iterables (e.g., lists, tuples) whose elements will be passed to the function.
# ...: You can pass multiple iterables, and the function will take arguments from each iterable one by one.

# 2. Basic Example of map()
# Here’s an example of using map() to square each number in a list.
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)  # Applies square function to each element

print(list(squared_numbers))  # Output: [1, 4, 9, 16]

# Explanation:
# The square() function is applied to each number in the numbers list.
# map() returns an iterator, so we use list() to convert it into a list for easy viewing.

# 3. Using Lambda with map()
# You can use lambda functions (anonymous functions) with map() to keep the code short.

numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x * x, numbers)  # Using lambda for squaring each element

print(list(squared_numbers))  # Output: [1, 4, 9, 16]

# Explanation:
# lambda x: x * x is the same as the square() function from before, but it's inline.

# 4. Using Multiple Iterables with map()
# If you pass multiple iterables to map(), the function should accept that many arguments.
def add(x, y):
    return x + y

numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]
summed_numbers = map(add, numbers1, numbers2)  # Adds corresponding elements

print(list(summed_numbers))  # Output: [6, 8, 10, 12]

# Explanation:
# The add() function takes two arguments, so map() pairs elements from numbers1 and numbers2 and applies add(x, y) to each pair.

# 5. Using map() with Multiple Functions
# You can also use map() to apply multiple functions to the same iterable.
def square(x):
    return x * x

def cube(x):
    return x * x * x

numbers = [1, 2, 3, 4]
squares = map(square, numbers)
cubes = map(cube, numbers)

print(list(squares))  # Output: [1, 4, 9, 16]
print(list(cubes))  # Output: [1, 8, 27, 64]

# Explanation:
# map() applies square() to numbers and cube() to numbers, creating two separate lists.

# 6. Performance Consideration
# The map() function is more memory-efficient than using a loop when working with large datasets because it returns an iterator and doesn’t generate a full list in memory.


# Python filter() Function
# The filter() function is used to filter out elements from an iterable (like a list, tuple, etc.) based on a condition. It returns an iterator that produces only the items that meet the specified condition.

# 1. Syntax of filter()
# filter(function, iterable)
# function: A function that returns True or False for each item in the iterable. Only the items where the function returns True are kept.
# iterable: The iterable (like a list, tuple, etc.) to be filtered.

# 2. Basic Example of filter()
# Let's start with a simple example where we want to filter out even numbers from a list.
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # Output: [2, 4, 6]

# Explanation:
# The is_even() function checks if a number is divisible by 2.
# filter() applies is_even() to each element of numbers, and only keeps the numbers that satisfy the condition (True).

# 3. Using lambda with filter()
# You can also use lambda functions with filter() to make the code more concise.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # Output: [2, 4, 6]

# Explanation:
# lambda x: x % 2 == 0 is an inline function that returns True if x is even, and False otherwise.

# 4. Filtering Odd Numbers
# You can filter out odd numbers by changing the condition.
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = filter(lambda x: x % 2 != 0, numbers)

print(list(odd_numbers))  # Output: [1, 3, 5]

# Explanation:
# lambda x: x % 2 != 0 filters out the odd numbers from the list.

# 5. Filtering Strings Based on Length
# You can filter strings based on their length using filter().
words = ["apple", "banana", "cherry", "date"]
long_words = filter(lambda x: len(x) > 5, words)

print(list(long_words))  # Output: ['banana', 'cherry']

# Explanation:
# lambda x: len(x) > 5 filters out words whose length is greater than 5.

# 6. Filtering Negative Numbers
# You can filter out negative numbers from a list.
numbers = [-10, 5, -3, 4, 0, -1]
positive_numbers = filter(lambda x: x >= 0, numbers)

print(list(positive_numbers))  # Output: [5, 4, 0]

# Explanation:
# lambda x: x >= 0 filters out negative numbers.

# 7. Using filter() with Multiple Conditions
# You can apply multiple conditions in the filtering function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0 and x > 5, numbers)

print(list(result))  # Output: [6, 8]

# Explanation:
# lambda x: x % 2 == 0 and x > 5 filters the numbers to only keep even numbers greater than 5.

# 8. Using filter() with None as Function
# If you use None as the function, filter() removes falsy values (like 0, False, None, etc.) from the iterable.

values = [0, 1, False, True, "", "hello", None]
filtered_values = filter(None, values)

print(list(filtered_values))  # Output: [1, True, 'hello']

# Explanation:
# None removes any falsy values from the list.

# 9. filter() Returns an Iterator
# The filter() function does not immediately produce a list. It returns an iterator that generates the filtered results when converted to a list (or tuple).

numbers = [1, 2, 3, 4, 5]
filtered = filter(lambda x: x % 2 == 0, numbers)
print(filtered)  # Output: <filter object at 0x...>
print(list(filtered))  # Output: [2, 4]

# Explanation:
# You need to convert the iterator to a list or tuple to view the results.

# Python reduce() Function
# The reduce() function is part of the functools module in Python and is used to apply a binary function (a function that takes two arguments) cumulatively to the items of an iterable, so as to reduce the iterable to a single value.

# 1. Syntax of reduce()
from functools import reduce
# reduce(function, iterable, [initializer])
# function: A binary function that takes two arguments and performs a cumulative operation on them (e.g., addition, multiplication).
# iterable: The iterable (like a list, tuple, etc.) to be reduced.
# initializer (optional): A value that is used as the first argument in the first call to the function. If not provided, the first two items of the iterable are used.

# 2. Basic Example of reduce()
# Let's start with a simple example where we use reduce() to add all numbers in a list.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)

print(result)  # Output: 15
# Explanation:
# lambda x, y: x + y is the function that adds two numbers.
# reduce() applies this function cumulatively to the list [1, 2, 3, 4, 5]:
# First, 1 + 2 = 3
# Then, 3 + 3 = 6
# Then, 6 + 4 = 10
# Finally, 10 + 5 = 15 So the result is 15.

# 3. Using reduce() to Multiply Numbers
# You can also use reduce() to multiply all the numbers in a list.
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 24

# Explanation:
# The lambda x, y: x * y function multiplies two numbers.
# reduce() applies this function cumulatively to the list [1, 2, 3, 4]:
# First, 1 * 2 = 2
# Then, 2 * 3 = 6
# Then, 6 * 4 = 24 The final result is 24.

# 4. Using reduce() with an Initializer
# You can pass an initializer value to reduce(), which will be used as the first argument in the first function call.
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers, 10)

print(result)  # Output: 20

# Explanation:
# The initializer is 10, so the first call of the function is 10 + 1 = 11.
# Then, 11 + 2 = 13, 13 + 3 = 16, and 16 + 4 = 20.
# The result is 20.

# 5. reduce() with Custom Functions
# You can define your own function and use it with reduce().
from functools import reduce
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
result = reduce(add, numbers)

print(result)  # Output: 10

# Explanation:
# The add() function adds two numbers, and reduce() applies it cumulatively to the list [1, 2, 3, 4].
# The result is 10.

# 6. Using reduce() to Find the Maximum Element
# You can use reduce() to find the maximum element in a list.
from functools import reduce

numbers = [1, 4, 3, 8, 2]
max_value = reduce(lambda x, y: x if x > y else y, numbers)

print(max_value)  # Output: 8

# Explanation:
# The lambda x, y: x if x > y else y function returns the larger of the two numbers.
# reduce() compares all the numbers, and the largest one (8) is returned.

# 7. Using reduce() to Combine Strings
# You can use reduce() to combine strings from a list into a single string.
# from functools import reduce
words = ["Hello", "World", "Python"]
result = reduce(lambda x, y: x + " " + y, words)

print(result)  # Output: "Hello World Python"

# Explanation:
# The lambda x, y: x + " " + y function concatenates two strings with a space in between.
# reduce() applies this function cumulatively to the list ["Hello", "World", "Python"], resulting in "Hello World Python".

# 8. Performance Consideration
# Efficiency: reduce() can be useful for cumulative operations like addition, multiplication, etc. However, for simple cases (like adding or multiplying all elements in a list), it's often more readable and efficient to use built-in functions like sum() or prod().

# Python List Comprehension
# List comprehension is a concise way to create lists in Python.
# It allows you to generate a new list by applying an expression to each item in an existing iterable.

# 1. Basic Syntax of List Comprehension
# [expression for item in iterable]
# expression: The operation or value to store in the new list.
# item: Each element in the iterable.
# iterable: A collection (like a list, range, string, etc.) to loop over.

# 2. Example 1: Creating a List of Squares
# Let's start with a simple example where we create a list of the squares of numbers from 1 to 5.

squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Explanation:
# The expression x**2 squares each number.
# The iterable range(1, 6) generates numbers from 1 to 5.
# The list comprehension generates a new list with the squared values.

# 3. Example 2: Creating a List of Even Numbers
# We can also use list comprehension to filter out even numbers from a range.

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Explanation:
# if x % 2 == 0 filters out only even numbers.
# range(1, 11) generates numbers from 1 to 10.
# The list comprehension adds only the even numbers to the new list.

# 4. Example 3: Convert Strings to Uppercase
# You can use list comprehension to perform operations on strings as well.

words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Explanation:
# word.upper() converts each string to uppercase.
# The list comprehension processes each word in the list words and generates the new list uppercase_words.

# 5. Example 4: Nested List Comprehension
# List comprehension can also be nested, meaning we can loop over lists of lists.
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [element for row in matrix for element in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

# Explanation:
# The outer loop iterates over each row in the matrix.
# The inner loop iterates over each element in the row.
# This flattens the list of lists into a single list.

# 6. Example 5: Applying Multiple Conditions
# You can include multiple conditions in a list comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x for x in numbers if x % 2 == 0 if x > 5]
print(result)  # Output: [6, 8, 10]

# Explanation:
# if x % 2 == 0 ensures only even numbers are included.
# if x > 5 filters out numbers greater than 5.
# The result is [6, 8, 10].

# 7. Example 6: Using List Comprehension with Functions
# You can apply functions within list comprehensions.
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squares = [square(x) for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Explanation:
# The square() function is applied to each number in the list.
# The list comprehension generates the squared values.

# 8. Example 7: Using else in List Comprehension
# You can include an else statement in a list comprehension to assign a value based on a condition.

numbers = [1, 2, 3, 4, 5]
result = [x if x % 2 == 0 else "odd" for x in numbers]
print(result)  # Output: ['odd', 2, 'odd', 4, 'odd']

# Explanation:
# If x % 2 == 0 (even number), it keeps x.
# If x is odd, it replaces it with the string "odd".
# The result is ['odd', 2, 'odd', 4, 'odd'].

# 9. Example 8: Creating a List of Tuples
# You can generate lists of tuples using list comprehension.
pairs = [(x, x**2) for x in range(1, 6)]
print(pairs)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Explanation:
# For each number x, it creates a tuple (x, x**2) with the number and its square.
# The result is a list of tuples [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)].

# 10. Example 9: Flatten a List of Lists
# You can flatten a list of lists using list comprehension.
matrix = [[1, 2, 3], [4, 5], [6]]
flat_list = [item for sublist in matrix for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]

# Explanation:
# The list comprehension iterates through each sublist and then through each item in the sublist, resulting in a flattened list.

# Python Dictionary Comprehension
# Dictionary comprehension in Python allows you to create dictionaries in a concise
# and readable way using a single line of code. It follows a similar structure to list comprehension but generates a dictionary instead of a list.

# 1. Basic Syntax of Dictionary Comprehension
# {key_expression: value_expression for item in iterable}
# key_expression: The key for the new dictionary.
# value_expression: The value associated with the key.
# item: Each element in the iterable.
# iterable: The collection you are iterating over (e.g., list, range, etc.).

# 2. Example 1: Basic Dictionary Comprehension
# Let's create a dictionary where the keys are numbers and the values are their squares.
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# Explanation:
# The key is x, and the value is x**2 (the square of x).
# range(1, 6) generates numbers from 1 to 5.
# The resulting dictionary is {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

# 3. Example 2: Filtering with Dictionary Comprehension
# You can add a condition to filter items in the dictionary comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(even_squares)

# Explanation:
# if x % 2 == 0 filters only the even numbers.
# The resulting dictionary is {2: 4, 4: 16, 6: 36, 8: 64}.

# 4. Example 3: Using Functions in Dictionary Comprehension
# You can apply functions to the keys or values in dictionary comprehension.
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squares = {x: square(x) for x in numbers}
print(squares)

# Explanation:
# The function square() is applied to each number to calculate its square.
# The resulting dictionary is {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

# 5. Example 4: Using if-else in Dictionary Comprehension
# You can use an if-else condition to assign different values based on a condition.
numbers = [1, 2, 3, 4, 5]
result = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
print(result)

# Explanation:
# x: "even" if x % 2 == 0 else "odd" assigns the value "even" for even numbers and "odd" for odd numbers.
# The resulting dictionary is {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}.

# 6. Example 5: Nested Dictionary Comprehension
# You can use dictionary comprehension to create nested dictionaries.

keys = ['a', 'b', 'c']
values = [1, 2, 3]

nested_dict = {key: {value: value**2} for key, value in zip(keys, values)}
print(nested_dict)

# Explanation:
# zip(keys, values) pairs each key with a corresponding value.
# The value of each key is another dictionary, where the inner dictionary has the value as the key and the square of the value as the value.
# The resulting dictionary is {'a': {1: 1}, 'b': {2: 4}, 'c': {3: 9}}.

# 7. Example 6: Combining Two Lists into a Dictionary
# You can combine two lists into a dictionary using dictionary comprehension.

keys = ['name', 'age', 'course']
values = ['Alice', 25, 'Math']

info = {key: value for key, value in zip(keys, values)}
print(info)

# Explanation:
# zip(keys, values) pairs each key with a corresponding value.
# The resulting dictionary is {'name': 'Alice', 'age': 25, 'course': 'Math'}.

# 8. Example 7: Modifying a Dictionary with Comprehension
# You can modify an existing dictionary by applying dictionary comprehension.

original_dict = {'a': 1, 'b': 2, 'c': 3}
modified_dict = {key: value * 2 for key, value in original_dict.items()}
print(modified_dict)

# Explanation:
# original_dict.items() provides the key-value pairs.

# The value for each key is multiplied by 2.
# The resulting dictionary is {'a': 2, 'b': 4, 'c': 6}.

# 9. Example 8: Swapping Keys and Values in a Dictionary
# You can use dictionary comprehension to swap keys and values.

original_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = {value: key for key, value in original_dict.items()}
print(swapped_dict)

# Explanation:
# The key-value pairs are swapped in the new dictionary.
# The resulting dictionary is {1: 'a', 2: 'b', 3: 'c'}.


# Python zip() Function
# The zip() function in Python is used to combine two or more iterables (lists, tuples, etc.) into an iterator of tuples. Each tuple contains elements from each of the iterables at the same position.

# 1. Basic Syntax of zip()
# zip(iterable1, iterable2, ...)
# iterable1, iterable2, ...: These are the iterables you want to combine.
# The zip() function returns an iterator that aggregates elements from each iterable. You can convert this iterator into a list or other collection types like tuples or dictionaries.

# 2. Example 1: Combining Two Lists
# Let's see how to combine two lists using zip().

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = zip(list1, list2)
print(list(result))

# Explanation:
# zip(list1, list2) combines the elements of both lists into pairs.
# The output will be a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')].

# 3. Example 2: Combining More Than Two Lists
# You can combine more than two iterables with zip().

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

result = zip(list1, list2, list3)
print(list(result))

# Explanation:
# zip(list1, list2, list3) combines elements from all three lists at the same position.
# The output will be a list of tuples: [(1, 'a', True), (2, 'b', False), (3, 'c', True)].

# 4. Example 3: Different Lengths of Iterables
# If the input iterables have different lengths, zip() stops at the shortest iterable.

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']

result = zip(list1, list2)
print(list(result))

# Explanation:
# Since list2 is shorter, zip() stops at the third element.
# The output will be: [(1, 'a'), (2, 'b'), (3, 'c')].

# 5. Example 4: Unzipping Using zip()
# You can "unzip" an iterator of tuples back into separate iterables using zip() in combination with the unpacking operator *.

zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*zipped)

print(list1)  # Output: (1, 2, 3)
print(list2)  # Output: ('a', 'b', 'c')

# Explanation:
# zip(*zipped) unzips the list of tuples into two separate lists.
# *zipped unpacks the zipped object into separate arguments for zip(), which then reverts to the original individual lists.

# 6. Example 5: Using zip() with Iterables of Different Types
# zip() can work with iterables of different types.

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

result = zip(names, ages)
print(list(result))

# Explanation:
# zip(names, ages) combines a list of strings (names) and a list of integers (ages).
# The output will be: [('Alice', 25), ('Bob', 30), ('Charlie', 35)].

# 7. Example 6: Converting zip() to Dictionary
# You can use zip() to easily create a dictionary.

keys = ['name', 'age', 'course']
values = ['Alice', 25, 'Math']

result = dict(zip(keys, values))
print(result)

# Explanation:
# zip(keys, values) combines the two lists into key-value pairs.
# dict() converts the result of zip() into a dictionary: {'name': 'Alice', 'age': 25, 'course': 'Math'}.

# 8. Example 7: Iterating Through zip()
# You can iterate through the result of zip() just like you would with any iterable.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for item in zip(list1, list2):
    print(item)

# Explanation:
# The for loop iterates over the zipped object and prints each tuple.
# The output will be:
# (1, 'a')
# (2, 'b')
# (3, 'c')

# Python time Module
# The time module in Python provides functions for working with time-related tasks. You can use it to get the current time, measure time intervals, and perform other time-related operations.

# 1. Importing the time Module
# Before using any function from the time module, you need to import it.
import time

# 2. time() Function
# The time() function returns the current time in seconds since the epoch (January 1, 1970, 00:00:00 UTC) as a floating-point number.
current_time = time.time()
print(current_time)

# Explanation:
# time.time() returns the current time in seconds as a float.
# The output might look like: 1675151563.238453 (this is just an example).

# 3. sleep() Function
# The sleep() function is used to pause the execution of your program for a specified amount of time.

print("Before sleep")
time.sleep(2)  # Pauses the program for 2 seconds
print("After sleep")

# Explanation:
# time.sleep(2) pauses the program for 2 seconds.
# Output: Before sleep (waits 2 seconds) After sleep

# 4. ctime() Function
# The ctime() function returns a human-readable string representing the current time. It converts a time in seconds (since the epoch) to a string.

current_time = time.time()
formatted_time = time.ctime(current_time)
print(formatted_time)

# Explanation:
# time.ctime() formats the time (in seconds) into a human-readable format.
# Example output: "Tue Feb 20 14:05:28 2025".

# 5. localtime() Function
# The localtime() function converts a time in seconds into a struct_time object, which represents the local time.

current_time = time.time()
local_time = time.localtime(current_time)
print(local_time)

# Explanation:
# time.localtime() returns a struct_time object that includes attributes such as tm_year, tm_hour, tm_min, etc.
# Example output:

time.struct_time(tm_year=2025, tm_mon=2, tm_mday=20, tm_hour=14, tm_min=5, tm_sec=28, tm_wday=4, tm_yday=51, tm_isdst=0)

# 6. strftime() Function
# The strftime() function is used to format struct_time into a string based on a specific format.

current_time = time.time()
local_time = time.localtime(current_time)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print(formatted_time)

# Explanation:
# time.strftime("%Y-%m-%d %H:%M:%S", local_time) converts struct_time into a custom string format.
# "%Y-%m-%d %H:%M:%S" specifies the format as year-month-day hour:minute:second.
# Example output: "2025-02-20 14:05:28".

# 7. strptime() Function
# The strptime() function is used to parse a string into a struct_time object according to a given format.
time_string = "2025-02-20 14:05:28"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(parsed_time)

# Explanation:
# time.strptime(time_string, format) converts a string into struct_time based on the specified format.
# Example output:
time.struct_time(tm_year=2025, tm_mon=2, tm_mday=20, tm_hour=14, tm_min=5, tm_sec=28, tm_wday=4, tm_yday=51, tm_isdst=-1)

# 8. Measuring Time Intervals (perf_counter())
# You can measure time intervals using perf_counter(), which provides a high-resolution timer.

start_time = time.perf_counter()
# Some code to measure
time.sleep(2)  # Simulate a delay
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

# Explanation:
# time.perf_counter() provides a precise time measurement.
# elapsed_time gives the time taken to execute the code between start_time and end_time.
# Example output: Elapsed time: 2.002034 seconds.

# 9. process_time() Function
# The process_time() function is used to measure CPU time, i.e., the amount of time the CPU spends running your program (not including time when the CPU is idle).

start_time = time.process_time()
# Some code to measure
time.sleep(2)  # Simulate a delay
end_time = time.process_time()

elapsed_time = end_time - start_time
print(f"CPU time: {elapsed_time} seconds")

# Explanation:
# time.process_time() returns the CPU time consumed by the program.
# This measurement excludes time when the program is sleeping or waiting.
# Example output: CPU time: 0.002345 seconds.

# 10. timezone and tzname
# The timezone and tzname attributes provide information about time zone offsets and names.

print("Timezone offset (seconds):", time.timezone)
print("Timezone name:", time.tzname)

# Explanation:
# time.timezone gives the offset in seconds from UTC for the local time zone.
# time.tzname gives the name of the time zone (e.g., "EST" for Eastern Standard Time).

# Python threading Module
# The threading module in Python provides a way to run multiple operations concurrently, allowing you to execute multiple threads (smaller units of a program) in parallel. This is particularly useful for tasks that are I/O-bound or require multitasking.

# 1. Importing the threading Module
# To use threads in Python, you need to import the threading module.
import threading

# 2. Creating a Thread
# You can create a thread by instantiating the Thread class. A thread can be created to execute a specific function.
# Example:
import threading

def print_message():
    print("Hello from the thread!")

# Create a thread
thread = threading.Thread(target=print_message)

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

# Explanation:
# threading.Thread(target=print_message) creates a new thread that will execute the print_message() function.
# thread.start() starts the thread.
# thread.join() ensures that the main program waits for the thread to complete before continuing.

# 3. Passing Arguments to Threads
# You can pass arguments to the function that the thread will execute using the args parameter.
# Example:
import threading

def print_message(name):
    print(f"Hello, {name}!")

# Create a thread and pass the argument
thread = threading.Thread(target=print_message, args=("Alice",))

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

# Explanation:
# args=("Alice",) passes the argument "Alice" to the print_message() function.
# The output will be: Hello, Alice!.

# 4. Running Multiple Threads
# You can create and run multiple threads at the same time.
# Example:

import threading

def print_message(name):
    print(f"Hello, {name}!")

# Create multiple threads
thread1 = threading.Thread(target=print_message, args=("Alice",))
thread2 = threading.Thread(target=print_message, args=("Bob",))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

# Explanation:
# Two threads are created, one for "Alice" and one for "Bob".
# The threads will run concurrently.
# The output will be: Hello, Alice! Hello, Bob!

# 5. Using Thread with a Target Function
# You can also create a thread by subclassing the Thread class and overriding the run() method.
# Example:
import threading

class MyThread(threading.Thread):
    def run(self):
        print("Hello from the custom thread!")

# Create a thread
thread = MyThread()

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()

# Explanation:
# MyThread subclasses the Thread class and overrides the run() method.
# thread.start() starts the thread and calls the run() method.

# 6. Daemon Threads
# A daemon thread is a thread that runs in the background and doesn't prevent the program from exiting. When all non-daemon threads finish, the program ends, even if daemon threads are still running.
# Example:

import threading
import time

def background_task():
    while True:
        print("Background task running...")
        time.sleep(1)

# Create a daemon thread
thread = threading.Thread(target=background_task, daemon=True)

# Start the thread
thread.start()

# Main program will end after 5 seconds
time.sleep(5)
print("Main program finished")

# Explanation:
# The background task will print a message every second, but the program will exit after 5 seconds because it's a daemon thread.
# The output will be:
# Background task running...
# Background task running...
# Background task running...
# Main program finished

# 7. Synchronizing Threads with Locks
# In multi-threaded programs, multiple threads might try to modify shared data at the same time. This can cause data corruption. You can use locks to ensure that only one thread can access a shared resource at a time.
# Example:

import threading

# Shared resource
counter = 0

# Create a lock
lock = threading.Lock()

def increment_counter():
    global counter
    with lock:  # Ensures only one thread can access this block at a time
        counter += 1
        print(f"Counter value: {counter}")

# Create multiple threads
threads = []
for _ in range(5):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Final counter value:", counter)

# Explanation:
# lock = threading.Lock() creates a lock object.
# with lock: ensures that only one thread can increment counter at a time.
# The program creates 5 threads, each trying to increment the shared counter.
# Output (may vary slightly due to timing):
# Counter value: 1
# Counter value: 2
# Counter value: 3
# Counter value: 4
# Counter value: 5
# Final counter value: 5

# 8. Threading with Event
# The Event class is used to signal threads to perform an action. One thread sets the event, and other threads wait for it to be set before continuing.
# Example:

import threading
import time

# Create an event object
event = threading.Event()

def wait_for_event():
    print("Thread waiting for event to be set.")
    event.wait()  # Block until the event is set
    print("Thread received the event!")

# Create and start threads
thread1 = threading.Thread(target=wait_for_event)
thread2 = threading.Thread(target=wait_for_event)
thread1.start()
thread2.start()

# Set the event after 2 seconds
time.sleep(2)
print("Setting the event.")
event.set()

# Wait for threads to finish
thread1.join()
thread2.join()

# Explanation:
# event.wait() blocks the thread until the event is set by event.set().
# Both threads wait for the event to be set before printing the second message.

# 9. Threading with Condition
# A Condition variable allows threads to wait until a certain condition is met, then be notified.
# Example:

import threading

# Create a condition object
condition = threading.Condition()

def task():
    with condition:
        print("Waiting for the condition to be met.")
        condition.wait()  # Block until notified
        print("Condition met, thread proceeding.")

# Create and start a thread
thread = threading.Thread(target=task)
thread.start()

# Simulate some processing before notifying the condition
with condition:
    print("Condition is now met.")
    condition.notify()  # Notify waiting threads

# Wait for the thread to finish
thread.join()

# Explanation:
# condition.wait() makes the thread wait.
# condition.notify() wakes up one of the waiting threads.

# Python multiprocessing Module
# The multiprocessing module in Python allows you to create multiple processes, enabling concurrent execution across multiple CPU cores. This is particularly useful for CPU-bound tasks, where parallel execution can improve performance.

# 1. Importing the multiprocessing Module
# To use multiprocessing in Python, you need to import the multiprocessing module.
import multiprocessing

# 2. Creating a Process
# A process in multiprocessing is similar to a thread but runs in a separate memory space. You can create a process by instantiating the Process class and passing the target function.
# Example:
import multiprocessing

def print_message():
    print("Hello from the process!")

# Create a process
process = multiprocessing.Process(target=print_message)

# Start the process
process.start()

# Wait for the process to complete
process.join()

# Explanation:
# multiprocessing.Process(target=print_message) creates a new process that will execute the print_message() function.
# process.start() starts the process.
# process.join() ensures that the main program waits for the process to complete before continuing.

# 3. Passing Arguments to Processes
# You can pass arguments to the target function of a process using the args parameter.
# Example:
import multiprocessing

def print_message(name):
    print(f"Hello, {name}!")

# Create a process and pass the argument
process = multiprocessing.Process(target=print_message, args=("Alice",))

# Start the process
process.start()

# Wait for the process to complete
process.join()

# Explanation:
# args=("Alice",) passes the argument "Alice" to the print_message() function.
# The output will be: Hello, Alice!.

# 4. Running Multiple Processes
# You can create and run multiple processes in parallel.
# Example:
import multiprocessing

def print_message(name):
    print(f"Hello, {name}!")

# Create multiple processes
process1 = multiprocessing.Process(target=print_message, args=("Alice",))
process2 = multiprocessing.Process(target=print_message, args=("Bob",))

# Start the processes
process1.start()
process2.start()

# Wait for the processes to complete
process1.join()
process2.join()

# Explanation:
# Two processes are created, one for "Alice" and one for "Bob".
# The processes will run concurrently.
# The output will be:
# Hello, Alice!
# Hello, Bob!

# 5. Using Pool for Parallel Execution
# If you have a function that needs to be applied to multiple items, you can use multiprocessing.Pool to parallelize the task across multiple processes.
# Example:
import multiprocessing

def square(number):
    return number * number

# Create a pool of processes
with multiprocessing.Pool() as pool:
    result = pool.map(square, [1, 2, 3, 4, 5])

print(result)

# Explanation:
# pool.map(square, [1, 2, 3, 4, 5]) applies the square() function to each item in the list [1, 2, 3, 4, 5] in parallel.
# The output will be: [1, 4, 9, 16, 25].

# 6. Shared Memory with Value and Array
# In multiprocessing, different processes do not share memory by default. However, you can create shared memory using Value (for single values) or Array (for sequences of values).
# Example (Shared Value):
import multiprocessing

def increment(shared_value):
    shared_value.value += 1

# Create a shared value
shared_value = multiprocessing.Value('i', 0)

# Create multiple processes
process1 = multiprocessing.Process(target=increment, args=(shared_value,))
process2 = multiprocessing.Process(target=increment, args=(shared_value,))

# Start the processes
process1.start()
process2.start()

# Wait for the processes to complete
process1.join()
process2.join()

print(f"Final value: {shared_value.value}")

# Explanation:
# shared_value = multiprocessing.Value('i', 0) creates a shared integer initialized to 0.
# Both processes increment the shared value by 1.
# The output will be: Final value: 2.

# 7. Using Queue for Communication Between Processes
# You can use a Queue to send data between processes, which allows inter-process communication (IPC).
# Example:

import multiprocessing

def producer(queue):
    queue.put("Message from producer")

def consumer(queue):
    message = queue.get()
    print(f"Consumer received: {message}")

# Create a queue
queue = multiprocessing.Queue()

# Create producer and consumer processes
process1 = multiprocessing.Process(target=producer, args=(queue,))
process2 = multiprocessing.Process(target=consumer, args=(queue,))

# Start the processes
process1.start()
process2.start()

# Wait for the processes to complete
process1.join()
process2.join()

# Explanation:
# The producer process puts a message in the queue using queue.put().
# The consumer process retrieves the message from the queue using queue.get().
# The output will be: Consumer received: Message from producer.

# 8. Using Manager for Shared Data Structures
# The Manager class allows the creation of shared data structures like lists, dictionaries, etc., that can be safely accessed by multiple processes.
# Example (Shared List):
# import multiprocessing

def append_to_list(shared_list):
    shared_list.append("Data")

# Create a manager
with multiprocessing.Manager() as manager:
    # Create a shared list
    shared_list = manager.list()

    # Create multiple processes
    process1 = multiprocessing.Process(target=append_to_list, args=(shared_list,))
    process2 = multiprocessing.Process(target=append_to_list, args=(shared_list,))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for the processes to complete
    process1.join()
    process2.join()

    print(f"Final list: {shared_list}")

# Explanation:
# shared_list = manager.list() creates a list that can be accessed by multiple processes.
# Both processes append "Data" to the list.
# The output will be: Final list: ['Data', 'Data'].

# 9. Process Pool with apply_async
# The apply_async() method in the Pool class allows you to apply a function asynchronously to multiple inputs.
# Example:

import multiprocessing

def square(number):
    return number * number

# Create a pool of processes
with multiprocessing.Pool() as pool:
    result = pool.apply_async(square, (5,))

    # Wait for the result
    print(result.get())

# Explanation:
# pool.apply_async(square, (5,)) asynchronously applies the square() function to 5.
# result.get() retrieves the result once the process finishes.
# The output will be: 25.

# 10. Daemon Processes
# Like threads, processes can also be marked as daemon processes. A daemon process runs in the background and does not block the program from exiting when the main process finishes.
# Example:

import multiprocessing
import time

def background_task():
    while True:
        print("Background task running...")
        time.sleep(1)

# Create a daemon process
process = multiprocessing.Process(target=background_task, daemon=True)

# Start the process
process.start()

# Main program will end after 5 seconds
time.sleep(5)
print("Main program finished")

# Explanation:
# The background task will continue to run, but the program will terminate after 5 seconds since the process is a daemon.
# The output will be:
# Background task running...
# Background task running...
# Background task running...
# Main program finished

