// შექმენით ფუნქცია, რომელიც გამოიტანს მესიჯს სამი წამის შემდეგ
setInterval(function(){
    console.log("3 second passed")
}, 3000)

// შექმენით პროგრამა, რომელიც ყოველ წამს გამოიტანს ამჟამინდელ დროს "საათი:წუთი:წამი"

setInterval(function() {
    const date = new Date();
    console.log(date.toUTCString())

}, 1000);

//  შექმენით პროგრამა, რომელიც ყოველ 3 წამში შეცვლის საიტის background ფონის ფერს.

setInterval(function() {
    document.body.style.backgroundColor = getRandomColor();
}, 3000);


// შექმენით პროგრამა ტაიმერი, რომელსაც გადასცემთ 3 ღილაკს Start,Pause,Reset

const p = document.getElementById("t-text")

let time = 0;

const StartBUT = document.getElementById("1")
const PauseBUT = document.getElementById("2")
const ResetBUT = document.getElementById("3")



StartBUT.addEventListener("click", function() {
    if(!interval === null){
        interval = setInterval(function(){
            time++;
            p.textContent = time
        }, 1000)
    }
    setInterval(function(){
        time++;
        p.textContent = time
    }, 1000)
})

PauseBUT.addEventListener("click", function(){
    clearInterval(interval)
    interval = null
})

ResetBUT.addEventListener("click", function() {
    time = 0;
})