Medicine Reminder

1. Problem Statement

Many people forget to take their medicines on time, especially when managing multiple prescriptions.
This project aims to provide a simple reminder system that helps users track medicine schedules.


2. Scope

The system allows users to store medicine details locally.

It provides basic operations: add, view, and schedule reminders.

Works completely offline and requires no database.

Small-scale, beginner-friendly project suitable for academic learning


3. Target Users

Students learning Python

Elderly people needing simple reminders

Anyone who wants a basic medicine notification system


4. High-Level Features

Add medicine information

View all medicines

Daily automated reminders

JSON-based file storage

Simple command-line interface

## Functional Modules

1. Medicine Management (tracker.py)
   - Add new medicine (name, dosage, time)
   - Edit / delete medicine
   - Mark medicine as taken

2. Storage & Data Handling (storage.py)
   - Read/write medicine data to data/medicines.json
   - Provide functions: load_data(), save_data()

3. Reminder Scheduling (scheduler.py & reminder.py)
   - Start a loop to check scheduled times
   - Trigger console reminders and log status

   # Non-Functional Requirements

1. Performance
   - Scheduler checks reminders every 1 second.
   - Operations (add/view/mark) must respond within 2 seconds.

2. Usability
   - Console menu with numbered options and clear prompts.
   - Simple messages and confirmations for actions.

3. Reliability
   - Medicine data persists in data/medicines.json.
   - Graceful handling of missing data file.

4. Maintainability
   - Modular code (tracker, storage, scheduler).
   - Documented functions and comments.

5. Error Handling
   - Validate user input and handle exceptions during file IO.