input_user = input('Введите строку')
user_list = input_user.split()
for i in range(len(user_list)):
    user_str = str(user_list[i])
    if len(user_str) > 10:
        user_str = user_str[:10]
    print(f'{i + 1} {user_str}')