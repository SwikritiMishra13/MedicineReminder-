import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(_file_)))
DATA_FILE = os.path.join(BASE_DIR, "data", "medicines.json")

def load_data():
    """Load data from JSON file, with error handling."""
    if not os.path.exists(DATA_FILE):
        return {"medicines": []}

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # If file is corrupted, back it up and reset
        try:
            os.rename(DATA_FILE, DATA_FILE + ".bak")
        except Exception:
            pass
        return {"medicines": []}

def save_data(data):
    """Save medicine data to JSON file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error saving data:", e)