import re#подключаем модуль ре
import string#подключаем модуль стринг

kolvo = int(input("Введите количество строк: "))#вводим переменную количества строок
lines = []  # Создаём список для хранения строк

for a in range(kolvo):#пишем цикл
    line = input(f"Введите строку {a + 1}: ")#просим ввести строку
    lines.append(line)# Создаём список списков слов
words = [line.split() for line in lines]#разбиваем на слова


total_words = sum(len(word_list) for word_list in words)#считаем количество слов
print(f"Общее количество слов: {total_words}")# Выводим количество слов во всех введённых строках




