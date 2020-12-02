def my_func(number_1, number_2, number_3):
    summ_number = []
    summ_number.append(number_1)
    summ_number.append(number_2)
    summ_number.append(number_3)
    summ_number.sort()
    print(summ_number[1]+summ_number[2])

my_func(int(input('Введите первое число')), int(input('Введите второе число')), int(input('Введите третье число')))