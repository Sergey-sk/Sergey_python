# 1. Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).

N = input('Введите целое, положительное число: ')
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Неправильно ввели')
        N = input('Введите целое, положительное число: ')

result = 1.0
for k in range(1, N + 1):
    result *= (1 + 0.1 * k)
print(result)