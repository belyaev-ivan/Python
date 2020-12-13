my_lesson_dict = {}
with open('text_file6.txt', 'r', encoding='UTF-8') as f:
    for i in f:
        name_object, time_object = i.split(':')
        q = []
        for z in time_object:
            if z == ' ' or (z >= '0' and z <= '9'):
                q.append(z)
        q = "".join(q)
        summ_time = sum(map(int, "".join(q).split()))
        my_lesson_dict[name_object] = summ_time
print(my_lesson_dict)











