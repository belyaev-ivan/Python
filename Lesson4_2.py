user_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [user_list[i] for i in range(1, len(user_list)) if user_list[i] > user_list[i-1]]
print(result_list)