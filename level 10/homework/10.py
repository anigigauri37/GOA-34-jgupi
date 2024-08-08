#)0-იდან 20-ის ჩათვლით დაპრინტეთ ყველა მთელი რიცხვი

for i in range(0, 21):
    print(i)

#დაპრინტეთ პირველი 10 ნატურალური რიცხვი 

for i in range(11):
    print(i)

#დაპტინტეთ 0-იდან 100-ის ჩათვლით ლუწი რიცხვები

for i in range(102):
    if i % 2 == 0:
        print(i)

#შემოატანინეთ მომხმარებელს რიცხვი და დაადგინეთ არის თუ არა დადებითი უარყოფითი ან ნულის ტოლ

num = int(input("shemoitanet ricxvi"))
if num < 0:
    print("uaryofiti")
elif num == 0:
    print("tolia nulis")
else:
    print("dadebitia")


#შემოატანინეთ მომხმარებელს მისი ასაკი თუ მისი ასაკი 18 წელზე მეტია დაუპრინტეთ “you are adult” თუ 18 წელზე ნაკლები “you are virgin”

age = int(input("shemoitanet asaki"))
num2 = 18

while age == num2:
    print("you are adult")
    break
else:
    print("you are virgin")

#დაწერეთ ისეთი პროგრამა რომელიც მომხმარებელს უპრინტავს კვირის დღეს მომხმარებლის შემოტანილი რიცხვის მიხედვით

num = int(input('enter your number: '))
if num == 1:
    print('orshabati')

elif num == 2:
    print("samshabati")

if num == 3:
    print("orxshabati")

elif num == 4:
    print("xutshabati")

if num == 5:
    print("paraskevi")

elif num == 6:
    print("shabati")

if num == 7:
    print("kvira")