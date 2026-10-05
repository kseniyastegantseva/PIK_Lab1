"""Решение биквадратного уравнения с использованием match-case."""

import math
import sys


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


def add_root(roots, root):
    if not any(math.isclose(root, old_root) for old_root in roots):
        roots.append(root)


def solve_equation(a, b, c):
    """Решить уравнение, используя сопоставление с образцом для случаев D."""
    if a == 0:
        y_values = [] if b == 0 else [-c / b]
        discriminant = None
    else:
        discriminant = b * b - 4 * a * c
        match discriminant:
            case d if d < 0:
                return discriminant, []
            case 0:
                y_values = [-b / (2 * a)]
            case _:
                d = math.sqrt(discriminant)
                y_values = [
                    (-b + d) / (2 * a),
                    (-b - d) / (2 * a),
                ]

    roots = []
    for y in y_values:
        match y:
            case value if value > 0:
                root = math.sqrt(value)
                add_root(roots, root)
                add_root(roots, -root)
            case value if math.isclose(value, 0):
                add_root(roots, 0.0)

    return discriminant, sorted(roots)


def main():
    arguments = sys.argv[1:4]
    values = []
    for index, name in enumerate(['A', 'B', 'C']):
        value = arguments[index] if index < len(arguments) else None
        values.append(read_number(name, value))

    discriminant, roots = solve_equation(*values)
    print(f"Дискриминант: {discriminant}")
    if roots:
        print("Действительные корни:", *roots)
    else:
        print("Действительных корней нет.")


if __name__ == '__main__':
    main()
