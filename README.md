Medicine Reminder – Python Project

📌 Overview

This is a simple console-based Medicine Reminder application.
It allows users to add medicines, view their list, and run a daily reminder schedule.
The project is designed to follow the basic principles of modular programming and file handling.


✨ Features

1. Add medicine details (name, dosage, time)
2. View all added medicines
3. Daily reminder scheduling using the schedule library
4. JSON-based storage (no database required)
5. Simple and beginner-friendly file structure

🧩 Technologies Used

1. Python 3
2. Schedule library (for reminders)
3. JSON for storing data

📁 Project Structure

medicine-reminder-project/
│
├── data/
│   └── medicines.json
│
├── src/
│   ├── main.py
│   ├── reminder.py
│   ├── scheduler.py
│   ├── storage.py
│   ├── tracker.py
│   └── utils/
│       ├── helper.py
│       └── validator.py
│
├── tests/
├── README.md
├── statement.md
└── requirements.txt

⚙ Installation & Running

Step 1. — Install dependencies:
    pip install -r requirements.txt

Step 2 — Run the project:
    cd src
    python main.py

📝 How to Use

1. Choose 1 to add a medicine
2. Choose 2 to view saved medicines
3. Choose 3 to start the reminder scheduler
4. Press Ctrl + C to stop the scheduler

🧪 Testing Instructions

1. Add 2–3 medicines
2. Restart the program and verify they are still saved
3. Start the scheduler at the correct time and see reminders

### Input / Output Examples

1. Add medicine
   - Input: name (string), dosage (string), time (string, e.g. 09:30 AM)
   - Output: "Medicine added successfully." and entry saved to data/medicines.json

2. View medicines
   - Input: choose '2' in menu
   - Output: printed list with index, name, dosage, time, status

3. Mark taken
   - Input: choose '3', then enter medicine index
   - Output: status updated to "taken" in JSON and confirmation printed

4. Start reminders
   - Input: choose '4'
   - Output: scheduler starts; when time matches shows "Reminder: Take <name> — <dosage>"