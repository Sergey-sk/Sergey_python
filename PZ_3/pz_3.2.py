# 2. Дано целое число, лежащее в диапазоне 1-999. Вывести его строку- описание вида
# «четное двузначное число», «нечетное трехзначное число» и т. д.

num = input('Введите число от 1 до 999: ')
while type(num) != int:
    try:
        num = int(num)
    except ValueError:
        print('Неправильно ввели!')
        num = input('Введите число от 1 до 999: ')
if 1 < num < 999:
    if num % 2 == 0:
        chet = 'четное'
    else:
        chet = 'нечетное'

    if num < 10:
        dig = 'однозначное'
    elif 10 <= num < 100:
        dig = 'двузначное'
    else:
        dig = 'трехзначное'
    print(f'число {chet} {dig}')
else:
    print('число должно быть в диапазоне 1-999')
