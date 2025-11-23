from datetime import datetime
from storage import load_data, save_data

def valid_time_format(t):
    """Validate time in format HH:MM AM/PM."""
    try:
        datetime.strptime(t, "%I:%M %p")
        return True
    except ValueError:
        return False

def add_medicine(name, dosage, time_str):
    """Adds a new medicine to the list, after validation."""
    if not name.strip():
        print("Error: medicine name cannot be empty.")
        return
    if not dosage.strip():
        print("Error: dosage cannot be empty.")
        return
    if not valid_time_format(time_str):
        print("Error: time must be in format like 09:30 AM.")
        return

    data = load_data()
    new_item = {
        "name": name,
        "dosage": dosage,
        "time": time_str,
        "status": "pending"
    }
    data["medicines"].append(new_item)
    save_data(data)
    print("\nMedicine added successfully!\n")

def show_all_medicines():
    """Displays all medicines."""
    data = load_data()
    if not data["medicines"]:
        print("\nNo medicines found.\n")
        return

    print("\n----- Medicine List -----")
    for i, med in enumerate(data["medicines"], start=1):
        print(f"{i}. {med['name']} - {med['dosage']} at {med['time']} | Status: {med['status']}")
    print("-------------------------\n")

def mark_taken(index):
    """Marks a medicine as taken by index."""
    data = load_data()
    if 0 <= index < len(data["medicines"]):
        data["medicines"][index]["status"] = "taken"
        save_data(data)
        print("\nMedicine marked as taken!\n")
    else:
        print("\nInvalid medicine number.\n")