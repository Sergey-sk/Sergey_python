num = input('Введите целое двузначное число:')
try:
    num = int(num)
    if num < 10 or num > 99:
        print('Число не двузначное')
    else:
        print(num // 10, num % 10, sep='\n')
except ValueError:
    print('Неверно ввели!')
    num = input('Введите целое двузначное число:')
