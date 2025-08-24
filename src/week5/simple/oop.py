# Smartphone class with inheritance

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")

    def info(self):
        print(
            f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")

# Inheritance: GamingSmartphone extends Smartphone


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def play_game(self, game):
        print(
            f"{self.brand} {self.model} is playing {game} 🎮 with {self.cooling_system} cooling system!")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", 256)
phone1.info()
phone1.call("0712345678")

gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 512, "liquid")
gaming_phone.info()
gaming_phone.play_game("PUBG Mobile")
