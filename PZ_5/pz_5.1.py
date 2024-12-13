# Составить функцию, которая напечатает 40 любых символов

def simvols():
    s = input('Введите количество символов: ')
    while type(s) != int:
        try:
            s = int(s)
        except ValueError:
            print('Неправильно ввели!')
            s = input('Введите количество символов: ')

    for i in range(0, 0 + s):
        print(chr(i), end='')

simvols()