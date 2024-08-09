# inputs = input("Enter Your Name: ")

# capitalized_name = inputs.capitalize()
# print(capitalized_name)

#lower ფუნქცია აპატარავებს სტრინგში დიდ ასოებს
#counr ფუნქცია ითვლის ასოებს ერთ წინადადებაში (რომელიც ჩვენ მოგვესურვება)
# capitalize ადიდებს სთრინგის პირველ ასოს
# upper ადიდებს სთრინგის ყველა ასო
#index არის ფუნქცია რომელიც გვიბრონებს ინტეგერს და პასუხში არის გადმოცემული რა ასოსაც მიუთითებთ იმისი index ანუ (ადგილი)
#find არის ფუნქცია რომელიც გვიბრონებს ინტეგერს და პასუხში არის გადმოცემული რა ასოსაც მიუთითებთ იმისი index ანუ (ადგილი) find და index ის განსხვავებაა რომ თუ ისეთი აო ნა სითყვა რომელიც str  არ მოიძებნა find ფუნქცია დააბრუნებს(-1) და index (error)

# sentence = "My Name Is andria, and I am JR.Programmist."

# occurs = sentence.index("m")
# print (occurs)


# sentence = "My Name Is andria, and I am JR.Programmist."

# occurs = sentence.index("m")
# print (occurs)


emails = []

count = int(input("Please Enter How Many Emails Do You Wanna Enter: "))

for i in range(count):
    email = input("Pleace Enter Email: ")

    if email.endswith("@gmail.com"):
        emails.append(email)
        print("Email Was Correct!")
    else:
        print("Invalid Email")
print(emails)