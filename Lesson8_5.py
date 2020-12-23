class Scud_A:
    prihod = {}
    uhod = {}
    def revision(self):
        print('На текущий момент на складе находится:\n')
        for i in self.prihod.keys():
            print(*i, self.prihod[i], end='\n')


    def broadcast(self, param1, param2):
        self.uhod[param1] = f'{self.prihod[param1]} {param2}'
        del self.prihod[param1]
        print(f'Товар {param1} перешол со склада в {param2}')
        print('')




class office_equipment:
    param1 = 'название типа оргтехники'
    param2 = 'производитель'
    param3 = 'модель'
    param4 = 'дата производства'
    param5 = 'стоимость'

    def __init__(self, param1, param2, param3, param4, param5):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.param5 = param5

    def scud_up(self, quantity):
        Scud_A().prihod[f'{self.param1} {self.param2} {self.param3}'] = [f'\nколичество {quantity}' ,f'дата производства - {self.param4}',
                                                                    f'стоимость - {self.param5}']


class copy_machine(office_equipment):
    my_param1 = 'Возможнсть цветной печати'
    my_param2 = 'Разрешение (dpi)'
    my_param3 = 'Ёмкость фотобарабана'
    my_param4 = 'Формат используемой бумаги'

    def __init__(self, param1, param2, param3, param4, param5, my_param2, my_param3, my_param4, my_param1 = False):
        super().__init__(param1, param2, param3, param4, param5)
        self.my_param1 = my_param1
        self.my_param2 = my_param2
        self.my_param3 = my_param3
        self.my_param4 = my_param4

    def scud_up(self, quantity):
        Scud_A().prihod[f'{self.param1} {self.param2} {self.param3}'] = f'\nколичество {quantity}\n' \
                                                                   f'дата производства - {self.param4}\n' \
                                                                   f'стоимость - {self.param5}\n' \
                                                                   f'Возможнсть цветной печати - {self.my_param1}\n' \
                                                                   f'Разрешение (dpi) - {self.my_param2}\n' \
                                                                   f'Ёмкость фотобарабана - {self.my_param3}\n' \
                                                                   f'Формат используемой бумаги - {self.my_param4}\n'
        print(f'{self.param1} {self.param2} {self.param3}', Scud_A().prihod[f'{self.param1} {self.param2} {self.param3}'])



class scanner(office_equipment):
    my_param1 = 'Тип сканера (планшетный, протяжный, слайд-сканер)'
    my_param2 = 'Тип датчика (Contact Image Sensor - CIS, Charge-Coupled Device - CCD)'
    my_param3 = 'Разрешение'

    def __init__(self, param1, param2, param3, param4, param5, my_param1, my_param2, my_param3):
        super().__init__(param1, param2, param3, param4, param5)
        self.my_param1 = my_param1
        self.my_param2 = my_param2
        self.my_param3 = my_param3

    def scud_up(self, quantity):
        Scud_A().prihod[f'{self.param1} {self.param2} {self.param3}'] = f'\nколичество {quantity}\n' \
                                                                   f'дата производства - {self.param4}\n' \
                                                                   f'стоимость - {self.param5}\n' \
                                                                   f'Тип сканера  - {self.my_param1}\n' \
                                                                   f'Тип датчика - {self.my_param2}\n' \
                                                                   f'Разрешение - {self.my_param3}\n'
        print(f'{self.param1} {self.param2} {self.param3}', Scud_A().prihod[f'{self.param1} {self.param2} {self.param3}'])


class printer(office_equipment):
    my_param1 = 'Формат используемой бумаги'
    my_param2 = 'Разрешение (dpi)'
    my_param3 = 'Скорость печати принтера'
    my_param4 = 'Фотопечать'
    my_param5 = 'Технология устройства (Матричный, Струйный, Лазерный, МФУ, Сублимационный)'

    def __init__(self, param1, param2, param3, param4, param5, my_param1, my_param2, my_param3, my_param5,
                 my_param4 = False ):
        super().__init__(param1, param2, param3, param4, param5)
        self.my_param1 = my_param1
        self.my_param2 = my_param2
        self.my_param3 = my_param3
        self.my_param4 = my_param4
        self.my_param5 = my_param5

    def scud_up(self, quantity):
        Scud_A().prihod[f'{self.param1} {self.param2} {self.param3}'] = f'\nколичество {quantity}\n' \
                                                                   f'дата производства - {self.param4}\n' \
                                                                   f'стоимость - {self.param5}\n' \
                                                                   f'Формат используемой бумаги - {self.my_param1}\n' \
                                                                   f'Разрешение (dpi) - {self.my_param2}\n' \
                                                                   f'Скорость печати принтера - {self.my_param3}\n' \
                                                                   f'Фотопечать - {self.my_param4}\n' \
                                                                   f'Технология устройства (Матричный, Струйный, Лазерный, МФУ, Сублимационный) - {self.my_param5}\n'
        print(f'{self.param1} {self.param2} {self.param3}', Scud_A().prihod[f'{self.param1} {self.param2} {self.param3}'])

z = printer('Принтер', 'Pantum', 'P2200', '11.12.2019', 5000, 'A4', 20, 30, 'Лазерный', True)
z.scud_up(10)

x = scanner('Сканер', 'Pantum', 'S2200', '11.03.2008', 3000, 'планшетный', 'CCD', 10)
x.scud_up(20)
Scud_A().revision()
Scud_A().broadcast('Принтер Pantum P2200', '1 отдел')
Scud_A().revision()
