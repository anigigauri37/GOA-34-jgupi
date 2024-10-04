function filter(numbers){
    const Number = []
    for(let i = 0; i < numbers.length; i++){
        if(numbers[i] % 2 === 0){
            Number.push(numbers[i])
        }
    }
    return Number
}

console.log(filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))