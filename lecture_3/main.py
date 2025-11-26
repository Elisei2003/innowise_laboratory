def calculate_average(grades):
    """Calculates the average of a list of grades, handling empty lists."""
    if not grades:
        return None  # Use None to signify "N/A" or zero grades
    return sum(grades) / len(grades)


def add_student(students):
    """Option 1: Adds a new student to the list."""
    name = input("Enter the new student's name: ").strip()

    if not name:
        print("Error: Name cannot be empty.")
        return

    # Проверяем, содержит ли имя только буквы (игнорируя пробелы
    if not name.replace(' ', '').isalpha():
        print("Error: Name must contain only letters and spaces.")
        return

    # Check if student already exists
    if any(student['name'] == name for student in students):
        print(f"Student '{name}' already exists.")
        return

    students.append({"name": name, "grades": []})
    print(f"Student '{name}' added successfully.")


def add_grades(students):
    """Option 2: Adds grades for an existing student."""
    name = input("Enter the name of the student to add grades for: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    # Find the student
    target_student = None
    for student in students:
        if student['name'] == name:
            target_student = student
            break

    if not target_student:
        print(f"Error: Student '{name}' not found.")
        return

    print(f"Enter grades for {name}. Enter 'done' to finish.")

    while True:
        grade_input = input("Enter grade (0-100) or 'done': ").strip().lower()

        if grade_input == 'done':
            break

        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                target_student['grades'].append(grade)
                print(f"Grade {grade} added for {name}.")
            else:
                print("Error: Grade must be between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number or 'done'.")


def show_report(students):
    """Option 3: Shows individual reports and overall summary."""
    if not students:
        print("No students have been added yet.")
        return

    print("\n--- Student Grade Report ---")

    # Calculate averages and store them temporarily for summary calculation
    student_averages = []
    has_grades_data = False

    for student in students:
        avg = calculate_average(student['grades'])

        if avg is not None:
            print(f"{student['name']}'s average grade is {avg:.1f}")
            student_averages.append(avg)
            has_grades_data = True
        else:
            # Handle ZeroDivisionError case (student has no grades)
            print(f"{student['name']}'s average grade is N/A")

    if not has_grades_data:
        print("No grades have been recorded for any student.")
        return

    # Calculate Summary Statistics
    max_avg = max(student_averages)
    min_avg = min(student_averages)
    overall_avg = sum(student_averages) / len(student_averages)

    print("\n--- Overall Summary ---")
    print(f"Max Average Grade: {max_avg:.1f}")
    print(f"Min Average Grade: {min_avg:.1f}")
    print(f"Overall Average Grade (of students with grades): {overall_avg:.1f}")


def find_top_performer(students):
    """Option 4: Finds and prints the student with the highest average grade."""

    # Filter out students who have no grades, as they cannot be compared meaningfully
    students_with_grades = [
        student for student in students if student['grades']
    ]

    if not students_with_grades:
        print("No students with recorded grades to compare.")
        return

    # Use max() with a lambda function based on the calculated average
    # We use calculate_average inside the lambda key
    top_student = max(
        students_with_grades,
        key=lambda student: calculate_average(student['grades'])
    )

    top_avg = calculate_average(top_student['grades'])

    print(f"The top performer is {top_student['name']} with an average grade of {top_avg:.1f}.")


def display_menu():
    """Displays the main menu options."""
    print("\n===== Student Grade Analyzer =====")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")
    print("==================================")


def main():
    """Main function to run the Student Grade Analyzer program."""
    students = []  # Step 1: Initialize the list of student dictionaries

    while True:  # Step 2: Main Program Loop
        display_menu()

        try:
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                add_student(students)

            elif choice == '2':
                add_grades(students)

            elif choice == '3':
                show_report(students)

            elif choice == '4':
                find_top_performer(students)

            elif choice == '5':
                print("Exiting the Student Grade Analyzer. Goodbye!")
                break  # Step 5: Exit

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except Exception as e:
            # General error handling for unexpected issues
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
