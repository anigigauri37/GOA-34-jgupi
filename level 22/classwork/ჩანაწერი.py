# def calculate_average():
#     numbers = [135, 177, 188, 163, 150]  
#     average = sum(numbers) / len(numbers)
#     return average

# print(calculate_average())




# def print_numbers():
#     for i in range(10):
#         print(i + 5)


# print_numbers()

# print_numbers()

# def print_numbers(start, end):
#     for i in range(start, end):
#         print(i)
#     print("end")

# print_numbers(5, 10)
# print_numbers(10, 12)

# input(name = "andria")

# def greet(name = "Guest"):
#     print("Welcome", name)


# greet('Andria')
# greet('Gio')
# greet('Erekle')
# greet()


# def manual_sum(numbers):
#     output = 0
#     for number in numbers:
#         output += number
#     return output

# age = [15, 13, 12, 28]
# output = manual_sum(age)
# print(output)

# def Make_sandwich(ingredients):
#     print("Open bread")
#     print(ingredients)
#     print("End Break")
    
#     return "sandwich"

# Make_sandwich(["Tomato", "Cucumber,", "Potato"])



# def Make_sandwich():
#     return"sandwich"

# my_order = Make_sandwich()

# print(my_order)


# def manual_sum(numbers_list):
#     sum = 0

#     for num in numbers_list:
#          sum = sum +num

#          return sum
    
# print (manual_sum([1,2,3,]))



# def manual_max(num1, num2):
#     if num1 > num2:
#         return num1
#     elif num1 < num2:
#         return num2
#     else:
#         return "Both numbers Are equal"
    

# print(manual_max(8,5))


# def filter_list(number_list):
#     for num in number_list:
#         if num % 2 == 0:
#             print("Even:", num)
#         else:print("Odd:", num)


# filter_list([1,2,3,4,5,6,7,8,9,10])

##################################################################################################################################################################################


# def print_even_numbers(n):
#     for i in range(2, n +1):
#         if i % 2 == 0:
#             print(i)

# print_even_numbers(10)


# def find_maximum(num1, num2):
#     return max(num1, num2)

# result = find_maximum(50, 30)
# print(result)  



# def reverse_string(s):
#     return s[::-1]


# result = reverse_string("Hello Andria")
# print(result) 

# def rectangle_area(length, width):
#     return length * width


# result = rectangle_area(15, 25)
# print(result)  


# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# result = is_prime(17)
# print(result) 



# def sum_of_numbers(numbers):
#     return sum(numbers)


# result = sum_of_numbers([11, 20, 19, 14, 7])
# print(result) 


# def to_uppercase(strings):
#     return [s.upper() for s in strings]


# result = to_uppercase(["hello", "world"])
# print(result)  


def count_xmovnebi(s):
    xmovnebi = "aeiou"
    count = sum(1 for char in s if char in xmovnebi)
    return count


result = count_xmovnebi("a e i o u")
print(result)  
