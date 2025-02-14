# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар, печенье, сыр.
# Пятерочка – мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар, печенье. Лента
# – печенье, молоко, сыр.
# Определить:
# 1. в каких магазинах нельзя приобрести соль.
# 2. в каких магазинах можно приобрести одновременно молоко, печенье и сыр.
# 3. в каких магазинах можно приобрести мясо и молоко.

magnit = {'молоко', 'соль', 'сахар', 'печенье', 'сыр'}
pyaterochka = {'мясо', 'молоко', 'сыр'}
perekrestok = {'молоко', 'творог', 'сыр', 'сахар', 'печенье'}
lenta = {'печенье', 'молоко', 'сыр'}
milk_cheese = set()
milk_meat = set()
no_salt = set()

if not {'соль'}.intersection(magnit):
    no_salt.add('Магнит')
if not {'соль'}.intersection(pyaterochka):
    no_salt.add('Пятерочка')
if not {'соль'}.intersection(perekrestok):
    no_salt.add('Перекресток')
if not {'соль'}.intersection(lenta):
    no_salt.add('Лента')

milk_cheese.add('Магните' if 'молоко' in magnit and 'печенье' in magnit and 'сыр' in magnit else 0)
milk_cheese.add('Пятерочке' if 'молоко' in pyaterochka and 'печенье' in pyaterochka and 'сыр' in pyaterochka else 0)
milk_cheese.add('Перекрестке' if 'молоко' in perekrestok and 'печенье' in perekrestok and 'сыр' in perekrestok else 0)
milk_cheese.add('Ленте' if 'молоко' in lenta and 'печенье' in lenta and 'сыр' in lenta else 0)

milk_meat.add('Магните' if 'молоко' in magnit and 'мясо' in magnit else 0)
milk_meat.add('Пятерочке' if 'молоко' in pyaterochka and 'мясо' in pyaterochka else 0)
milk_meat.add('Перекрестке' if 'молоко' in perekrestok and 'мясо' in perekrestok else 0)
milk_meat.add('Ленте' if 'молоко' in lenta and 'мясо' in lenta else 0)

store_with_milk = {item for item in milk_cheese if item != 0}
store_with_meat = {item for item in milk_meat if item != 0}

print(f'Соли нет в {no_salt}')
print(f'Приобрести одновременно молоко, печенье и сыр можно в {store_with_milk}')
print(f'Приобрести мясо и молоко можно в {store_with_meat}')