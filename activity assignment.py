# Polymorphism Challenge 🎭
class Vehicle:
    def move(self):
        # Base method with default behavior
        print(">>>>>>Moving in some way...>>>>>>")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road__...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water...")

class Bike(Vehicle):
    def move(self):
        print("🚴 Pedaling on the path...")

# Polymorphism
# List to loop through all
vehicles = [Car(), Plane(), Boat(), Bike()]

print("\nEach vehicle moves in its own unique way:")

for vehicle in vehicles:
    vehicle.move()  # Same method name, different behavior

main_vehicle = Vehicle()
main_vehicle.move()

