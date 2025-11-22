from tracker import add_medicine, show_all_medicines, mark_taken
from scheduler import start_reminder_loop

def main():
    while True:
        print("==== Medicine Reminder System ====")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Mark Medicine as Taken")
        print("4. Start Reminder")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter medicine name: ")
            dosage = input("Enter dosage: ")
            time = input("Enter time (Ex: 09:00 AM): ")
            add_medicine(name, dosage, time)

        elif choice == "2":
            show_all_medicines()

        elif choice == "3":
            show_all_medicines()
            num = int(input("Enter medicine number to mark taken: "))
            mark_taken(num - 1)

        elif choice == "4":
            start_reminder_loop()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")


if _name_ == "_main_":
    main()