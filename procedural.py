"""Решение биквадратного уравнения с помощью функций."""

import math
import sys


def get_number(name, argument=None):
    if argument is not None:
        try:
            return float(argument)
        except ValueError:
            print(f"Аргумент {name} должен быть числом. Введите его вручную.")

    # Если аргумента нет или он неправильный, спрашиваем число с клавиатуры.
    while True:
        try:
            return float(input(f"Введите {name}: ").replace(',', '.'))
        except ValueError:
            print("Ошибка: введите число.")


def solve(a, b, c):
    # Делаем замену y = x^2. Тогда получаем A*y^2 + B*y + C = 0.
    if a == 0:
        discriminant = None
        if b == 0:
            if c == 0:
                return discriminant, None  # любое число подходит
            return discriminant, []
        y_values = [-c / b]
    else:
        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return discriminant, []
        elif discriminant == 0:
            y_values = [-b / (2 * a)]
        else:
            y1 = (-b + math.sqrt(discriminant)) / (2 * a)
            y2 = (-b - math.sqrt(discriminant)) / (2 * a)
            y_values = [y1, y2]

    # Из y = x^2 получаем x = корень из y и x = минус корень из y.
    roots = []
    for y in y_values:
        if y > 0:
            roots.append(math.sqrt(y))
            roots.append(-math.sqrt(y))
        elif y == 0:
            roots.append(0)

    return discriminant, sorted(roots)


def main():
    args = sys.argv[1:]
    a = get_number('A', args[0] if len(args) > 0 else None)
    b = get_number('B', args[1] if len(args) > 1 else None)
    c = get_number('C', args[2] if len(args) > 2 else None)

    discriminant, roots = solve(a, b, c)
    print('Дискриминант:', discriminant)

    if roots is None:
        print('Корни: любое действительное число')
    elif roots:
        print('Действительные корни:', roots)
    else:
        print('Действительных корней нет')


if __name__ == '__main__':
    main()
