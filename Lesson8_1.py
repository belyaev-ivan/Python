class Date:
    def __init__(self, data):
        self.data = data

    @classmethod
    def one_metod(cls, data):
        my_date = [int(i) for i in data.split('-')]
        return my_date

    @staticmethod
    def two_metod(my_date):
        if my_date[0] >= 1 and my_date[0] <= 31:
            if my_date[1] >= 1 and my_date[1] <= 12:
                if my_date[2] >= 1 and my_date[2] <= 2020:
                    print(f'Текущая дата {my_date[0]} {my_date[1]} {my_date[2]}')
                else:
                    print('неверный формат года')
            else:
                print('неверный формат месяца')
        else:
            print('неверный формат дня')

    def my_date(self):
        self.two_metod(self.one_metod(self.data))


Date('12-12-2020').my_date()
Date('12-13-2020').my_date()
Date('32-13-2020').my_date()
Date('12-12-3020').my_date()








