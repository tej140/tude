# Initialize an empty dictionary for student grades
student_grades = {}

while True:
    print("\nOptions:")
    print("1. Add a new student")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Add a new student
        name = input("Enter student's name: ")
        grade = input("Enter student's grade: ")
        if name in student_grades:
            print(f"{name} already exists. Use update option to change the grade.")
        else:
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")

    elif choice == "2":
        # Update existing student's grade
        name = input("Enter student's name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"{name} does not exist. Use add option to add the student first.")

    elif choice == "3":
        # Print all student grades
        if student_grades:
            print("\nStudent Grades:")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")
        else:
            print("No student grades available.")

    elif choice == "4":
        # Exit the program
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

