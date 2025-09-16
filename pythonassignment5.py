
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def charge(self):
        print(f"{self.brand} {self.model} is charging... 🔋")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB, Battery: {self.battery_life}mAh")


# Adding an inheritance layer (Polymorphism/Encapsulation example)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system

    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} 🎮 with {self.cooling_system} cooling system!")


class Vehicle:
    def move(self):
        print("The vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Test the classes
if __name__ == "__main__":
    # Test Smartphone
    phone1 = Smartphone("Samsung", "S23", 256, 4500)
    phone1.info()
    phone1.call("+254113800683")
    phone1.charge()

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 512, 6000, "liquid cooling")
    gaming_phone.info()
    gaming_phone.play_game("Call of Duty Mobile")

    print("\n--- Polymorphism Challenge ---")
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        v.move()

