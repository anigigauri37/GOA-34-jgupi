start = int(input("Please enter start number: "))

end = int(input("Please enter end number: "))


numbers = []

for i in range(start, end):
    numbers.append(i)



print(sum(numbers))
print(max(numbers))
print(min(numbers))

print(numbers)