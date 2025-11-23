import time
from datetime import datetime
from storage import load_data

def check_and_alert(medicines, now_time, notify_fn):
    """
    Check the medicines list for matches with now_time
    and call notify_fn(med) when it's time.
    """
    for med in medicines:
        if med.get("time") == now_time and med.get("status") == "pending":
            notify_fn(med)

def notify_print(med):
    """Default notify function: prints to console."""
    print(f"\n🔔 Reminder! It's time to take: {med['name']} — {med.get('dosage', '')}\n")

def start_reminder_loop():
    """Continuously checks every 30 seconds for due reminders."""
    print("\nReminder system started... (Press CTRL + C to stop)\n")

    while True:
        now = datetime.now().strftime("%I:%M %p")
        data = load_data()
        medicines = data.get("medicines", [])
        check_and_alert(medicines, now, notify_print)
        time.sleep(30)