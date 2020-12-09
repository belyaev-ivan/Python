from itertools import count, cycle
x = int(input('Введите число, с которого начнется цикл'))

for i in count(x):
    print(i, end = '')
    end = input()
    if end == 'q':
        break

my_list = input('Введите элементы списка').split()
for i in cycle(my_list):
    print(i, end = '')
    end = input()
    if end == 'q':
        break