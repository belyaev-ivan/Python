import sys

def ZP():
    try:
        time, money, bonus = map(int, sys.argv[1:])
        print(f'Заработная плата сотрудника за {time} часов составила {time * money + bonus}')
    except ValueError:
        print("Неверный формат введенных значений")
ZP()