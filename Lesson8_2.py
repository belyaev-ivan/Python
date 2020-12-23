class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(self.txt)

inp_number_one = input("Введите делимое число: ")
inp_number_two = input("Введите делитель: ")

try:
    if inp_number_two == '0' or inp_number_two == 0:
        raise OwnError("На ноль делить нельзя!!!!")
    else:
        print(f"Все хорошо. Ваше число: {int(inp_number_one) / int(inp_number_two)}")

except OwnError:
    print('Измените делитель')
