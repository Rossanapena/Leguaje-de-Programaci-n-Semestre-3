import json

def save_data(objects, filename):

    data = []

    for obj in objects:
        data.append({
            "type": type(obj).__name__,
            "carbon_footprint": obj.get_carbon_footprint()
        })

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)