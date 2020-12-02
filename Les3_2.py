def my_func_v1  (name, surname, year, city, email, phone_number):
    return f'Меня зовут {name} {surname}, я родился {year} и живу в городе {city}, мой почтовый ящик {email}, ' \
           f'мой номер телефона {phone_number}.'

print(my_func_v1(name=input("Укажите свое имя "), surname=input("Укажите свою фамилию "),
                 year=input("Укажите дату вашего рождения "),
                 city=input("Укажите горд, в котором вы живете "), email=input("Укажите адрес ващей электронной почты "),
                 phone_number=input("Введите номер вашего телефона ")))

def my_func_v2 ():
    name = input("Укажите свое имя ")
    surname = input("Укажите свою фамилию ")
    year = input("Укажите дату вашего рождения ")
    city = input("Укажите горд, в котором вы живете ")
    email = input("Укажите адрес ващей электронной почты ")
    phone_number = input("Введите номер вашего телефона ")
    print(f'Меня зовут {name} {surname}, я родился {year} и живу в городе {city}, мой почтовый ящик {email}, '
          f'мой номер телефона {phone_number}.')

my_func_v2()
