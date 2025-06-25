# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
# год и поместить ее в новый текстовый файл.

import re

with open("C:\\Users\\Admin\\Downloads\\Dostoevsky.txt", encoding='utf-8') as file:
    lines = file.read()

year = re.findall(r'1857[\s\S]*?(?=\n\d{4}|$)', lines)
print(year)

with open('new_file.txt', 'w') as new_file:
    for i in year:
        new_file.write(i)