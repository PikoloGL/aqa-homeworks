"""Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення :
периметр квадрата, площа квадрата та діагональ квадрата.
Надрукуйте їх"""
import math


def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal


if __name__ == "__main__":
    side = float(input("Enter length of the side: "))
    perimeter, area, diagonal = square(side)

    print("Your square perimeter:", perimeter)
    print("Your square are:", area)
    print("Your square diagonal:", diagonal)
