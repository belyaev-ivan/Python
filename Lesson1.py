# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько
# чисел и строк и сохраните в переменные, выведите на экран.
def level_One():
    One_object_str = "Hello World"
    Two_object_str = 'My name is Ivan'
    One_object_int = 2020
    One_object_float = 23.11
    One_object_tuple = (1, 2, 3)
    One_object_list = [1, "1", 2.4]
    One_object_dict = {
        'str': 'Hello World',
        'int': 1,
        'float': 1.0,
        'tuple': (1, 2, 3),
        'list': [1, "1", 2.4]
    }

    print(One_object_str, type(One_object_str))
    print(Two_object_str, type(Two_object_str))
    print(One_object_int, type(One_object_int))
    print(One_object_float, type(One_object_float))
    print(One_object_tuple, type(One_object_tuple))
    print(One_object_list, type(One_object_list))
    print(One_object_dict, type(One_object_dict))

    one_int_number = int(input('Введите целое число'))
    two_float_number = float(input('Введите дробное число'))
    three_str = str(input('Введите строку'))
    print(f'Вы ввели числа {one_int_number} и {two_float_number}, сумма которых равна {one_int_number + two_float_number},'
          f' а также строку "{three_str}"')
# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
def level_Two():
    Time = int(input('Введите количество секунд'))
    Time_hour = Time // 3600
    Time_minute = (Time % 3600) // 60
    Time_second = (Time % 60)
    if Time_hour == 1:
        Time_hour_str = "часу"
    else:
        Time_hour_str = "часам"

    if Time_minute == 1:
        Time_minute_str = "минуте"
    else:
        Time_minute_str = "минут"

    if Time_second == 1:
        Time_second_str = "секунде"
    else:
        Time_second_str = "секундам"
    print(f'Введеное количество секунд равно {Time_hour} {Time_hour_str}, {Time_minute} {Time_minute_str}, '
          f'{Time_second} {Time_second_str}')

    if Time_hour < 10:
        Time_hour_int = 0
    else:
        Time_hour_int = ""

    if Time_minute < 10:
        Time_minute_int = 0
    else:
        Time_minute_int = ""

    if Time_second < 10:
        Time_second_int = 0
    else:
        Time_second_int = ""
    print(f'Введеное количество секунд равно {Time_hour_int}{Time_hour}:{Time_minute_int}{Time_minute}:'
          f'{Time_second_int}{Time_second}')
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
def level_Three():
    number = input("Введите число")
    number_one = int(number)
    number_two = int(number + number)
    number_three = int(number + number + number)
    result = number_one + number_two + number_three
    print(result)
# 4. Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические операции.
def level_Four():
    number = int(input("Введите число"))
    if number >= 0:
        number = str(number)
        print(max(number))


        number = list(number)
        while not len(number) == 1:
            if number[0] > number[1]:
                number.pop(1)
            elif number[0] < number[1]:
                number.pop(0)
            elif number[0] == number[1]:
                number.pop(0)
        print(number[0])
    else:
        print("Введите положительное число!!!")

    number = int(input("Введите число"))
    Ost = number % 10
    Len = number // 10

    while Len > 0:
        if Ost < Len % 10:
            Ost = Len % 10
        Len = Len // 10
    print(Ost)
# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.
def level_Five():
    income = int(input("Введите сумму доходов "))
    expenditure = int(input("Введите сумму расходов "))
    if income > expenditure:
        print("Фирма работает с положительным финансовым результатом")
        print(f'Прибыль составляет {income - expenditure}')
        populate_employee = int(input("Введите количество сотрудников, работающих в компании "))
        print(f'Прибыль компании на одного сотрудника составляет {(income - expenditure)/populate_employee}')
    else:
        print("Фирма работает с отрицательным финансовым результатом")
        print(f'Убыток составляет {expenditure - income}')
# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.
def level_Six():
    one_result = int(input("Введите количество киллометров, которое вы можете пробежать на данном этапе"))
    end_result = int(input("Введите количество киллометров, которое вы хотите пробегать после занятий по нашей "
                             "специальной программе"))
    i = 1
    print(f'{i}-й День : {one_result}')
    while not one_result >= end_result:
        i += 1
        one_result = one_result * 1.1
        print(f'{i}-й День : {one_result}')
    else:
        print(f'Вы достигните результата в {end_result} киллометров на {i} день')

