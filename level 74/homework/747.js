// .appendChild(node),
const h1 = document.createElement("h1");

h1.textContent = "ani";
document.body.appendChild(h1);


// .createElement,
const div = document.querySelector("div")
const body = document.querySelector("text")

const ani = document.createElement("div");
id = "div"
body.append("id");


// .insertBefore,
const p = document.createElement("p");
p.textContent = "Hello";

const h1 = document.querySelector("h1");
document.body.insertBefore(p, h1);

// .removeChild(node),

const p = document.querySelector("p");
document.body.removeChild(p);


// .parentNode,

const p = document.querySelector("p");
console.log(p.parentNode);



// აუცილებელია ამ მეთოდების გამოყენებით შექმნილი ობიექტების
// ჩამატება რომელიმე ელემენტში რომ გახდნენ ხილვადები

// შექმნის მეთოდები
// document.createElement("Element") - ქმნის ელემენტს
// document.createTextNode(text) - ქმნის ტექტს
// element.cloneNode() - ქმნის ტექსტის კლონს

// ჩამატების მეთოდები
// Element.appendChild(node) - ელემენტში ამატებს სასურველ ობიექტს
// element.insertBefore(node1, node2) 

// parent.removeChild(node) - ელემენტის წაშლა
// child.parentNode - აბრუნებს შვილი ელემენტის მშობელს
// parent.replaceChild(node1, node2) - ანაცვლებს მშობელ ელემენტში მეორე ობიექტს ანაცვლებს პირველით