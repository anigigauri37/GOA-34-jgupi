#გამოიყენეთ ყველა კონვერტაციის ფუნქცია და გააკეთეთ თითოეულზე 5-5 მაგალითი, 

num  = 10
str_num = str(num)
print("10" + "20")

num  = 10
str_num = str(num)
print("10" + "10")

num  = 10
str_num = str(num)
print("100" + "2")

num  = 10
str_num = str(num)
print("55" + "35")

num  = 10
str_num = str(num)
print("10" + "20")

#შექმენით პროგრამა სადაც მომხმარებელი შემოიტანს 5 რციხვს, ხოლო ამ 5 რიცხვს შორის გამოიყენეთ ყველა არითმეტიკული ოპერაცია 

num = 42
str_num = str(num)
def getnumbers():
    numbers = []
    for i in range(5):
        number = int(input(f"shemoitanet ricxvi {i + 1}: "))
        numbers.append(number)
    return numbers


def performoperations(numbers):

    sumresult = sum(numbers)
    prodresult = 1
    for num in numbers:
        prod_result *= num


    floor_div_result = numbers[0] // numbers[1] 
    mod_result = numbers[0] % numbers[1] 


    print(f"რიცხვების ჯამი: {sum_result}")
    print(f"რიცხვების ნამრავლი: {prod_result}")
    print(f"{numbers[0]} // {numbers[1]} = {floor_div_result}")
    print(f"{numbers[0]} % {numbers[1]} = {mod_result}")

def main():
    numbers = get_numbers() 
    perform_operations(numbers)

if "name" == "main":
    main()
