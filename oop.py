"""Решение биквадратного уравнения объектно-ориентированным способом."""

import math
import sys


class BiquadraticEquation:
    """Биквадратное уравнение A*x^4 + B*x^2 + C = 0."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = None

    def _add_root(self, roots, root):
        if not any(math.isclose(root, old_root) for old_root in roots):
            roots.append(root)

    def solve(self):
        """Вычислить и вернуть список действительных корней."""
        if self.a == 0:
            if self.b == 0:
                return []
            y_values = [-self.c / self.b]
        else:
            self.discriminant = self.b ** 2 - 4 * self.a * self.c
            if self.discriminant < 0:
                return []
            if math.isclose(self.discriminant, 0):
                y_values = [-self.b / (2 * self.a)]
            else:
                d = math.sqrt(self.discriminant)
                y_values = [
                    (-self.b + d) / (2 * self.a),
                    (-self.b - d) / (2 * self.a),
                ]

        roots = []
        for y in y_values:
            if y > 0:
                value = math.sqrt(y)
                self._add_root(roots, value)
                self._add_root(roots, -value)
            elif math.isclose(y, 0):
                self._add_root(roots, 0.0)

        return sorted(roots)


def read_number(name, value=None):
    if value is not None:
        try:
            return float(value)
        except ValueError:
            print(f"Значение {name} в командной строке некорректно.")

    while True:
        try:
            return float(input(f"Введите коэффициент {name}: ").replace(',', '.'))
        except ValueError:
            print("Ошибка: нужно ввести число.")


def main():
    arguments = sys.argv[1:4]
    values = []
    for index, name in enumerate(['A', 'B', 'C']):
        value = arguments[index] if index < len(arguments) else None
        values.append(read_number(name, value))

    equation = BiquadraticEquation(*values)
    roots = equation.solve()
    print(f"Дискриминант: {equation.discriminant}")
    if roots:
        print("Действительные корни:", *roots)
    else:
        print("Действительных корней нет.")


if __name__ == '__main__':
    main()
