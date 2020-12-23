class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __add__(self, other):
        print(f'Сумма равна')
        return f'число = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение равно')
        return f'число = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'число = {self.a} + {self.b} * i'


x = Complex_number(2, 4)
y = Complex_number(5, 2)

print(x + y)
print(x * y)