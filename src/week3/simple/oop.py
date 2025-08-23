"""
Assignment 1: Smartphone Class with Inheritance

This program demonstrates how to create a class with attributes, methods,
constructors, inheritance, and encapsulation.
"""


class Smartphone:
    """A class representing a generic smartphone."""

    def __init__(self, brand: str, model: str, storage: int, battery: int):
        """
        Constructor to initialize a smartphone.

        Args:
            brand (str): Brand of the smartphone.
            model (str): Model of the smartphone.
            storage (int): Storage capacity in GB.
            battery (int): Battery percentage (0–100).
        """
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery = battery  # Encapsulated attribute (private)

    def charge(self, amount: int):
        """Charge the smartphone battery."""
        self.__battery = min(100, self.__battery + amount)
        print(f"{self.model} charged. Battery now: {self.__battery}%")

    def use(self, hours: int):
        """Simulate phone usage that drains the battery."""
        self.__battery = max(0, self.__battery - hours * 10)
        print(f"{self.model} used for {hours} hours. Battery now: {self.__battery}%")

    def get_battery(self) -> int:
        """Return the current battery level."""
        return self.__battery


# Subclass with inheritance
class iPhone(Smartphone):
    """A class representing an iPhone, inheriting from Smartphone."""

    def __init__(self, model: str, storage: int, battery: int, ios_version: str):
        """Initialize iPhone with iOS version in addition to smartphone attributes."""
        super().__init__("Apple", model, storage, battery)
        self.ios_version = ios_version

    # Polymorphism: override use() method
    def use(self, hours: int):
        """iPhones consume less battery for the same hours."""
        self._Smartphone__battery = max(
            0, self._Smartphone__battery - hours * 5)
        print(f"{self.model} (iOS {self.ios_version}) used for {hours} hours. Battery now: {self._Smartphone__battery}%")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 80)
phone1.use(3)
phone1.charge(15)

iphone1 = iPhone("iPhone 14", 256, 90, "iOS 17")
iphone1.use(3)
