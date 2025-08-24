class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = 0  # Encapsulated attribute
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")
    
    def get_mileage(self):
        return self._mileage
    
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
    
    def move(self):
        self._mileage += 10
        return "Driving 🚗"
    
    def honk(self):
        return "Beep beep! 🎵"

class Airplane(Vehicle):
    def __init__(self, brand, model, year, wingspan):
        super().__init__(brand, model, year)
        self.wingspan = wingspan
    
    def move(self):
        self._mileage += 500
        return "Flying ✈️"
    
    def take_off(self):
        return "Taking off! 🛫"

class Boat(Vehicle):
    def __init__(self, brand, model, year, boat_type):
        super().__init__(brand, model, year)
        self.boat_type = boat_type
    
    def move(self):
        self._mileage += 30
        return "Sailing ⛵"
    
    def anchor(self):
        return "Dropping anchor! ⚓"

# Demonstration of polymorphism
def demonstrate_vehicles():
    vehicles = [
        Car("Toyota", "Camry", 2022, "Hybrid"),
        Airplane("Boeing", "737", 2020, 117),
        Boat("Beneteau", "Oceanis", 2021, "Sailboat")
    ]
    
    print("Vehicle Movement Demonstration:\n")
    for vehicle in vehicles:
        print(f"{vehicle}:")
        print(f"  Movement: {vehicle.move()}")
        print(f"  Mileage: {vehicle.get_mileage()} units")
        
        # Class-specific methods
        if isinstance(vehicle, Car):
            print(f"  Sound: {vehicle.honk()}")
        elif isinstance(vehicle, Airplane):
            print(f"  Action: {vehicle.take_off()}")
        elif isinstance(vehicle, Boat):
            print(f"  Action: {vehicle.anchor()}")
        
        print()

# Run the demonstration
if __name__ == "__main__":
    demonstrate_vehicles()