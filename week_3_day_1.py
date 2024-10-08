# # Week3
# # This week we will work on :
# # Working With Strings


# # 1.   Working With Numbers
# # 2.   Getting Input From Users




# # 1.   Building a Basic Calculator
# # 2.   Mad Libs Game

###############################################################################################

# # Review
# create variables for the following :
# 1. age
age = 16
# 2. name
name = "Bryan"
# 3. song
song = "Hate. Breeds. Life"
# 4. food
food = "comida"
# 5. number
number = 59


# #now include the variables you just made print in the following...


# Once upon a time, there was a [age] old coder named [name].
#concatenation

# [name] liked to hum the song [song] while coding. It was so annoying that their teammates would throw [food] until [name] would stop singing.


# Still, [name] was the best coder on the team and could write [number] lines of code every day. Maybe [song] was [name]’s secret power?
##########################################################################################

print(f"Once upon a time, there was a {age} old coder named {name}.")
print(f"{name} liked to hum the song {song} while coding. It was so annoying that their teammates would throw {food} until {name} would stop singing.")
print(f"Still, {name} was the best coder on the team and could write {number} lines of code every day. Maybe {song} was {name}’s secret power?")

date_of_birth = 2021
number2 = 123
number3 = 123.456
number4 = 123.33
number5 = 4555

print("one and a " + str(number2) + " and a " + str(number3) + " and a " + str(number4) + " and a " + str(number5) + " and born on " + str(date_of_birth))
print(f"the date of birth is {date_of_birth}, one and a {number2} and a {number3} and a {number3} and a {number4} and a {number5}")

##########################################################################################
# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
#    or 'I' (uppercase letter eye) as single character variable names.
# 6. Avoid using words that have special meaning in Python like "list" and "str"


# Here are some exercises to practice the rules:


# Correcting Invalid Names: Below are some invalid names. Correct them according to the rules:


# first_name
# last_name
# email_address
# percent
# variable_name
# zero
# you cannot use a reserved word for your own varaiable
# Creating Valid Names: Create valid names for the following descriptions:


# The first name of a person
# The last name of a person
# The email address of a person
# The percentage of marks obtained by a student
# A variable to store the number of items in a shopping cart




# Identify Valid and Invalid Names: Identify which of the following names are valid or invalid according to the rules:


# first_name
# lastName
# email_address
# percentage
# variable_name
# first_variable
# email_address
# percentage
# integer


# # **Working with** **numbers** **bold text**
# We'll learn about the following topics:
# 1. Types of Numbers in Python
# 2. Basic Arithmetic
# 3. Differences between classic division and floor division


# Python has various "types" of numbers (numeric literals).
# 1. We'll mainly focus on integers and floating point numbers.
# Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.


##########################################################################################
# #addition
print(2+1)
# #multiplication
print(2*2)
# #division
print(6/2)
# #modulo
print(7%4)
# #powers
print(2**3)
# #get the max and min of a number
print(f"the max of 2 and 3: {max(2,3)}")
print(f"The min of 2 and 3: {min(2,3)}")
# #round a number
print(f"rounded num: {round(3.2)}")
# # absolute value
print(f"absolute value {abs(-15)}")
# # order of operations
print(f"10-9+10*7 is = ",7*10+9-10)
# #to do more you need to import special math libraries from python
from math import *    
# #this goes out and grabs some different math functions we can use
# #floor method
print(floor(2.95))
# #ceil method
print(ceil(6.0001))
# #sqrt method
print(sqrt(16))














##########################################################################################
# So what have we learned? We learned some of the basics of numbers in Python. We also learned how to do arithmetic and use Python as a basic calculator. We then wrapped it up with learning about Variable Assignment in Python.
# # **Getting Input from users**
# #how do we get input from users?
# input("what is your name?")
name = input("What is your name?: ")
# # basic math calculator
# #ask the user for 2 numbers
num_one = float(input("Input your first number: "))
num_two = float(input("Input your second number: "))
# # print out a statement where you:
# # add them together
print("Result: ",num_one+num_two)
# #multiply
# # find the max number
print("Here's the max of both numbers: ",max(num_one, num_two))
# # find the remainder of the numbers
print(f"The remainder of {num_one} and {num_two} is: ",(num_one%num_two))
# #round one number
print("Rounded: ",round(num_one))








##########################################################################################
# # mad libs game
# print("Roses are {color}")
# print("{plural noun} are blue")
# print("I love {celebrity}")
# # On to codehs.com

###########################################################################################

print("------------------- \n Helllo User\n-------------------------")

num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))

print("Subtracted: ",(num1-num2))
print("Divided: ",(num1-num2))
print("Min number: ",(min(num1,num2)))
print("Absolute value First Number: ",abs(num1))
print("Floor of First Number: ",floor(num1))
print("Ceiling of Second Number: ",ceil(num2))
print("Square Root of Second Number: ",sqrt(num2))