# Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
# метод, который выводит информацию о товаре в формате "Название: название,
# Цена: цена, Количество: кол-во"

class Tovar:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        print(f'Название: {self.name}, Цена: {self.price}, Количество: {self.count}')

product1 = Tovar(input('Введите название товара: '), input('Введите цену товара: '), input('Введите количество товара: '))
product1.__str__()