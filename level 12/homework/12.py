#გამოიტანეთ რიცხვები 0-დან 20-ის ჩათვლით 

for i in range(0,21):
    print(i)

#მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ შემოტანილი რიცხვი ლუწია თუ არა თუ ლუწია დაუპრინტეთ "Number is even" 

while True:
    user_input = input("Enter a number : ")
    

    if user_input.isdigit():
        number = int(user_input)
        if number % 2 != 0:
            print("Number is odd")
        else:
            print("Number is even")
    else:
        print("Invalid input. Please enter a valid number.")

#დაპრინტეთ 20-მდე ლუწი რიცხვები

for i in range(22):
    if i % 2 == 0:
        print(i)

#50-იდან 100-ის ჩათვლით არსებული ყველა რიცხვი დააჯამეთ for ციკლის გამოყენებით. ეს ჯამი უნდა შეინახოს ცვლადში, ამიტომ ციკლის გარეთ შექმენით sum ცვლადი (sum-ჯამი)

sum = 0
for i in range(50 , 100):
    print("1 + ", i, "=", 1 + i)

#დაწერეთ ალგორითმი რომელიც ბეჭდავს 5-ის ჯერად რიცხვებს (რიცხვები რომლებიც იყოფა 5-ზე) 1-დან 50-ის ჩათვლით

for i in range(50, 101):
    if i % 5 == 0:
      print(i)

#დაწერეთ ალგორითმი, რომელიც დაბეჭდავს 5-იდან ათის ჩათვლით რიცხვების ნამრავლს for loop-ის გამოყენებით.

for i in range(5,11):
     print(i)

#BOSS: For loop დახმარებით ეცადეთ, რომ სიტყვა დაპრინტოთ საპირისპირო მიმართულებით (შეიძლება არ გამოგივიდეთ მაგრამ სცადეთ)

word = input("Enter Your Name : ")

length = len(word)

for i in range(length - 1, -1, -1):
    print(word[i], end="")

print()