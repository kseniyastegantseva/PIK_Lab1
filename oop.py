"""Решение биквадратного уравнения с помощью класса."""

import math
import sys


def get_number(name, argument=None):
    if argument is not None:
        try:
            return float(argument)
        except ValueError:
            print(f"Аргумент {name} должен быть числом. Введите его вручную.")

    while True:
        try:
            return float(input(f"Введите {name}: ").replace(',', '.'))
        except ValueError:
            print("Ошибка: введите число.")


class Equation:
    def __init__(self, a, b, c):
        # Коэффициенты сохраняются внутри объекта.
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = None

    def solve(self):
        # Замена y = x^2 превращает уравнение в A*y^2 + B*y + C = 0.
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return None  # любое число подходит
                return []
            y_values = [-self.c / self.b]
        else:
            self.discriminant = self.b ** 2 - 4 * self.a * self.c

            if self.discriminant < 0:
                return []
            elif self.discriminant == 0:
                y_values = [-self.b / (2 * self.a)]
            else:
                y1 = (-self.b + math.sqrt(self.discriminant)) / (2 * self.a)
                y2 = (-self.b - math.sqrt(self.discriminant)) / (2 * self.a)
                y_values = [y1, y2]

        roots = []
        for y in y_values:
            if y > 0:
                roots.append(math.sqrt(y))
                roots.append(-math.sqrt(y))
            elif y == 0:
                roots.append(0)

        return sorted(roots)


def main():
    args = sys.argv[1:]
    a = get_number('A', args[0] if len(args) > 0 else None)
    b = get_number('B', args[1] if len(args) > 1 else None)
    c = get_number('C', args[2] if len(args) > 2 else None)

    equation = Equation(a, b, c)
    roots = equation.solve()
    print('Дискриминант:', equation.discriminant)

    if roots is None:
        print('Корни: любое действительное число')
    elif roots:
        print('Действительные корни:', roots)
    else:
        print('Действительных корней нет')


if __name__ == '__main__':
    main()
