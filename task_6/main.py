import random
from itertools import combinations

data = [[random.randint(-10, 10) for _ in range(4)] for _ in range(20)]#Создаём список 
print("Случайный список:")#Пишем Случайный список
for row in data:#Пишем цикл                       
    print(row)#Выводим список
unique_combinations = {tuple(sorted(row)) for row in data}#Находим уникальные комбинации 
print("\nУникальные комбинации:")
print(list(unique_combinations))#Выводим уникальные комбинации
# 3. Ввод числа пользователем
n = int(input("\nВведите целое число: "))#Вводим число
all_numbers = [num for row in data for num in row]# Берём все числа из исходного списка
count = sum(1 for combo in unique_combinations if sum(combo) < n)# Вычисляем сумму пар
print(f"\nКоличество пар, сумма которых меньше {n}: {count} ")# Выводим сумму пар

