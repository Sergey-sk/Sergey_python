#1. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Каждое из
# чисел A, B, C положительное».

A = input('Введите целое число: ')
B = input('Введите целое число: ')
C = input('Введите целое число: ')
try:
 A = int(A)
except ValueError:
 print("Неправильно ввели!")
 A = input("Введите первое число: ")
try:
 B = int(B)
except ValueError:
 print("Неправильно ввели!")
 B= input("Введите второе число: ")
try:
 C = int(C)
except ValueError:
 print("Неправильно ввели!")
 C = input("Введите третье число: ")

if int(A) > 0 and int(B) > 0 and int(C) > 0:
    print(True)
else:
    print(False)
