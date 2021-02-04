# Lesson 2
# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
user_list = list((input('Введите список через запятую ')).split(','))
print('Исходный список - {}'.format(user_list))
list_len = len(user_list)
new_list = []
for i in range(list_len):
    if 2*i + 1 == list_len:
        new_list.append(user_list[list_len-1])
        break
    elif 2*i + 1 > list_len:
        break
    else:
        new_list.append(user_list[2*i + 1])
        new_list.append(user_list[2*i])
print('Поменял соседние элементы местами - {}'.format(new_list))
