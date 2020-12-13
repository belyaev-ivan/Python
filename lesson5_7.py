import json
dict_profit = {}
average_profit = {}
with open('text_file7.txt', 'r', encoding='UTF-8') as f:
    y = 0
    summ_profit = 0
    for i in f:
        name, tip, prib, rashod = i.split(' ')
        profit = int(prib) - int(rashod)
        if profit > 0:
            y += 1
            summ_profit += profit
        dict_profit[name] = profit

    sred_profit = summ_profit / y

    average_profit['average_profit'] = sred_profit
print(dict_profit, average_profit)

with open('text_file7.json', 'w') as f1:
    list_json = [dict_profit, average_profit]
    json.dump(list_json, f1)
