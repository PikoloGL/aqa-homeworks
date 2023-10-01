"""
Create a class with a description of the worker. Any worker or employees.
"""


class Worker:
    def __init__(self, name, employee_id, position, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"Employee Name: {self.name}\n" \
               f"Employee ID: {self.employee_id}\n" \
               f"Position: {self.position}\n" \
               f"Department: {self.department}\n" \
               f"Salary: ${self.salary}"


# Example usage:

# Create an instance of the Worker class for an employee
employee1 = Worker(
    name="John Doe",
    employee_id="EMP123",
    position="Software Engineer",
    department="Engineering",
    salary=80000  # Annual salary in dollars
)

# Display information about the employee
print(employee1)
