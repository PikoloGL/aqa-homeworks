"""
Create a class describing any company. For example, Toshiba or Apple
"""


class Company:
    def __init__(self, name, founded_year, industry, headquarters_location, CEO, employees, revenue):
        self.name = name
        self.founded_year = founded_year
        self.industry = industry
        self.headquarters_location = headquarters_location
        self.CEO = CEO
        self.employees = employees
        self.revenue = revenue

    def __str__(self):
        return f"Company Name: {self.name}\n" \
               f"Founded Year: {self.founded_year}\n" \
               f"Industry: {self.industry}\n" \
               f"Headquarters Location: {self.headquarters_location}\n" \
               f"CEO: {self.CEO}\n" \
               f"Number of Employees: {self.employees}\n" \
               f"Annual Revenue: ${self.revenue} billion"


# Example usage:

# Create an instance of the Company class for Apple Inc.
apple = Company(
    name="Apple Inc.",
    founded_year=1976,
    industry="Technology",
    headquarters_location="Cupertino, California, USA",
    CEO="Tim Cook",
    employees=147000,
    revenue=365.7  # In billions of dollars (2021)
)

# Display information about Apple Inc.
print(apple)
