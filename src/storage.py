import json
import os

DATA_FILE = "data/medicines.json"

def load_data():
    """Loads medicine data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {"medicines": []}

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    """Saves medicine data to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)