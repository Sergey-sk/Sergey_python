# Дан список A размера N (N — четное число). Вывести его элементы с четными
# номерами в порядке возрастания номеров: A2, A4, A6, ..., AN. Условный оператор не
# использовать.

element = 1
N = int(input('Введите четное число - размер списка A: '))
while True:
    if N % 2 != 0:
        print('Число нечетное!')
        N = int(input('Введите четное число: '))
    break

A = list(range(N))
print(A[::2])