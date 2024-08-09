
# def Vending_Machine(product):
#     count = 1
#     for product in product:
#         print(count, product)
#         count = count + 1
#     choose = int(input("Prease Choise Product: "))
#     money = int(input("Please Enter Money : "))

#     if choose == 1 and money >= 2:
#         return "Cola"
#     elif choose == 3 and money >= 3:
#         return "Chips"
#     elif choose == 3 and money >= 4.5:
#         return "Sniggers"
#     else:
#         return "Invalid Option Or Not Enough Money" 
# print (Vending_Machine(["Cola 2.00", "Chips 3.00", "Sniggers 4.50"]))

# def add(num1, num2):
#     return num1 + num2

# resoult = add(500, 300)
# print(resoult)


# def print_products(products):
#     count = 1
#     for product in products:
#         print(count, product)
#         count = count + 1

# def get_product(choice, products):
#     return products[choice]

# def check_products(choice, products):
#     choice = choice - 1
#     if choice >= 0 and choice < len(products):
#         return choice

# def vending_machine(products):
#     print_products(products)

#     choice = int(input("Please enter choice: "))

#     choice = check_products(choice, products)

#     result = get_product(choice, products)

#     return result


# print(vending_machine(["Cola 2.00", "Borjomi 5.00", "Snickers 3.00", "Pomidori"]))



# def calculator(num1, num2):
#     print("1. +")
#     print("1. -")
#     print("1. *")
#     print("1. /")
#     choise = int(input("pleace Enter Your Choise"))
#     resoult = 0
#     if choise == 1:
#         resoult = num1 + num2
#     elif choise == 2:
#         resoult = num1 - num2 
#     elif choise == 3:
#         resoult = num1 * num2 
#     elif choise == 4:
#         resoult = num1 * num2
#     else:
#         print("Invalid Choise")
#     return resoult 
# print(calculator(5,10))