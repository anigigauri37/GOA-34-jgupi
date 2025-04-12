setInterval(function() {
    console.log("5 second passed")

}, 2000);



setInterval(function() {
    const date = new Date();
    console.log(date.toUTCString())

}, 2000);



let userTime = 10;

setInterval(function() {
    userTime--;
    console.log(userTime, "left");
    if(userTime === 0){
        console.log("time is up")
    }

}, 2000);



// minisebshi agar gadadis
let Time = 10;

const h = setInterval(function() {
    Time--;
    console.log(Time, "left");
    if(Time === 0){
        clearInterval(h);
        console.log("time is up")
    }

}, 2000);


// emateba
let useTime = 10;

const t = setInterval(function() {
    useTime++
    console.log(useTime, "left");
    if(useTime === 0){
        clearInterval(t);
        console.log("time is up")
    }

}, 2000);

