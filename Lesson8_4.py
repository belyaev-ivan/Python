class Scud_A:
    pass

class office_equipment:
    param1 = 'габариты'
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

class copy_machine(office_equipment):
    my_param1 = 'Возможнсть цветной печати'
    my_param2 = 'Разрешение (dpi)'
    my_param3 = 'Ёмкость фотобарабана'
    my_param4 = 'Формат бумаги'

    def __init__(self,param1, param2, param3, param4, param5, my_param1, my_param2, my_param3, my_param4):
        super().__init__(param1, param2, param3, param4, param5)
        self.my_param1 = my_param1
        self.my_param2 = my_param2
        self.my_param3 = my_param3
        self.my_param4 = my_param4



class scanner(office_equipment):

    my_param1 = 'Тип сканера (планшетный, протяжный, слайд-сканер)'
    my_param2 = 'Тип датчика (Contact Image Sensor - CIS, Charge-Coupled Device - CCD)'
    my_param3 = 'Разрешение'

    def __init__(self,param1, param2, param3, param4, param5, my_param1, my_param2, my_param3):
        super().__init__(param1, param2, param3, param4, param5)
        self.my_param1 = my_param1
        self.my_param2 = my_param2
        self.my_param3 = my_param3


class printer(office_equipment):
    my_param1 = 'Формат бумаги'
    my_param2 = 'Разрешение (dpi)'
    my_param3 = 'Скорость печати принтера'
    my_param4 = 'Фотопечать'
    my_param5 = 'технология устройства (Матричный, Струйный, Лазерный, МФУ, Сублимационный)'

    def __init__(self,param1, param2, param3, param4, param5, my_param1, my_param2, my_param3, my_param4, my_param5):
        super().__init__(param1, param2, param3, param4, param5)
        self.my_param1 = my_param1
        self.my_param2 = my_param2
        self.my_param3 = my_param3
        self.my_param4 = my_param4
        self.my_param5 = my_param5


z = printer('Принтер', 'Pantum', 'P2200', '11.12.2019', 5000, 'A4', 20, 30, 'Лазерный', True)
