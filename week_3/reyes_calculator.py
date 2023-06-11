# Exercise 3.3 - Calculator Program
# Code referenced from https://www.w3schools.com/python/python_functions.asp

# This function adds x and y values.
def add(x, y): 
    return x + y

# This function subtracts x and y values.
def subtract(x, y):
    return x - y

# This function multiplies x and y values.
def multiply(x, y):
    return x * y

# This function divides x and y values.
def divide(x, y):
    return x / y

# Variables for calculator input.
num_1 = 4
num_2 = 7
num_3 = 15
num_4 = 6
num_5 = 8
num_6 = 2
num_7 = 10
num_8 = 2

# Template for first number, operation, second number, and result.
output_template = "%s %s %s is %s."

print(output_template %(num_1, '+', num_2, add(num_1, num_2)))
print(output_template %(num_3, '-', num_4, subtract(num_3, num_4)))
print(output_template %(num_5, '*', num_6, multiply(num_5, num_6)))
print(output_template %(num_7, '/', num_8, divide(num_7, num_8)))

