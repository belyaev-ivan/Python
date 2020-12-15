class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def return_full_name(self):
        self.get_full_name = f'{self.name} {self.surname}'
        return self.get_full_name

    def return_total_income(self):
        self.get_total_income = self._income["wage"] + self._income["bonus"]
        return self.get_total_income


a = Position('Ivan', 'Ivanov', 'Manager', 20000, 15000)
print(a.return_full_name())
print(a.position)
print(a.return_total_income())
