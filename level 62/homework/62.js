//  Multiply Two Numbers Write a function multiply() that prompts the user to input two numbers and returns their product.

function multiply(){
    num1 = prompt("Enter num1:");
    num2 = prompt("Enter num2:");
    result = num1 * num2;
    console.log(result);
}

// Subtract Two Numbers Write a function subtract() that prompts the user for two numbers and returns the difference.

function subtract(){
    num1 = prompt("Enter num");
    num2 = prompt("Enter num");
    result = num1 - num2;
    console.log(result);
}

// // Divide Two Numbers Write a function divide() that prompts the user for two numbers and returns their quotient.

function divide(){
    num1 = prompt("Enter num");
    num2 = prompt("Enter num");
    result = num1 / num2;
    console.log(result);
}
// // Return a Full Name Write a function fullName() that prompts the user to input their first name and last name, and returns the full name as a single string.

function fullName(){
    Name = (input("enter your name"));
    surname = (input("enter your surname"));
    full_name = Name + " " + surname;
    console.log(full_name);
}

// // .Convert Minutes to Seconds Write a function minutesToSeconds() that prompts the user for a number of minutes and returns the equivalent in seconds.

function minutesToSeconds(){
    minuts = int(input("enter minuts"));
    seconds = minuts * 60;
    console.log(seconds);
}

// // Calculate the Area of a Rectangle Write a function rectangleArea() that prompts the user to input the length and width of a rectangle and returns the area.

function rectangleArea(){
    length = int(input("enter length"));
    width = int(input("enter width"));
    area = length * width;
    console.log(area);
}

// // Concatenate Two Strings Write a function concatenateStrings() that prompts the user for two strings and returns them concatenated together.

function concatenateStrings() {
    num1 = input("enter str1");
    num2 = input("enter str2");
    concatenated = num1 + num2;
    console.log(concatenated);
}

// // Exponentiation Write a function power() that prompts the user for a base number and an exponent, and returns the result of raising the base to the power of the exponent.

function power(){
    base = int(input("enter base"));
    exponent = int(input("enter exponent"));
    result = base ** exponent;
    console.log(result);
}

// Calculate Circle Circumference Write a function circumference() that prompts the user to input a circle's radius and returns the circumference.

function circumference(){
    radius = int(input("enter radius"));
    circumference = 4 * 2,5 * radius;
    console.log(circumference);
}

// // Return the Next Number Write a function nextNumber() that prompts the user for a number and returns the next number (the input number plus one).

function nextNumber(){
    number = int(input("enter number"));
    next_number = number + 1;
    console.log(next_number);
}