"""
Create a class describing any company. For example, Toshiba or Apple
"""


class Company:
    """
    A class to describe a company.

    Attributes:
        name (str): The name of the company.
        founded_year (int): The year the company was founded.
        industry (str): The industry in which the company operates.
        headquarters_location (str): The location of the company's headquarters.
        CEO (str): The name of the company's CEO.
        employees (int): The number of employees in the company.
        revenue (float): The annual revenue of the company in billions of dollars.
    """

    def __init__(self, name, founded_year, industry, headquarters_location, CEO, employees, revenue):
        """
        Initializes a new Company instance.
        """
        self.name = name
        self.founded_year = founded_year
        self.industry = industry
        self.headquarters_location = headquarters_location
        self.CEO = CEO  # Public attribute
        self._employees = employees  # Protected attribute
        self.__revenue = revenue  # Private attribute

    def __str__(self):
        """
        Function that returns information about our company
        """
        return f"Company Name: {self.name}\n" \
               f"Founded Year: {self.founded_year}\n" \
               f"Industry: {self.industry}\n" \
               f"Headquarters Location: {self.headquarters_location}\n" \
               f"CEO: {self.CEO}\n" \
               f"Number of Employees: {self._employees}\n" \
               f"Annual Revenue: ${self.__revenue} billion"

    @property
    def revenue(self):  # getter
        return self.__revenue

    @revenue.setter
    def revenue(self, new_revenue):  # setter
        self.__revenue = new_revenue


if __name__ == "__main__":
    """
    Create an instance of the Company class for Apple Inc.
    """
    apple = Company(
        name="Apple Inc.",
        founded_year=1976,
        industry="Technology",
        headquarters_location="Cupertino, California, USA",
        CEO="Tim Cook",
        employees=147000,
        revenue=365.7  # In billions of dollars (2021)
    )
    """
    Display information about Apple Inc.
    """
    print(apple)
    print(f"Old revenue: ${str(apple.revenue)} billion")
    apple.revenue = 501.3
    print(f"New revenue: ${str(apple.revenue)} billion")
