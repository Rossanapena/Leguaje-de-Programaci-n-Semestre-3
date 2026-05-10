from carbon_footprint import CarbonFootprint

class Building(CarbonFootprint):

    def __init__(self, electricity_use):
        self.electricity_use = electricity_use

    def get_carbon_footprint(self):
        return self.electricity_use * 0.5