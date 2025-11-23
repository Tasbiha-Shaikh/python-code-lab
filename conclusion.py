# -------------------------------
#   PYTHON PROGRAM BASIC CONCEPTS
# -------------------------------

# IMPORTING MODULES

import math          # built-in module
import datetime      # module for date & time

# COMMENTS

# This is a single-line comment
"""
This is a multi-line comment
Explaining basic Python concepts
"""

# VARIABLES & DATA TYPES

name = "Tasbiha"     # string
age = 22             # integer
height = 5.4         # float
is_student = True    # boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# STRINGS

message = "Hello Python Programming"

print("\nOriginal Message:", message)

# STRING SLICING
print("First 5 characters:", message[0:5])
print("Last 5 characters:", message[-5:])
print("Every 2nd char:", message[0::2])

# STRING FUNCTIONS
print("\nUppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title:", message.title())
print("Replace:", message.replace("Python", "World"))
print("Split:", message.split(" "))
print("Length:", len(message))


# LISTS

fruits = ["apple", "banana", "orange"]

print("\nFruit List:", fruits)
print("First Fruit:", fruits[0])

fruits.append("mango")       # add item
fruits.remove("banana")      # remove item

print("Updated Fruit List:", fruits)


# TUPLES

colors = ("red", "green", "blue")

print("\nColors Tuple:", colors)
print("Second Color:", colors[1])


# USING A MODULE

print("\nSquare root of 25:", math.sqrt(25))
print("Current Date:", datetime.datetime.now())