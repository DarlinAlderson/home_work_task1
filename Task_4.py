# Задание 4.
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
profit = proceeds - costs
loss = costs - proceeds
if proceeds > costs:
    print("Финансовый результат: прибыль\n",
          "Величина прибыли:", profit)
else:
    print("Финансовый результат - убыток\n",
          "Величина убытка:", loss)
print("Рентабельность выручки:", float(costs / proceeds))
empl = abs(int(input("Введите количество сотрудников: ")))
print("Прибыль фирмы в расчете на одного сотрудника: ", float(profit / empl))
