# Лабораторная работа №1

Программы решают биквадратное уравнение:

```text
A*x^4 + B*x^2 + C = 0
```

## Запуск

Можно ввести коэффициенты с клавиатуры:

```text
python procedural.py
```

Или передать их в командной строке:

```text
python procedural.py 1 -5 4
python oop.py 1 -5 4
python functional.py 1 -5 4
```

Для примера `1 -5 4` программа получает корни `-2, -1, 1, 2`.

Файлы отличаются способом организации кода:

- `procedural.py` — функции;
- `oop.py` — класс `BiquadraticEquation`;
- `functional.py` — сопоставление с образцом `match-case`.
