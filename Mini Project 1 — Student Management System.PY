students_list = []
while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student\n2. Show Students\n3. Exit")
    choice = input("Enter option (1/2/3): ")
    if choice == "1":
        name = input("Enter student name: ")
        students_list.append(name)
        print(f"{name} has been added successfully!")
    elif choice == "2":
        if not students_list:
            print("No students registered yet.")
        else:
            print("Registered Students:")
            for s in students_list:
                print(f"- {s}")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")
    