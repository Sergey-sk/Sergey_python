# В двумерном списке найти сумму и произведение элементов строки N (N задать с
# клавиатуры)

import random
from functools import reduce

cols = int(input('Введите количество строк: '))
rows = int(input('Введите количество столбцов: '))

lst = [[random.randint(-10, 10) + j * rows for i in range(rows)] for j in range(cols)]


n = int(input(f'Введите номер строки 1-{cols}: '))
n -= 1

for matr in lst:
    print(matr, sep='\n')

if 0 <= n < len(lst):
    multipl = reduce(lambda x, y: x * y, lst[n])
    print(f'Сумма и произведение {n + 1} строки: {sum(lst[n])}, {multipl}')
else:
    print('Неверный номер строки!')
