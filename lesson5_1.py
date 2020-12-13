with open('text_file1.txt','w', encoding='UTF-8') as f:
    while True:
        text = input('Введите строку текста')
        if text == 'end':
            break
        else:
            f.write(f"{text}\n")

