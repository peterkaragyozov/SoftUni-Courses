class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        needed_fuel = kilometers * self.fuel_consumption
        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel

