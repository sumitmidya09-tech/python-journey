class vehicle:
    def general_usage(self):
        print("general use: transport")
class car(vehicle):
    def __init__(self):
        print("i'm a car")
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        print("specific use: commute to work , vacation with family")

class motorcycle(vehicle):
    def __init__(self):
        print("i'm a motor cycle")
        self.wheels = 4
        self.has_rof = True

    def specific_usage(self):
        print("specific use: motorcycle to go work ")
m=motorcycle()
m.general_usage()
m.specific_usage()

c=car()
c.general_usage()
c.specific_usage()

#inheritance is isinstance and issubclass

print(isinstance(c,car))
print(isinstance(m,motorcycle))
print(isinstance(m,car))


print(issubclass(car,vehicle))
print(issubclass(car,motor
