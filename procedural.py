"""Решение биквадратного уравнения процедурным способом.

Уравнение: A*x^4 + B*x^2 + C = 0.
"""

import math
import sys


def read_number(name, command_line_value=None):
    """Получить действительное число из аргумента или с клавиатуры."""
    if command_line_value is not None:
        try:
            return float(command_line_value)
        except ValueError:
            print(f"Значение {name} в командной строке некорректно.")

    while True:
        try:
            return float(input(f"Введите коэффициент {name}: ").replace(',', '.'))
        except ValueError:
            print("Ошибка: нужно ввести число.")


def read_coefficients():
    """Считать коэффициенты A, B и C."""
    arguments = sys.argv[1:4]
    names = ['A', 'B', 'C']
    coefficients = []

    for index, name in enumerate(names):
        value = arguments[index] if index < len(arguments) else None
        coefficients.append(read_number(name, value))

    return coefficients


def add_root(roots, root):
    """Добавить корень, если его ещё нет."""
    if not any(math.isclose(root, old_root) for old_root in roots):
        roots.append(root)


def solve_equation(a, b, c):
    """Вернуть дискриминант и список действительных корней."""
    # Сначала решаем квадратное уравнение относительно y = x^2.
    if a == 0:
        if b == 0:
            return None, []
        y_values = [-c / b]
        discriminant = None
    else:
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return discriminant, []
        if math.isclose(discriminant, 0):
            y_values = [-b / (2 * a)]
        else:
            sqrt_discriminant = math.sqrt(discriminant)
            y_values = [
                (-b + sqrt_discriminant) / (2 * a),
                (-b - sqrt_discriminant) / (2 * a),
            ]

    roots = []
    for y in y_values:
        if y > 0:
            value = math.sqrt(y)
            add_root(roots, value)
            add_root(roots, -value)
        elif math.isclose(y, 0):
            add_root(roots, 0.0)

    return discriminant, sorted(roots)


def main():
    a, b, c = read_coefficients()
    discriminant, roots = solve_equation(a, b, c)

    print(f"Дискриминант: {discriminant}")
    if roots:
        print("Действительные корни:", *roots)
    else:
        print("Действительных корней нет.")


if __name__ == '__main__':
    main()
