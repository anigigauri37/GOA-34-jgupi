const p = document.getElementById("t-text")
let time = 10;

setInterval(function(){
    p.textContent = time
    time--;
    console.log(time)
    if(time < 0){
        p.textContent = "Time's up!"
    }

}, 100)

console.log(t)

