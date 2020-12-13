from random import randint

with open('text_file5.txt','w', encoding='UTF-8') as f:
    f.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
with open('text_file5.txt', 'r', encoding='UTF-8') as f1:
    print(sum(map(int, f1.readline().split())))

