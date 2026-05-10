from car import Car
from building import Building
from bicycle import Bicycle

objects = [
    Car(20),
    Building(100),
    Bicycle(15)
]

for obj in objects:
    print(type(obj).__name__)
    print("Carbon Footprint:", obj.get_carbon_footprint())
    print("-------------------")