from carbon_footprint import CarbonFootprint

class Bicycle(CarbonFootprint):

    def __init__(self, kilometers):
        self.kilometers = kilometers

    def get_carbon_footprint(self):
        return 0