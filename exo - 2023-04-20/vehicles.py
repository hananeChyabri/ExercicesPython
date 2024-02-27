class Vehicle:

    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
    
    def ride(self, duration):
        travel = self.speed * duration
        self.distance += travel


class Bike(Vehicle):

    def __init__(self):
        super().__init__(15)

class Car(Vehicle):

    def __init__(self):
        super().__init__(100)


bike = Bike()
car = Vehicle(100)

bike.ride(2)
car.ride(2)

print(f"Distance parcourue avec le vélo: {bike.distance} km.")
print(f"Distance parcourue avec la voiture: {car.distance} km.")