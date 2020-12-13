with open('text_file2.txt','r', encoding='UTF-8') as f:
    user_line = [f'{num}. {" ".join(line.split())} : {len(line.split())} слов ' for num, line  in enumerate(f, 1)]
    print(*user_line, f'Всего строк - {len(user_line)}.', sep='\n')