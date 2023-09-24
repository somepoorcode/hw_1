a, b, c = map(int, input("Введите три числа через пробел: ").split())

if a == b == c:
    print("3")
elif a != b != c:
    print("0")
else:
    print("2")