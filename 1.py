# Lesson 4
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
def salary_calc(work_hours, rate = 200, bonus = 0):
    return (work_hours * rate) + bonus

print(salary_calc(work_hours=20,bonus=500))
print(salary_calc(10))
print(salary_calc(bonus=500,work_hours=5))