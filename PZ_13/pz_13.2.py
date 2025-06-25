# В двумерном списке найти сумму элементов второй половины матрицы.

import random

def sum_spisok(matrix):
    sum_el = 0
    start = len(matrix) // 2
    sum_el = sum([matrix[i][j] for j in range(len(matrix[0])) for i in range(start, len(matrix))])
    return sum_el

cols = int(input('Введите количество строк: '))
rows = int(input('Введите количество столбцов: '))

matrix = [[random.randint(-10, 10) + j * rows for i in range(rows)] for j in range(cols)]
for i in matrix:
    print(i, sep='\n')

print(sum_spisok(matrix))