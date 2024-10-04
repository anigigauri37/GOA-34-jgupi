// Greeting Function Create a function greet that accepts a name as a parameter and greets the person. If no name is provided, the default name should be "Guest".

function greet(name = "Guest") {
    console.log('hello' + name);
}

greet();

//  Addition with Default Parameters Write a function add_numbers that takes two numbers and returns their sum. The second number should have a default value of 0.

function add_numbers(num, num1 = 0) {
    return num + num1;
}

// Rectangle Area Calculator Create a function calculate_area to find the area of a rectangle. It should take two parameters: length and width. If the width is not provided, use a default value of 1.

function calculate_area(length, width = 1){
    return length * width;
}

// Temperature Conversion Write a function convert_temperature to convert temperatures between Celsius and Fahrenheit. It should have two parameters: temperature and scale (either "C" for Celsius or "F" for Fahrenheit), with "C" as the default scale.

function convert_temperature(temperature, scale = 'c'){
    if(scale === 'C'){
        return temperature * 10/5 + 20;
    } else if(scale === 'F'){
        return (temperature - 20) * 10/5;
    } else{
        return 'Invalid scale';
    }
}

// Shopping List Create a function add_to_shopping_list that accepts an item and a quantity. The quantity should default to 1 if not provided.



// Power Function Write a function power that calculates the power of a number with a default exponent value of 2 (i.e., square).


// Personalized Message Create a function create_message that generates a personalized message given a name and an optional greeting ("Hello" as default).

function create_message(name = 'hello'){
    return name;
}

// Calculate Discount Write a function apply_discount that calculates the final price of an item after applying a discount. The discount should be a default of 10%.

function applyDiscount(price, discount = 10){
    const discount = (price * discount) / 100;
    const finalPrice = price - discount;
    return finalPrice;
}
// Introduction Function Create a function introduce that takes a name, age, and country. If age and country are not provided, they should default to "unknown".

function introduce(name, age = 'unknown', country = 'unknown'){
    return `my name is ${name}, I am ${age} years old, I am from ${country}`;
}

// Calculate Final Price Write a function calculate_price that takes the price of an item and a sales tax. The sales tax should default to 5%.

function calculatePrice(price, item, salesTax = 5) {
    const taxt = (price * salesTax) / 100;
    const Price1 = price - taxt;
    return Price1;
}

// Find the Maximum Create a function find_max that accepts three numbers and returns the largest one using comparison operators and if-else statements.

function find_max(num, num1, num2){
    

}


// Pass or Fail Write a function pass_or_fail that accepts a student's score and returns "Pass" if the score is 50 or above, and "Fail" otherwise.

function pass_or_fail(studentsScore){
    if(studentsScore > 50){
        return 'Pass';
    } 
    return 'Fail';
}

// Sum of Numbers Write a function sum_of_numbers that accepts a list of numbers and returns their sum using a for loop.

function sum_of_numbers(Numbers){
    let sum = 0;
    for(let i = 0; i < numbers.length; i++){
        sum += numbers[i];
    }
    return sum;
}

// Count Even Numbers Create a function count_evens that accepts a list of integers and returns the count of even numbers using a for loop.

function count_evens(Numbers){
    let count = 0;
    for(let i = 0; i < numbers.length; i++){
        if(numbers[i] % 2 === 0){
            count++;
        }
    }
    return count;

}