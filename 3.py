# Lesson 2
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month_id = input('Введите месяц в виде целого числа от 1 до 12 ')
while month_id.isdigit() == False or int(month_id) not in range(1,12):
    month_id = input('Неверный формат! Введите месяц в виде целого числа от 1 до 12 ')

month_id = int(month_id)
months_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(months_list[month_id-1])
months_dict = {'1': 'Jan','2': 'Feb','3': 'Mar','4': 'Apr','5': 'May','6': 'Jun','7': 'Jul','8': 'Aug','9': 'Sep','10': 'Oct','11': 'Nov','12': 'Dec'}
print(months_dict[str(month_id)])