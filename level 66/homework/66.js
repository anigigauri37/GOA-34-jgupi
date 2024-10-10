// შექმენი ფუნქცია, რომელიც მიიღებს რიცხვს და პირობით შეამოწმებს, არის თუ არა ის კენტი ან ლუწი.

function text(number) {
    if (number % 2 === 0) {
        return "Even";
    } else {
        return "Odd";
    }
}

// შექმენი პირობა, რომელიც შეამოწმებს, არის თუ არა სია ცარიელი და თუ არა, იპოვოს რიცხვების ჯამი.

function sumOfNumbers(numbers) {
    if (numbers.length === 0) {
        return 0;
    } else {
        return numbers.reduce((accumulator, current) => accumulator + current, 0); 
    }
}

// შექმენი ფუნქცია, რომელიც მიიღებს რიცხვების სიას, გაამრავლებს ყველა რიცხვს 3-ზე და დაიბრუნებს მხოლოდ იმ რიცხვებს, რომლებიც 20-ზე მეტია.

function filterNumbers(numbers) {
    return numbers
        .map(num => num * 3)
        .filter(num => num > 20);
}

// შექმენი პირობა, რომელიც შეამოწმებს სიაში უდიდეს რიცხვს და დააბრუნებს მას.




// დაწერე ფუნქცია, რომელიც მიიღებს ორ რიცხვს და პირობით შეამოწმებს, თუ მათი ნამრავლი 100-ზე მეტია.

function text(num1, num2){
    if(num1 + num2 > 100){
        return "Their sum is greater than 100";
    } else {
        return "Their sum is less than or equal to 100";
    }
}

// შექმენი ფუნქცია, რომელიც მიიღებს ტექსტს და შეამოწმებს, თუ ტექსტის პირველ და ბოლო ასოები ერთნაირია.

function isPalindrome(text){
    const reversedText = text.split('').reverse().join('');
    return text === reversedText;
}


// შექმენი ფუნქცია, რომელიც მიიღებს ტექსტს და დააბრუნებს თითოეული ასოს სიხშირეს, ანუ რამდენჯერ გვხვდება თითოეული ასო ტექსტში.

function countOccurrences(text, char){
    let count = 0;
    for(let i = 0; i < text.length; i++){
        if(text[i] === char){
            count++;
        }
    }
    return count;
}

// შექმენი ფუნქცია, რომელიც მიიღებს ტექსტს და შეამოწმებს, არის თუ არა ის პალინდრომი (ტექსტი, რომელიც წაკითხვისას ერთნაირად ჩანს როგორც წინ და უკან,

