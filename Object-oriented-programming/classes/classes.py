
"""
    This is a basic class definition with a parametized constructor

"""
#This is the base class or super class:
class Car:
    #static objects:
    productionNumber = 0
    def __init__(self, name):
        #it is python conventions to use the underscore to declare protected members:
        self._name = name
        #use the double underscore to declare private members:
        self.__serial_number = 110
        #increment static variable productionNumber:
        Car.productionNumber = Car.productionNumber + 1
        self.number = Car.productionNumber
        pass
    def get_name(self):
        return self._name
    def get_serialNumber(self):
        return self.__serial_number
    def get_productionNumber(self):
        return self.number

    #static class methods:
    #The static method decorator can also be used to make a class method static and callable by the objects:
    @staticmethod
    def get_current_production():
        return Car.productionNumber

"""
    class inheritance: 
        This is the process by which new classes called derived classes are created from existing classes called base classes.

"""
class Model(Car):
    def __init__(self, model, name, engine_cc):
        #calling the base class constructor:
        super().__init__(model)
        #modifying the base class protected member name:
        self._name = "Nissan"
        self.model = model
        self.engine_cc = engine_cc
    def get_model(self):
        return self.model
    def get_engine_cc(self):
        return self.engine_cc

if __name__ == "__main__":
    print("-----------------Normal class instantiation:-----------------")
    mycar = Car("Toyota")
    print("The brand I got is a ",mycar.get_name())

    print("-------------------Class inheritance:-------------------------")
    #using the derived class:
    mycar = Model("Toyota","Land Cruiser", 4600)
    print(" The model of the car is: ",mycar.get_model())

    print("------------------protected variables in python----------------")
    #Accessing the modified protected member outside its class:
    print("The new car brand I got is the: ", mycar.get_name())

    print("----------------How to accss private members:------------ ")
    print("The serial number of my car is-> ", mycar.get_serialNumber())

    print("-----------------Static members-------------------------------")
    print("This is the production number of car 1: ", mycar.get_productionNumber())

    mySecondCar = Model("Toyota","Prado", 2800)
    print("This is the production number of car 2: ", mySecondCar.get_productionNumber())

    #using staticmethod() function to define a static function: 
    # Car.get_current_production = staticmethod(Car.get_current_production)

    print("This is the current production level: ", mycar.get_current_production())

