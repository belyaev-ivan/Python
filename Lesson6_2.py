class Road:
    _length = 0
    _width = 0
    __hight = 5   # число см толщины полотна
    __massa = 25    # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
    def __init__(self, a, b):
        self._length = a
        self._width = b
        summ_massa = self._length * self._width * self.__hight * self.__massa
        print(f'Масса асфальта для покрытия дороги длинной {self._length} метров и шириной {self._width} '
              f'метров составляет {summ_massa} тонн')

a = Road(1000, 10)
