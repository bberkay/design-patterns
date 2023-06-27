"""
    Builder Pattern
    ---------------
    The builder pattern separates the construction of a complex object from its representation,
    allowing the same construction process to create different representations. It is useful when
    you want to create an object step by step or when the creation process involves multiple
    optional parameters.

    - All descriptions and comments created by ChatGPT and GitHub Copilot
"""
class Car:
    """
        Car
        ---
        The final product of the builder pattern.
    """
    def __init__(self):
        self.brand = None
        self.color = None
        self.model = None

    def __str__(self):
        return f"{self.brand} {self.color} {self.model}"

class CarBuilder:
    """
        CarBuilder
        -------
        The abstract builder class.
    """
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand: str):
        self.car.brand = brand
        return self

    def set_color(self, color: str):
        self.car.color = color
        return self

    def set_model(self, model: str):
        self.car.model = model
        return self

    def build(self):
        return self.car


if __name__ == "__main__":
    builder = CarBuilder()
    car = builder.set_brand("Ford").set_color("Red").set_model("Mustang").build()
    print(car)

"""
    Output:
    -------
    Ford Red Mustang
"""


