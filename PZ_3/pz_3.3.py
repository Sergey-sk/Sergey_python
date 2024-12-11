# Ввести 2 числа. Если их произведение отрицательно, умножить его на 8,
# в противном случае, увеличить его в 1.5 раза

num_1, num_2 = int(input('Введите первое число: ')), int(input('Введите первое число: '))
proizvid = num_1 * num_2
if proizvid < 0:
    print(proizvid * 8)
else:
    print(proizvid * 1.5)