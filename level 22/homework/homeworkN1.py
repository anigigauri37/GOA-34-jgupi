
# 1 შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს

# semoatanine = int(input("Enter Number: "))

# def Number (semoatanine):
#     return semoatanine + 5 

# resoult = Number(semoatanine)
# print(resoult)



# 2. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს



# num1 = 105
# num2 = 205

# def integer(num1, num2):
#     return num1 * num2

# resoult = integer(num1, num2)
# print(resoult)



# 3. შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len())



# word = "ROBOTIC"

# def string(word):
#     return len(word)

# resoult = string("ROBOTIC")
# print(resoult)



# 4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).


# listN1 = ["TRASH"]

# stringN1 = ("COAL")

# def sigrze(listN1):
#     return len(listN1)

# resoult = sigrze("TRASH")
# print(resoult)

# def sigrze(stringN1):
#     return len(stringN1)

# resoult = sigrze("COAL")
# print(resoult)



# 5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome
# (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.


# def is_palindrome(s):
#     s = s.lower()
#     reversed_s = s[::-1]
#     return s == reversed_s



# print(is_palindrome("WOW")) 
# print(is_palindrome("CAR"))  
# print(is_palindrome("SUPERMAN"))  



# 6. შექმენით ფუნქცია, რომელიც პოულობს ყველაზე გრძელ string'ს string'ების სიაში.

# string1 = ["FLYING CAR"]
# string2 = ["DISCORD"]
# string3 = ["SPONGEBOB"]


# def biggest_string(string1):
#     return len(string1)

# def biggest_string(string2):
#     return len(string2)

# def biggest_string(string3):
#     return len(string3)

# resoult = biggest_string("FLYING CAR")
# print (resoult)
# resoult = biggest_string("DISCORD")
# print (resoult)
# resoult = biggest_string("SPONGEBOB")
# print (resoult)



# 7. შექმენით ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის factorial'ს (რა არის ფაქტორიალი: https://en.wikipedia.org/wiki/Factorial).



# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# print(factorial(100))



# 8. შექმენით ფუნქცია, რომელიც იღებს 2 integer'ების list'ს და აბრუნებს ორივე list'იდან მაქსიმალური რიცხვების ჯამს.



# def max_sums(list1, list2):
#     max_sums_list = []
#     for i in range(len(list1)):
#         max_sums_list.append(max(list1[i], list2[i]))
#     return max_sums_list

# list1 = [1, 5, 3, 8]
# list2 = [2, 4, 6, 7]
# result = max_sums(list1, list2)
# print(result)



# 9. შექმენით ფუნქცია, რომელიც იღებს 2 integer'ების list'ს და აბრუნებს ორივე list'იდან მინიმალური რიცხვების სხვაობას


# def difference_min_lists(list1, list2):
#     if not list1 or not list2:
#         return None 

#     min_list1 = min(list1)
#     min_list2 = min(list2)
#     difference = abs(min_list1 - min_list2)
#     return difference


# list1 = [5, 8, 2, 10]
# list2 = [3, 7, 1, 9]
# result = difference_min_lists(list1, list2)
# print(f"Difference between min values of lists: {result}")



# 10. შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს და აბრუნებს ამ სიაში მაქსიმალური და მინიმალური რიცხვების სხვაობას. make this work 



# def difference_max_min(numbers):
#     if not numbers:
#         return None 
    
#     max_num = max(numbers)
#     min_num = min(numbers)
#     difference = max_num - min_num
#     return difference


# numbers = [3, 9, 1, 7, 4, 2]
# result = difference_max_min(numbers)
# print(f"Difference between max and min: {result}") 
