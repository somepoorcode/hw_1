n = int(input("Введите натуральное число: "))
max_width = n * 3

for i in range(1, n + 1):
    numbers = ''.join(str(j) for j in range(1, i + 1))
    spaces = " " * (max_width - len(numbers))

    print(f"{spaces}{numbers}{numbers[::-1][1:]}")