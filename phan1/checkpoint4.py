numbers = [5, 1, 8, 92, 7, 30]
b = []
a = 0
while a < len(numbers):
    if numbers[a] % 2 == 0:
        b.append(numbers[a])
    a += 1

# In ra các số chẵn
print("Even numbers:", end=" ")
for num in b:
    print(num, end=" ")
