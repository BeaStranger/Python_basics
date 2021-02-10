# Lesson 4
# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
digit_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(digit_list)
new_list = [j for i,j in zip(digit_list,digit_list[1:]) if j > i]
print(new_list)