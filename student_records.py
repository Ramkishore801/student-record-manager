records = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        records[name] = marks
        print("Student added successfully")

    elif choice == "2":
        print("\nStudent Records:")
        for name, marks in records.items():
            print(name, ":", marks)

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
