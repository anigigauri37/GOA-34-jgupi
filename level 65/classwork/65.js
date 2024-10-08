// შექმენით 20 წყვილი ცვლადი და შინახეთ მათ შიგნით true და false data types სხვადასხვა გზით და გამოიტანთ ეკრაზე მათი შედარება "და" და "ან" ლოგიკუ ოპერატორებით
// 1
let a = true
let b = 10 < 20

console.log(a && b)
// true

// 2
let c = true
let d = 10 > 20

console.log(c || d)
// false

// 3
let w = false
let n = 542 == 10

console.log(w || n)
// false

// 4
let k = 120 > 78 
let r = true

console.log(k && r)
// true

// 5
let p = 500 < 500
let t = false

console.log(p || t)
// false

// 6

let x = 10
let y = 20

console.log(x == y)
// false

// 7

let v = false
let z = 10* 10 < 20

console.log(v === z)
// true

// 8

let m = 10
let l = "10"

console.log(m == l)
// true

// 9

let g = true
let h = 35 < 78

console.log(g === h)
// true

// 10

let u = 10
let j = 20

console.log(u != j)
// true

// 11

let f = false
let e = 10 / 2 > 20

console.log(f !== e)
// false

// 12

let o = 10
let q = 25

console.log(o !== q)
// true

// 13

let s = 10
let hs = 10

console.log(s === hs)
// true

// 14

let le = 25 * 14 < 137
let ot = true

console.log(le && ot)
// false

// 15

let gr = 25 * 14 > 137
let yu = false

console.log(gr || yu)
// true

// 16

let al = 100 * 2 == 137
let po = false

console.log(al || po)
// false

// 17

let re = 100 * 2 / 3 > 134
let yu2 = true

console.log(re === yu2)
// false

// 18

let jk = 13 * 58 / 7 < 348
let asd = false

console.log(jk && asd)
// false

// 19

let df = 13 * 58 / 7 > 348
let gfg = true

console.log(df || gfg)
// true

// 20

let be = 14 * 30
let etfe = false

console.log(be && etfe)
// false


// 2) შექმენით ათი წყვილი ცვლადი და და თითოს მიანიჭეთ "მოსწორო" და "მოარასწორო" მნიშვენლობა. შემდეგ ლოგიკური ოპერატორების გამო

// 1
let je = 5
let vgv = "78"

console.log(je || vgv)
// 5

// 2

let yu3 = "true"
let er = 20

console.log(yu3 && er)
// 20

// 3

let dd = 0
let ke = "hello"

console.log(dd || ke)
// hello

// 4

let qwe = "false"
let rty = 10

console.log(qwe && rty)
// 10

// 5

let uio = 15
let jkl = "15"

console.log(uio || jkl)
// 15

// 6

let asdf = "hello"
let zxcv = "0"

console.log(asdf && zxcv)
// 0

// 7

let gfh = "true"
let hjkl = 15

console.log(gfh || hjkl)
// true

// 8

let cvbn = 15
let mnb = "15"

console.log(cvbn && mnb)
// 15

// 9

let tgb = "hello"
let yhn = 26

console.log(tgb && yhn)
// 26

// 10

let qwer = "ancho"
let tyu = 10

console.log(qwer || tyu)
// ancho


// 3) გამოიყენეთ უკვე ნასწავლი მასალა და შეინახეთ ცვლადებში (სხვადასხვა გზით) true და false მნიშვნელობები. შემდეგ შეაბრუნეთ.

console.log(!true)
console.log(!false)

// 1

let hahx = 10 < 54
console.log(!false)

// 2

let anx = 87 == 14
console.log(!true)

// 3

let ad = 12 * 7 / 4 < 7
console.log(!true)


// 4

let qer = 20 < 14
console.log(!false)

// 5

let rbd = 48 < 78
console.log(!false)

// 1

// let year = prompt('In which year was the ECMAScript-2015 specification published?', '');

// if (year == 2015) {
//   alert( 'You guessed it right!' );
// } else {
//   alert( 'How can you be so wrong?' ); // any value except 2015
// }



// // 2
// let accessAllowed;
// let age = prompt('How old are you?', '');

// if (age > 18) {
//   accessAllowed = true;
// } else {
//   accessAllowed = false;
// }

// alert(accessAllowed);

// // 3
// let age = prompt('age?', 18);

// let message = (age < 3) ? 'Hi, baby!' :
//   (age < 18) ? 'Hello!' :
//   (age < 100) ? 'Greetings!' :
//   'What an unusual age!';

// alert( message );


// "და" - "&&" // "ან" - "||" // "NOT" - "!"