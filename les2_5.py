my_list = [7, 5, 3, 3, 2]
user_input = int(input("Введите новое значение"))

for i in range(len(my_list)):
    if my_list[i] <= user_input:
        my_list.insert(i, user_input)
        break
else:
    my_list.append(user_input)
print(my_list)