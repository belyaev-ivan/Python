my_dict = { 'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре'}
my_list = []
with open('text_file4.txt','r', encoding='UTF-8') as f:
    my_list = [line.split() for num, line in enumerate(f, 1)]
    for i in my_list:
        i[0] = (my_dict[i[0]])
    with open('text_file4_new.txt', 'w', encoding='UTF-8') as nf:
        for i in my_list:
            nf.write(f"{i[0]} {i[1]} {i[2]}\n")



