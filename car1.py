class Car:
    name = ""
    color = ""
    model = ""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("Name: ", self.name)
        print("Color: ", self.color)
        print("Starting the engine.")
 
#creating car object
my_car = Car("Corolla","silver")
""" my_car.name = "Allion"
my_car.color = "white"
 """

""" Car.name = "Axio"
Car.color = "Black" """
""" print("Name: ", my_car.name)
print("Color: ", my_car.color) """
my_car.start()
#print(dir(Car))