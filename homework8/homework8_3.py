"""
Створіть декоратор, який повертає результат функції.
а також час за який вона виконана.
Підсказка (для фіксації часу імпортуйте модуль time:  import time)
"""
import time


def my_decorator(func):
    def wrapper(num):
        start_time = time.time()
        func(num)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function execution time: {execution_time} seconds")

    return wrapper


@my_decorator
def gen_range(range_num):
    for num in range(range_num + 1):
        if num % 2 == 0:
            print(num ** 2)


number = int(input("Enter your number: "))
gen_range(number)
