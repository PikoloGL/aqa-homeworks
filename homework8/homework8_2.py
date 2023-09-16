"""
Створіть функцію, яка може повертати квадрати парних чисел у діапазоні від 0 до 1000000000 включно.
Рішення має працювати і не фрізити комп’ютер.
"""


def gen_range(range_num):
    for num in range(range_num + 1):
        if num % 2 == 0:
            yield num ** 2


if __name__ == "__main__":
    gen = gen_range(1000000000)
    for i in gen:
        print(i)
