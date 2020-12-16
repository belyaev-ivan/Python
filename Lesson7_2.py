from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, quantity):

        self.quantity = quantity

    @property
    def create(self):
        return f'Расход ткани на пальто равен: {self.quantity / 6.5 + 0.5}' \
               f'Расход ткани на костюм равен: {2 * self.quantity + 0.3}'

    @abstractmethod
    def abstract(self):
        pass



class Coat(Clothes):
    @property
    def create(self):
        return f'Расход ткани на пальто равен: {self.quantity / 6.5 + 0.5}'
    def abstract(self):
        pass

class Suit(Clothes):
    @property
    def create(self):
        return f'Расход ткани на костюм равен: {2 * self.quantity + 0.3}'
    def abstract(self):
        pass

try:
    clothes = Clothes(100)
except TypeError:
    print('Выберите класс одежды')

coat = Coat(105)
print(coat.create)
suit = Suit(1.85)
print(suit.create)