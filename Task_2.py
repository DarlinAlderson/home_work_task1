# Задание 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print("Var_1")
seconds = int(input("Введите время в секундах: "))
seconds = seconds % (24 * 3600)
hours = seconds // 3600
minutes = seconds // 60
print(f"Время в формате чч:мм:сс: "
      f"{hours}:"
      f"{minutes}:"
      f"{seconds}")

print("Var_2")
import time

seconds = int(input("Введите время в секундах: "))
time_format = time.strftime("%H:%M:%S", time.gmtime(seconds))
print("Время в формате чч:мм:сс:", time_format)
