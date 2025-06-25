# В последовательности на n целых чисел найти и вывести:
# 1. минимальный среди положительных
# 2. элементы кратные пяти
# 3. их среднее арифметическое

import random

n = int(input('Введите длину последовательности: '))
lst = [random.randint(-100, 100) for i in range(n)]

min_list = list(filter(lambda i: i > 0, lst))
new_list = list(filter(lambda i: i % 5 == 0, lst))
arithmetic_list = [sum(lst) / len(lst)]

print(f'Изначальная последовательность: {lst}')
print(f'Минимальный среди положительных: {min(min_list)}')
print(f'Элементы кратные 5: {new_list}')
print(f'Среднее арифметическое: {arithmetic_list}')