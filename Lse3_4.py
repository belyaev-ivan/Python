def my_func_v1(x, y):
    if x <= 0:
        return print('Переменная х должна принимать положительное число')
    elif y >= 0:
        return print('Переменная у должна принимать отрицательное число')
    elif y != int(y):
        return print('Переменная у должна принимать целое число')
    else:
        return x ** y


def my_func_v2(x, y):
    if x <= 0:
        return print('Переменная х должна принимать положительное число')
    elif y >= 0:
        return print('Переменная у должна принимать отрицательное число')
    elif y != int(y):
        return print('Переменная у должна принимать целое число')
    else:
        z = -1
        x1 = x
        while z != y:
            z -= 1
            x = x1 * x
        return 1 / x


print(my_func_v1(int(input('Введите число')), int(input('Введите степень, в которую будет возведено число'))))
print(my_func_v2(int(input('Введите число')), int(input('Введите степень, в которую будет возведено число'))))
