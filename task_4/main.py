import re#подключаем модуль ре
import string#подключаем модуль стринг
substring = str(input("Введите строку: "))#вводим подстроку
with open("text.txt", "r", encoding="utf-8") as file:# Открываем файл text.txt 
    lines = file.readlines()# считываем все строки
matched = [line.strip() for line in lines if substring in line]# Ищем совпадения
print(f"Количество строк, содержащих '{substring}': {len(matched)}\n")# Выводим количество совпадений
print("Найденные строки:")# Выводим найденные строки
for line in matched:# Выводим найденные строки
    print(line)# Выводим найденные строки
sorted_lines = sorted(matched, key=len)# Сортируем по длине
print("\nОтсортированные по длине:")# Выводим отсортированные строки
for line in sorted_lines:
    print(line)
