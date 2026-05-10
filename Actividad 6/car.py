from carbon_footprint import CarbonFootprint

class Car(CarbonFootprint):

    def __init__(self, fuel_consumption):
        self.fuel_consumption = fuel_consumption

    def get_carbon_footprint(self):
        return self.fuel_consumption * 2.3