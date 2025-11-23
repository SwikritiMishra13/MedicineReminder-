import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "medicines.json")

def load_data():
    """Load all medicine data from JSON file."""
    if not os.path.exists(DATA_FILE):
        return {"medicines": []}

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    """Save medicine data to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)