# Дано число R и список A размера N. Найти элемент списка, который наиболее близок
# к числу R (то есть такой элемент AK, для которого величина |AK - R| является
# минимальной).

import random

N = int(input('Введите размер списка A: '))
R = int(input('Введите число: '))
A = []
num = random.randint(0, R * 10)
while len(A) != N:
    A.append(num)
    num = random.randint(0, R * 10)
print(f'список A - {A}')
element = A[0]
for i in A:
    min_num = abs(i - R)
    max_num = i - R
    if max_num < min_num:
        min_num = max_num
        element = i
print(f'Наиболее близкий элемент списка к числу R: {element}')