n = int(input("Введите натуральное число: "))

for i in range(2, n + 2):
    print(*range(1, i), sep="")