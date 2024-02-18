#!/usr/bin/env python3

# Program liczący pierwiastki (x0, x1, x2) delty na podstawie parametrów zadanych użytkownika

# a = 1, b = 4, c = 3 -> x1 = -3, x2 = -1
# a = 4, b = 4, c = 1 -> -0.5

from math import sqrt


def delta(a: int, b: int, c: int) -> int:
    """Funkcja obliczająca deltę"""
    return b ** 2 - 4 * a * c


def pierwiastki(a: int, b: int, c: int):
    """Funkcja obliczająca piewiastki równania kwadratowego"""
    d = delta(a, b, c)
    print(f"Delta = {d}")
    try:
        if d == 0:
            x = -b / (2 * a)
            print(f"x0 = {x}")
        elif d < 0:
            print("Brak pierwiastków rzeczywistych")
        else:
            x1 = (-b - sqrt(d)) / (2 * a)
            x2 = (-b + sqrt(d)) / (2 * a)
            print(f"x1 = {x1}, x2 = {x2}")
    except ZeroDivisionError as e:
        print("Podzielono przez 0! Współczynnyk a nie może być 0!")
        print(e)


if __name__ == '__main__':
    print("Podaj współczynniki (a, b, c) równania kwadratowego (ax^2 + bx + c):")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    pierwiastki(a, b, c)
