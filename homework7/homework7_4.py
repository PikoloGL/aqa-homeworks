"""
написати власну функцію map, використовуючи callback
"""


def my_map(callback, iterable):
    result = []
    for n in iterable:
        calculation = callback(n)
        result.append(calculation)
    return result


def square(number):
    number *= number
    return number


if __name__ == "__main__":
    print(my_map(square, [1, 2, 3]))
