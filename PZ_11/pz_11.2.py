# Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить строку
# наименьшей длины.

import string

with open("C:\\Users\\Admin\\Downloads\\text18-11.txt", encoding='utf-16') as file:
    fr1 = file.readlines()
    min_line = min(fr1, key=len)
    print(f'Содержимое файла: \n{''.join(fr1)}\n')
    count_punct = sum(1 for i in fr1 for char in i if char in string.punctuation)
    print(f'Количество знаков препинания: {count_punct}')

with open('new_file.txt', 'w') as fw:
    fw.write(min_line)

with open('new_file.txt') as file_read:
    print(f'Строка наименьшей длины: {min_line}')