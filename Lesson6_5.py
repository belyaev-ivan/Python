class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'С ее помощью можно писать аккуратно и красиво')

class Pencil(Stationery):
    def draw(self):
        print(f'С его помощью можно допускать неосторожности при письме и потом исправить их ')

class Handle(Stationery):
    def draw(self):
        print(f'При его использовании необходимо проявить особую осторожность!!!')

a = Pen('Pen')
b = Pencil('Pencil')
c = Handle('Handle')

a.draw()
b.draw()
c.draw()