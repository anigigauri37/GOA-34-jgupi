const div = document.querySelector("div");
div.innerHTML += `
<p>hello</p>
<button>click me</button>
<button>submit</button>
<h1>gamarjoba</h1>

`

// შექმენით დაულაგებელი სია პროგრამირების ენების შესახებ და ნასწავლი მეთოდების: document.createElement() და document.appendChild() საშვალებით ჩაამატეთ სიის ელემენტები, რომლებშიც ეწერება სხვადასხვა პროგრამირების ენის სახელი

const list1 = ["p", "button", "button", "h1"];
const List = document.createElement("ul");

elements.forEach(element => {
    const listItem = document.createElement("li");
    const textNode = document.createTextNode(element);
    listItem.appendChild(textNode);
    elementsList.appendChild(listItem);
});


// შექმენით ფორმა რომელშიც მომხმარებელს შემოატანინებთ სახელს, გვარსა და ემაილს. შემდეგ ეს მონაცემები დაამატეთ ცხრილში ნასწავლი მეთოდების საშვალებით, ასევე დაამატეთ წაშლის ფუნქცია ცხრილში ელემენტზე დაჭერისას

const nameInput = document.createElement("nameInput");
const lastNameInput = document.createElement("lastNameInput");
const emailInput = document.createElement("emailInput");

