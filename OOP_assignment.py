# =========================================
# Assignment 1: Design Your Own Class & Polymorphism Challenge
# =========================================

# -------------------------------
# Activity 1: Designing a Smartphone Class
# -------------------------------

class Smartphone:
    def init(self, brand, model, storage, battery):
        self.brand = brand        # Brand of the phone
        self.model = model        # Model name
        self.storage = storage    # Storage in GB
        self.battery = battery    # Battery capacity in mAh

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def take_photo(self):
        print(f"{self.brand} {self.model} takes a photo! 📸")

    def battery_status(self):
        print(f"{self.brand} {self.model} has {self.battery}% battery left 🔋")


# Inheritance example: Smartphone -> GamingPhone
class GamingPhone(Smartphone):
    def init(self, brand, model, storage, battery, cooling_system):
        super().init(brand, model, storage, battery)
        self.cooling_system = cooling_system  # Extra attribute for gaming phones

    def play_game(self, game):
        print(f"{self.brand} {self.model} is playing {game} with {self.cooling_system} cooling! 🎮")


# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", 256, 80)
phone2 = GamingPhone("ASUS", "ROG Phone 7", 512, 90, "Liquid Cooling")

# Using methods
phone1.make_call("123-456-7890")
phone1.take_photo()
phone1.battery_status()

phone2.make_call("987-654-3210")
phone2.play_game("Genshin Impact")
phone2.battery_status()


# -------------------------------
# Activity 2: Polymorphism Challenge
# -------------------------------

class Vehicle:
    def move(self):
        pass  # Base method, will be overridden


class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing on water 🚤")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()