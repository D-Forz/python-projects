class Vehicle:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
    
    def __str__(self) -> str:
        return f"Vehicle Object: color= {self.color}, wheels= {self.wheels}"

class Car(Vehicle):
    def __init__(self, color, wheels, velocity):
        #Vehicle.__init__(self, color, wheels)
        super().__init__(color, wheels)
        self.velocity = velocity
    
    def __str__(self) -> str:
        return f"{super().__str__()}, type= Car, Velocity(km/hr)= {self.velocity}"

class Bicycle(Vehicle):
    def __init__(self, color, wheels, type):
        super().__init__(color, wheels)
        self.type = type
    def __str__(self) -> str:
        return f"{super().__str__()}, type = {self.type}"

new_car = Car("red", 4, 100)
print(new_car)

#MRO - Method Resolutin Order
print(Bicycle.mro())