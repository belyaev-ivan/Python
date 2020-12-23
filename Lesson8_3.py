class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(self.txt)


my_list_number = []
my_number = []

while True:
    try:
        inp_data = input("Введите число: ")
        if inp_data == 'stop':
            print(my_number)
            break
        for i in inp_data:
            for z in range(0, 10):
                if str(z) == i:
                    break
            else:
                raise OwnError('Вы ввели строку, ДОСВИДАНИЯ!!!')
        my_number.append(inp_data)
        print(my_number)
    except OwnError:
        break

