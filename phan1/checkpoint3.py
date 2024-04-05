numbers = [5, 1, 8, 92, -1, 30]

input_number = int(input("Input a number: "))

if input_number in numbers:
    position = numbers.index(input_number) + 1
    print(f"Number found at position {position}")
else:
    print("Number not found")
tinh = sum(numbers)
print("Sum of all numbers:", tinh)
#bai3
numbers = []

print("Input the list of numbers.Enter 0 to finish.")

while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

print("Sum of numbers in list:", tinh)

