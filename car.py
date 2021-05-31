class Car:
    name = ""
    color = ""
    model = ""

    def start(self):
        print("Starting the engine.")
 
#creating car object
my_car = Car()
my_car.name = "Allion"
my_car.color = "white"


""" Car.name = "Axio"
Car.color = "Black" """
print("Name: ", my_car.name)
print("Color: ", my_car.color)
my_car.start()
#print(dir(Car))