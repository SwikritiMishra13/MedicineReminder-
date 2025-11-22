import time
from datetime import datetime
from storage import load_data

def start_reminder_loop():
    """Checks every 30 seconds if it's time to remind the user."""
    print("\nReminder system started... (Press CTRL + C to stop)\n")

    while True:
        now = datetime.now().strftime("%I:%M %p")
        data = load_data()

        for med in data["medicines"]:
            if med["time"] == now and med["status"] == "pending":
                print("\n🔔 Reminder! It's time to take:", med["name"])
        
        time.sleep(30)