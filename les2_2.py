len_list = int(input('Введите коичество элементов в списке'))
list = []
x = 0
while not x == len_list:
    x += 1
    element_list = input(f'Введите {x} элемент')
    list.append(element_list)


for i in range(len(list)):
    if i % 2 == 1:
        list[i], list[i - 1] = list[i - 1], list[i]

print(list)