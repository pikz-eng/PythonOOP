from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if not brand:
            raise ValueError('brand cannot be empty')
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if not model:
            raise ValueError('model cannot be empty')
        self.__model = model

    @abstractmethod
    def movement(self):
        pass

    def describe(self):
        return f'{self.__brand} {self.__model}'


class Car(Vehicle):
    def __init__(self, brand, model, nr_wheels):
        super().__init__(brand, model)
        self.__nr_wheels = nr_wheels

    @property
    def nr_wheels(self):
        return self.__nr_wheels

    @nr_wheels.setter
    def nr_wheels(self, nr_wheels):

        if nr_wheels <= 0:
            raise ValueError('nr_wheels cannot be negative')
        self.__nr_wheels = nr_wheels

    def movement(self):
        return "The car is on road"

    def describe(self):
        return f'{self.brand} {self.model}, with {self.__nr_wheels} wheels'

class Bicycle(Vehicle):
        def __init__(self, brand, model, type):
            super().__init__(brand, model)
            self.__type = type

        @property
        def type(self):
            return self.__type

        @type.setter
        def type(self, type):
            if not type:
                raise ValueError('type cannot be empty')
            self.__type = type

        def movement(self):
            return "The bicycle travels on cycle paths "

        def describe(self):
            return f' The Bicycle{self.brand} {self.model}, type {self.type}'


class Motorcycle(Vehicle):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.__power = power

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        if power <= 0:
            raise ValueError('power cannot be negative')
        self.__power = power


    def movement(self):
        return "The motorcycle is so fasttt!!! "


    def describe(self):
        return f'Motorcycle{self.brand} {self.model}, with  {self.power} horse power '


def main():

    vehicle1 = Car("Dacia", "Logan",4)
    vehicle2 =  Bicycle("Trek", "Marlin","mountain")
    vehicle3 = Motorcycle("Yamaha", "YZF", 120)

    vehicle = [vehicle1, vehicle2, vehicle3]

    for vehicle in vehicle:
        print(vehicle.describe())
        print(vehicle.movement())
        print()





if __name__ == '__main__':
    main()





