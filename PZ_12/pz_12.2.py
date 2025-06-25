# Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

stroka = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}"'

lst = [i for i in stroka if i in string.punctuation]
print(''.join(lst))