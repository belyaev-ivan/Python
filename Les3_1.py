def my_func (number_1, number_2):
    if number_2 == 0:
        print('На ноль делить нельзя')
    else:
        return number_1/number_2
print(my_func(int(input('Введите число')), int(input('Введите делитель'))))