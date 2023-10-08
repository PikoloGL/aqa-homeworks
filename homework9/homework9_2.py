"""
Create a class with a description of the worker. Any worker or employees.
"""


class Worker:
    """
        A class to describe a worker.

        Class attributes:
            company (str): Name of the company that worker is working in

        Attributes:
            name (str): Worker name
            employee_id (int): Worker id in our database
            position (str): Worker position in company
            department (str): Worker department
            salary (int): Worker salary
        """
    company = "Apple"

    def __init__(self, name, employee_id, position, department, salary):
        """
        Initializes a new Worker instance.
        """
        self.name = name
        self._employee_id = employee_id  # Protected attribute
        self.position = position
        self.department = department
        self.__salary = salary  # Private attribute
        self.company = Worker.company

    def __str__(self):
        """
        Function that returns information about our worker
        """
        return f"Employee Name: {self.name}\n" \
               f"Company Name: {self.company}\n" \
               f"Employee ID: {self._employee_id}\n" \
               f"Position: {self.position}\n" \
               f"Department: {self.department}\n" \
               f"Salary: ${self.__salary}"

    """
    Static method that shows day offs across the company
    """

    @staticmethod
    def day_off():
        return "Day offs in company: 1.01, 25.12"


if __name__ == "__main__":
    """
    Create an instance of the Worker class for an employee
    """
    employee1 = Worker(
        name="John Doe",
        employee_id="EMP123",
        position="Software Engineer",
        department="Engineering",
        salary=80000  # Annual salary in dollars
    )

    """
    Display information about the employee
    """
    print(employee1)
    print(Worker.day_off())
