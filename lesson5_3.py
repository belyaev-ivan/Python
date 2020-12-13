with open('text_file3.txt','r', encoding='UTF-8') as f:
    zp = [line.split() for num, line in enumerate(f, 1)]
    nzp = []
    summ_zp = 0
    for i in zp:
        summ_zp += int(i[1])
        if int(i[1]) <= 20000:
            nzp.append(i[0])
    print(f'Средняя зарплата сотрудников компании составляет : {summ_zp / len(zp)}')
    print(f'Зарплату менее 20000 получают сотрудники {nzp}')
