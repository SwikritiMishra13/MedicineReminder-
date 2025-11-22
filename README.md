Medicine Reminder & Tracker

This project is a beginner-friendly Python application that helps users manage their daily medicines by storing details, showing reminders, and tracking which medicines are taken.

📌 Overview

The Medicine Reminder & Tracker allows users to:

Add medicines with name, dosage, and time

View all medicines

Mark medicines as taken

Get time-based reminders


The system uses JSON file storage instead of a database, making it simple for beginners.

✨ Features

Add new medicines

Store dosage and daily schedule

View all added medicines

Mark medicine status as "taken"

Automatic reminders based on system time

File-based storage (no SQL required)


🛠 Technologies Used

Python 3

JSON for data storage

datetime module

time module


📁 Project Structure

medicine-reminder/
│
├── src/
│   ├── main.py
│   ├── reminder.py
│   ├── storage.py
│   ├── tracker.py
│   └── scheduler.py
│
├── data/
│   └── medicines.json
│
└── README.md

▶ How to Run the Project

1. Clone the repository

git clone <your-repository-link>

2. Navigate to the project folder

cd medicine-reminder

3. Run the main program

python src/main.py

🧪 Testing Instructions

Add some medicines using menu option 1

View them using option 2

Mark taken using option 3

Start the reminder system using option 4 (optional)


📷 Screenshots

(Add your screenshots here under /screenshots folder)

👩‍💻 Author

Your Name Here

📜 License

This project is for academic use.