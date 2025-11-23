Medicine Reminder – Project Statement

1. Problem Statement

Many individuals—especially elderly patients or those managing multiple prescriptions—often forget to take their medicines on time. Missing doses can reduce treatment effectiveness or cause health complications.
This project aims to build a simple, offline, command-line-based medicine reminder system that helps users store their medicine schedules and receive timely notifications.


---

2. Scope

The system is designed to be lightweight, user-friendly, and suitable for academic learning. Its scope includes:

Adding, viewing, editing, and deleting medicine details.

Storing medicine information locally using a JSON file.

Running an automated reminder loop.

No external databases or internet required.

Designed for beginners and small-scale use.



---

3. Target Users

Students learning Python and file handling.

Elderly people needing a simple reminder tool.

Anyone wanting a basic medicine tracking system without installing apps.



---

4. High-Level Features

Add new medicine (name, dosage, time).

View all stored medicines.

Mark medicines as taken.

Automatic time-based reminders.

Local JSON storage.

Simple command-line interface.



---

5. Functional Modules

1. Medicine Management (tracker.py)

Add medicine (name, dosage, schedule time).

Edit existing medicine details.

Delete a medicine.

Mark medicine as taken.

Display list of all medicines.


2. Storage & Data Handling (storage.py)

Read and write data to:
data/medicines.json

Main functions:
load_data() – loads stored information
save_data(data) – updates JSON file


3. Reminder Scheduling (scheduler.py & reminder.py)

A continuous loop that checks the current time.

Matches medicines with scheduled times.

Prints console reminders.

Ensures reminders trigger once per scheduled time.



---

6. Non-Functional Requirements

1. Performance

Scheduler checks reminders every 1 second.

Menu actions (add/view/edit) respond within 1–2 seconds.


2. Usability

Simple, numbered menu interface.

Clear prompts and confirmations.

Beginner-friendly wording.


3. Reliability

Data persists across runs using JSON storage.

Handles missing or corrupted data files gracefully.


4. Maintainability

Modular code with separate files for tracking, scheduling, and storage.

Clean, readable code with comments.


5. Error Handling

Validates user input (time format, empty fields, etc.)

Handles file read/write exceptions.

Prevents duplicate or invalid medicine entries.