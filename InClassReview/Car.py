class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
def main():
    Car0 = Car("Ford", "F-150")
    Car1 = Car("Toyota", "Camry")
    Car1.make = "Chevrolet"
    print(Car1.make)
    print(Car0.make)

main()