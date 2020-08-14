"""
Реализовать класс фигуры. На основе фигуры реализовать класс треугольника,\
квадрата и прямоугольника с методами подсчета площади и периметра.\
Методы должны возвращать значение, а не принтить (это важно)
"""


class Figure:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        self._sides = [side_a, side_b]

    def show_sides(self):
        return self._sides


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.__val_triangle(side_a, side_b, side_c)
        super().__init__(side_a, side_b)
        self.side_c = side_c
        self._sides.append(self.side_c)

    def __val_triangle(self, side_a, side_b, side_c):
        if (side_a < (side_b + side_c)) is not True:
            print("It's not triangle!")
            print(f"Wrong value = {side_a}")
            raise ValueError
        elif (side_b < (side_a + side_c)) is not True:
            print("It's not triangle!")
            print(f"Wrong value = {side_b}")
            raise ValueError
        elif (side_c < (side_a + side_b)) is not True:
            print("It's not triangle!")
            print(f"Wrong value = {side_c}")
            raise ValueError

    def show_sides(self):
        return self._sides

    @property
    def square(self):
        return round(((((self.perimeter / 2) *
                        ((self.perimeter / 2) - self.side_a) *
                        ((self.perimeter / 2) - self.side_b) *
                        ((self.perimeter / 2) - self.side_c))) ** 0.5), 4)

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__(side_a, side_b)
        self._sides.append(self.side_a)
        self._sides.append(self.side_b)

    def show_sides(self):
        return self._sides

    @property
    def square(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2


class Square(Figure):
    def __init__(self, side_a, side_b=0):
        super().__init__(side_a, side_b)

        if self.side_b != 0:
            raise ValueError
        self.side_b = self.side_a

        self._sides = []
        for side_num in range(4):
            self._sides.append(self.side_a)

    def show_sides(self):
        return self._sides

    @property
    def square(self):
        return self.side_a ** 2

    @property
    def perimeter(self):
        return self.side_a * 4


print("fig as class Figure:")
fig = Figure(2, 6)
print(f"All sides: {fig.show_sides()}")

print("\ntri as class Triangle:")
tri = Triangle(3, 5, 7)
print(f"All sides: {tri.show_sides()}")
print(f"Square: {tri.square}")
print(f"Perimeter: {tri.perimeter}")

print("\nrec as class Rectangle:")
rec = Rectangle(4, 5)
print(f"All sides: {rec.show_sides()}")
print(f"Square: {rec.square}")
print(f"Perimeter: {rec.perimeter}")

print("\nsqr as class Square:")
sqr = Square(7)
print(f"All sides: {sqr.show_sides()}")
print(f"Square: {sqr.square}")
print(f"Perimeter: {sqr.perimeter}")
