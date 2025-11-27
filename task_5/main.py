import random
numbers = [random.randint(-50, 50) for _ in range(25)]#Создаём список случайных целых чисел от -50 до 50, размером 25 элементов
elements = len(numbers)#Общее число элементов
# 2. Находим количество положительных, отрицательных и нулевых элементов
positive = sum(1 for num in numbers if num > 0)#Находим количество положительных
negative = sum(1 for num in numbers if num < 0)#Находим количество отрицательных
zero = sum(1 for num in numbers if num == 0)#Находим количество нулевых элементов
def print_stats(count, label):
    percent = (count / elements) * 100#Считаем проценты
    print(f"{label}: {count} ({percent:.2f}%)")#Выводим значения и их количества с процентом
print("Сгенерированный список чисел:")#Выводим список
print(numbers)#Выводим список
print("\nРезультаты подсчёта:")#Выводим результаты подсчёта
print_stats(positive, "Положительных элементов")#Выводим положительные элементы
print_stats(negative, "Отрицательных элементов")#Выводим отрицательные элементы
print_stats(zero, "Нулевых элементов")#Выводим нулевые элементы

max_value = max(numbers)# Находим самое большое значение
min_value = min(numbers)# Находим самое маленькое значение
print(f"\nСамое большое значение: {max_value}")#Выводим самое большое значение
print(f"Самое маленькое значение: {min_value}")#Самое маленькое значение
