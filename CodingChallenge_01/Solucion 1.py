class Vehicle():
    def __init__(self, brand, model, rentalRateperDay):
        self._brand = brand
        self._model = model
        self._rentalRateperDay = rentalRateperDay

    def calculateRentalCost(self, days):
        pass

    def getDescription(self):
        return(f'{self._brand} {self._model}, ({self.__class__.__name__})')


class Car(Vehicle):
    def __init__(self, brand, model, rentalRateperDay,seats):
        super().__init__(brand, model, rentalRateperDay)
        self._seats = seats

    def calculateRentalCost(self, days):
        totalCost = self._rentalRateperDay * days
        return totalCost

class Truck(Vehicle):
    def __init__(self, brand, model, rentalRateperDay, cargoWeight):
        super().__init__(brand, model, rentalRateperDay)
        self._rentalRateperDay = rentalRateperDay
        self._cargoWeight = cargoWeight

    def calculateRentalCost(self, days):
       totalCost = (self._rentalRateperDay * days) + (self._cargoWeight * 50)
       return totalCost

class Motorcycle(Vehicle):
    def __init__(self, brand, model, rentalRateperDay, helmetIncluded):
        super().__init__(brand, model, rentalRateperDay)
        self._helmetIncluded = helmetIncluded

    def calculateRentalCost(self, days):
        totalCost = self._rentalRateperDay * days
        if self._helmetIncluded:
            totalCost += 10
        return totalCost

Toyota = Car("Toyota","Corolla",40,5)
Volvo = Truck("Volvo","FH16",80,2)
Yamaha = Motorcycle("Yamaha","R15",30,True)

print(f"{Toyota.getDescription()} -- Total Cost: {Toyota.calculateRentalCost(3)}")
print(f"{Volvo.getDescription()} -- Total Cost: {Volvo.calculateRentalCost(2)}")
print(f"{Yamaha.getDescription()} -- Total Cost: {Yamaha.calculateRentalCost(1)}")
