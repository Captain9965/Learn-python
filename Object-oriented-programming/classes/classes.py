class Car:
    def __init__(self, model, name, engine_cc):
        self.name = name
        self.brand = model
        self.engine_capacity = engine_cc
        pass
    def get_model(self):
        return self.name
    def get_engine_cc(self):
        return self.engine_capacity
    def get_brand(self):
        return self.brand
if __name__ == "__main__":
    mycar = Car("Toyota", "Land Cruiser", 1800)
    print("The brand I got is a ",mycar.get_model(), "And the brand is ", mycar.get_brand())
