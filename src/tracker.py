from storage import load_data, save_data

def add_medicine(name, dosage, time):
    """Adds a new medicine to the list."""
    data = load_data()
    new_item = {
        "name": name,
        "dosage": dosage,
        "time": time,
        "status": "pending"
    }
    data["medicines"].append(new_item)
    save_data(data)
    print("\nMedicine added successfully!\n")


def show_all_medicines():
    """Displays all medicines in a readable form."""
    data = load_data()

    if not data["medicines"]:
        print("\nNo medicines found.\n")
        return

    print("\n----- Medicine List -----")
    for i, med in enumerate(data["medicines"], start=1):
        print(f"{i}. {med['name']} - {med['dosage']} at {med['time']} | Status: {med['status']}")
    print("-------------------------\n")


def mark_taken(index):
    """Marks a medicine as taken."""
    data = load_data()

    if 0 <= index < len(data["medicines"]):
        data["medicines"][index]["status"] = "taken"
        save_data(data)
        print("\nMedicine marked as taken!\n")
    else:
        print("\nInvalid medicine number.\n")