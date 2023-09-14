"""Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями."""


def sum_range(start, end):
    total = 0
    if start < end:
        for i in range(start, end + 1):
            total += i
        return total
    else:
        for i in range(end, start + 1):
            total += i
        return total


if __name__ == "__main__":
    start_input = int(input("Enter first number: "))
    end_input = int(input("Enter second number: "))
    print(sum_range(start_input, end_input))
