💊 Medicine Reminder – Python Project

A simple and beginner-friendly console-based Medicine Reminder System built using Python. It allows users to store medicines, track their status, and receive time-based reminders — all without using any external database.


---

📌 Overview

This project helps users manage their daily medicines by allowing them to:

✔ Add medicines with name, dosage, and time
✔ View all saved medicines
✔ Mark medicines as taken
✔ Receive timed reminders
✔ Store everything in a JSON file

The project follows modular programming, proper folder structure, documentation, and includes unit testing to meet academic project standards.


---

✨ Features

✅ 1. Add Medicines

Enter name, dosage, and time in AM/PM format.

✅ 2. View Medicines

Displays all medicines with status (pending/taken).

✅ 3. Mark Medicine as Taken

Updates status inside the JSON file.

✅ 4. Daily Reminder System

Checks time and alerts user when it’s time to take a medicine.

✅ 5. JSON Storage

No database required — medicines are saved locally.

✅ 6. Modular Code Structure

Separated into tracker, scheduler, reminder, storage, utils, etc.

✅ 7. Unit Tests Included

Basic tests for major functional modules.


---

🧩 Technologies & Tools Used

Python 3

schedule (for reminder scheduling)

json (for storage)

unittest (for testing)

Git & GitHub (version control)



---

📁 Project Structure

medicine-reminder-project/
│
├── data/
│   └── medicines.json
│
├── diagrams/
│   ├── class_diagram.jpg
│   ├── sequence_diagram.jpg
│   ├── workflow.jpg
│   ├── use_case.jpg
│   └── schema.md
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
│   ├── test_add_medicine.py
│   ├── test_mark_taken.py
│   ├── test_view_medicines.py
│   ├── test_storage.py
│   └── test_scheduler.py
│
├── README.md
├── statement.md
└── requirements.txt


---

⚙ Installation & Running

Step 1 — Install dependencies

pip install -r requirements.txt

Step 2 — Run the project

cd src
python main.py


---

📝 How to Use

1. Add Medicine

Enter:

Name

Dosage

Time (e.g., 09:30 AM)


Output:

Medicine added successfully!


---

2. View Medicines

Choose option 2

Shows:

1. Paracetamol – 500mg at 09:30 AM | Status: pending


---

3. Mark Medicine as Taken

Choose option 3
Enter index
Updates status to taken.


---

4. Start Reminders

Choose option 4
The system begins checking time every 30 seconds.

If time matches:

🔔 Reminder! It's time to take: Paracetamol


---

🧪 Testing Instructions

Run all tests

pytest

Tests include:

Add medicine

View medicines

Mark taken

Storage load/save

Scheduler structure



---

🎯 Input / Output Examples

Add Medicine

Input: name, dosage, time
Output: "Medicine added successfully."

View Medicines

Shows indexed list with name, dosage, time, status.

Mark Taken

Status updated in JSON.

Start Reminders

Prints reminder message when time matches.