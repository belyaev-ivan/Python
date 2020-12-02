def my_func():
    user_input_str = input('Введите строку чисел, разделенных пробелом')
    a = 0
    if user_input_str != '*':
        while user_input_str != f'{a} *':

            if user_input_str != '*':
                list_number = user_input_str.split(' ')

                for i in range(len(list_number)):
                    a = a + int(list_number[i])

                print(a)
            user_input_str = input('Введите строку чисел, разделенных пробелом')

my_func()