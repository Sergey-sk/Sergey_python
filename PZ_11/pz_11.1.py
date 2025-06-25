# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Количество положительных элементов в первой половине:

import random

count_nums = int(input('Введите длину последовательности чисел: '))
numbers = [random.randint(-100, 100) for i in range(count_nums)]

with open('nums.txt', 'w') as file:
    for i in numbers:
        file.write(f'{i}\n')

with open('nums.txt') as fr:
    content = fr.read().split('\n')
    nums_more_zero = [i for i in content[0:count_nums // 2] if int(i) > 0]

with open('new.txt', 'w') as fw:
    fw.write(f'Исходные данные: {', '.join(content[:-1])}\n')
    fw.write(f'Количество элементов: {count_nums}\n')
    fw.write(f'Минимальный элемент: {min(int(i) for i in content[:-1])}\n')
    fw.write(f'Количество положительных элементов в первой половине: {len(nums_more_zero)}')

with open('new.txt') as file_read:
    print(file_read.read())