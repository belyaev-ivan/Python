def my_func(text):
    new_list = list(text)
    x = str(new_list[0]).upper()
    new_list.pop(0)
    new_list.insert(0, x)
    return ''.join(new_list)

def my_func_2():
    user_input = input('Введите строку')
    user_list = user_input.split(' ')
    result = []
    for i in user_list:
        result.append(my_func(i))
        my_func(i)
    result = ' '.join(result)
    print(result)

my_func_2()