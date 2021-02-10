# Lesson 4
# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
import itertools as it
# Выводит целые числа с заданным шагом
def integer_generator(start=0, end=10, step=1):
    c = start
    for el in it.count(start,step):
        if c > end:
            break
        print(el)
        c += step
# Выводит введенный список, добавляя копию одного элемента за каждую единицу во втором аргументе
def list_generator(list, repeat_count=1):
    c = 0
    for el in it.cycle(list):
        if c > repeat_count+1:
            break
        print(el)
        c += 1

print(integer_generator(0,10, 3))
print(list_generator(['Baba','Mama'],1))