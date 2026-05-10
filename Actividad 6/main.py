from car import Car
from building import Building
from bicycle import Bicycle
from file_manager import save_data

objects = [
    Car(20),
    Building(100),
    Bicycle(15)
]

for obj in objects:
    print(type(obj).__name__)
    print("Carbon Footprint:", obj.get_carbon_footprint())
    print("-------------------")

save_data(objects, "Actividad 6/data/carbon_data.json")

print("Datos guardados en JSON correctamente.")