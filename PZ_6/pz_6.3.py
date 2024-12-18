# Дан список размера N. Осуществить сдвиг элементов списка влево на одну позицию
# (при этом AN перейдет в AN-1, AN-1 — в AN-2, .., A2 — в A1, a исходное значение
# первого элемента будет потеряно). Последний элемент полученного списка
# положить равным 0.

import random

N = int(input('Введите размер списка: '))
spisok = []
while len(spisok) != N:
    spisok.append(random.randint(0, N * 10))
print(f'Изначальный список: {spisok}')
spisok.pop(0)
spisok[-1] //= spisok[-1]
for i in spisok:
    i -= 1
    print(i)