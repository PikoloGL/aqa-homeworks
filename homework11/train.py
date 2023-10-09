"""
Опишіть об’єкт «Поїзд». Клас повинен містити поля та метод для додавання вагонів
(необхідно додати об’єкти та екземпляри класу вагонів).

Опишіть клас Вагон разом із поїздом.
Вагон повинен містити список пасажирів і дозволяти додавати пасажирів.
У Вагоні може бути наприклад не більше 10 пасажирів.
Під час використання функції len у вагоні я хочу бачити кількість пасажирів.
Використовуючи len у поїзді, я хочу бачити список вагонів без локомотива.
Кожен вагон повинен мати номер.
Під час друку вагона на консолі я хочу бачити наступне «[n]», де n — номер вагона.

Реалізуйте друк потяга із завдання 2.
Під час друку потяга вагони та локомотив мають відображатися на консолі у такому форматі:

<=[HEAD]-[1]-[2]-[3]-[4]-[...]
"""


class Train:
    def __init__(self):
        self.head = "[HEAD]"
        self.carriages = []

    def add_carriage(self, carriage):
        self.carriages.append(carriage)

    def __len__(self):
        # Exclude the locomotive from the count
        return len(self.carriages)

    def __str__(self):
        carriage_str = " <= ".join([self.head] + [str(carriage) for carriage in self.carriages])
        return carriage_str


class Carriage:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print("Carriage is full. Cannot add more passengers.")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"[{self.number}]"


# Example usage:
if __name__ == "__main__":
    train = Train()
    train.add_carriage(Carriage(1))
    train.add_carriage(Carriage(2))
    train.add_carriage(Carriage(3))

    for i in range(11):
        train.carriages[0].add_passenger(f"Passenger-{i + 1}")

    print(f"Train length (excluding locomotive): {len(train)}")
    print(train)
