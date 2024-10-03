# Multiply Two Numbers Write a function multiply() that prompts the user to input two numbers and returns their product.

def multiply():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    product = num1 * num2
    return product

result = multiply()
print({result})

#Subtract Two Numbers Write a function subtract() that prompts the user for two numbers and returns the difference.

def subtract():
    num1 = int(input("enter num"))
    num2 = int(input("enter num"))
    difference = num1 - num2
    return difference

result = subtract()
print({result})

#Divide Two Numbers Write a function divide() that prompts the user for two numbers and returns their quotient.

def divide():
    num1 = int(input("enter num"))
    num2 = int(input("enter num"))
    quotient = num1 / num2
    return quotient
result = divide()
print({result})

#Return a Full Name Write a function fullName() that prompts the user to input their first name and last name, and returns the full name as a single string.

def fullName():
    name = (input("enter your name"))
    surname = (input("enter your surname"))
    full_name = name + " " + surname
    return full_name
result = fullName()
print({result})

#.Convert Minutes to Seconds Write a function minutesToSeconds() that prompts the user for a number of minutes and returns the equivalent in seconds.

def minutesToSeconds():
    minuts = int(input("enter minuts"))
    seconds = minuts * 60
    return seconds
result = minutesToSeconds()
print({result})

#Calculate the Area of a Rectangle Write a function rectangleArea() that prompts the user to input the length and width of a rectangle and returns the area.

def rectangleArea():
    length = int(input("enter length"))
    width = int(input("enter width"))
    area = length * width
    return area
result = rectangleArea()
print({result})

#Concatenate Two Strings Write a function concatenateStrings() that prompts the user for two strings and returns them concatenated together.

def concatenateStrings():
    num1 = input("enter str1")
    num2 = input("enter str2")
    concatenated = num1 + num2
    return concatenated
result = concatenateStrings()
print({result})

#Exponentiation Write a function power() that prompts the user for a base number and an exponent, and returns the result of raising the base to the power of the exponent.

def power():
    base = int(input("enter base"))
    exponent = int(input("enter exponent"))
    result = base ** exponent
    return result
result = power()
print({result})

#Calculate Circle Circumference Write a function circumference() that prompts the user to input a circle's radius and returns the circumference.

def circumference():
    radius = int(input("enter radius"))
    circumference = 4 * 2,5 * radius
    return circumference
result = circumference()
print({result})

#Return the Next Number Write a function nextNumber() that prompts the user for a number and returns the next number (the input number plus one).

def nextNumber():
    number = int(input("enter number"))
    next_number = number + 1
    return next_number
result = nextNumber()
print({result})