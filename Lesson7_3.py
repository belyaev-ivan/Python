class Cell:
    def __init__(self, param_cell):
        self.param_cell = int(param_cell)

    def __add__(self, other):
        return f'Произошло слияние двух клеток, размер новой клетки равен {self.param_cell + other.param_cell}'

    def __sub__(self, other):
        return f'На клетку напали и она потеряла частичку себя, ' \
               f'размер новой клетки равен {self.param_cell - other.param_cell}' if self.param_cell - other.param_cell > 0 \
                else 'Клетка уничтожена'

    def __mul__(self, other):
        return f'Произошол скачок роста клетки, размер новой клетки равен {self.param_cell * other.param_cell}'

    def __truediv__(self, other):
        return f'Произошло деление клетки на {other.param_cell} частей' \
               f', размер новой клетки равен {self.param_cell / other.param_cell}'

    def make_order(self, param):
        x = 0
        while x + param <= int(self.param_cell):
            x += param
            print('*' * param)
        else:
            print('*' * (int(self.param_cell) - x))





cell1 = Cell(16)
param = Cell(20)

print(cell1 - param)
print(cell1 + param)
print(cell1 / param)
print(cell1 * param)
cell1.make_order(5)