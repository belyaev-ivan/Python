number = int(input('Введите количество товара, который нужно добавить в учет товаров '))
user_list = []


for n in range(number):
    name = input(f'Введите название {n + 1} товара ')
    price = int(input(f'Введите цену {n + 1} товара '))
    quantity = int(input(f'Введите количество {n + 1} товара '))
    ed = input(f'Введите единицу измерения {n + 1} товара ')
    user_list.append((n+1, {'название': name, 'цена': price, 'количество': quantity, 'eд': ed}))

print(user_list)

stat_name = []
stat_price = []
stat_quantity = []
stat_ed = []
for x in range(len(user_list)):
    stat_name.append(user_list[x][1]['название'])
    stat_price.append(user_list[x][1]['цена'])
    stat_quantity.append(user_list[x][1]['количество'])
    if len(stat_ed) == 0:
        stat_ed.append(user_list[x][1]['eд'])

    for i in range(len(stat_ed)):
        if stat_ed.count(stat_ed[i]) == 0:
            stat_ed.append(user_list[x][1]['eд'])
    x = x + 1

stat = {'название': stat_name,
        'цена': stat_price,
        'количество': stat_quantity,
        'eд': stat_ed
        }
print(stat)