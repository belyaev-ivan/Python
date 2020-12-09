from functools import reduce

def numbers(num1, num2):
    return num1 * num2

user_list = [i for i in range(100, 1001)  if i % 2 == 0]
print(reduce(numbers, user_list))