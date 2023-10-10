"""
Створіть ітератор, який приймає послідовність і може перебирати значення в заданому діапазоні.
CustomIterator(послідовність, початковий_індекс, кінцевий_індекс)
"""


class CustomIterator:
    def __init__(self, sequence, starting_index, ending_index):
        self.sequence = sequence
        self.index = starting_index
        self.end_index = ending_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= self.end_index:
            result = self.sequence[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def counter(self):
        for value in self:
            print(value)


# Example usage:
if __name__ == "__main__":
    my_sequence = [1, 2, 3, 4, 5]
    iterator = CustomIterator(my_sequence, 1, 3)
    iterator.counter()
