from math import factorial
num = int(input("Введите число"))

def gen (num):
    for i in range(1, num + 1):
        yield f'Факториал числа {i} равен {factorial(i)}'

for x in gen(num):
    print(x)
