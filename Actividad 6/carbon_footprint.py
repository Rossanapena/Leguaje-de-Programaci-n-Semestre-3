from abc import ABC, abstractmethod

class CarbonFootprint(ABC):

    @abstractmethod
    def get_carbon_footprint(self):
        pass