# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.


class Figura:

    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Figura):
    pass

class Square(Figura):

    def area(self):
        area_square = self.width * self.height
        print(f'Площадь = {area_square}')

    def perimetr(self):
        perimetr_square = (self.width + self.height) * 2
        print(f'Периметр = {perimetr_square}')

square = Square(5, 8)
square.perimetr()
square.area()