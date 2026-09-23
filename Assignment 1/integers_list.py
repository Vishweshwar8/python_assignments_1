numbers = []

for i in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)

total = 0

for num in numbers:
    total = total + num

average = total / 10

print("Sum:", total)
print("Average:", average)
