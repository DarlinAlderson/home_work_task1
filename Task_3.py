# Задание 3.
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

n = abs(int(input("Введите число: ")))
s = (f"n + nn + nnn: "
     f" {n}"
     f" {n*2}"
     f" {n*3}")
print(s)