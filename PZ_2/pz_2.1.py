num = int(input('Введите двузначное число:'))
if len(str(num)) > 2 or len(str(num)) < 2:
    print('Число не двузначное')
else:
    print(num // 10, num % 10, sep='\n')
