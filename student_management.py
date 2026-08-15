import json
import os

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "students.json"
)
print("JSON FILE:", FILE_NAME)

def load_students():
    """Load student records from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

def save_students(students):
    """Save student records to JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Error: Unable to save student data.")

students = load_students()

print("Student Management System Started!")
print(f"Total students: {len(students)}")

# Student Class
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "marks": self.marks
        }

# Add Student
def add_student():
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return
    try:
        marks = float(input("Enter Student Marks: "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid marks.")
        return
    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists.")
            return
    new_student = Student(student_id, name, marks)
    students.append(new_student.to_dict())
    save_students(students)
    print("Student added successfully!")

# Update Student
def update_student():
    student_id = input("Enter Student ID to update: ").strip()
    for student in students:
        if student["student_id"] == student_id:
            new_name = input("Enter new name: ").strip()
            if not new_name:
                print("Student name cannot be empty.")
                return
            try:
                new_marks = float(input("Enter new marks: "))
                if new_marks < 0 or new_marks > 100:
                    print("Marks must be between 0 and 100.")
                    return
            except ValueError:
                print("Please enter valid marks.")
                return
            student["name"] = new_name
            student["marks"] = new_marks
            save_students(students)
            print("Student updated successfully!")
            return
    print("Student not found.")

# Delete Student
def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return
    print("Student not found.")

# Search Student
def search_student():
    search = input("Enter Student ID or Name to search: ").strip().lower()

    found = False

    for student in students:
        if (
            student["student_id"].lower() == search
            or student["name"].lower() == search
        ):
            print("\nStudent Found!")
            print("----------------------")
            print(f"Student ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print("----------------------")

            found = True

    if not found:
        print("Student not found.")

# Calculate Grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Show Grade
def show_grade():
    student_id = input("Enter Student ID: ").strip()
    for student in students:
        if student["student_id"] == student_id:
            grade = calculate_grade(student["marks"])

            print("\nStudent Grade")
            print("----------------------")
            print(f"Student ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print(f"Grade: {grade}")
            print("----------------------")
            return

    print("Student not found.")

# Display Student Records
def display_students():
    if not students:
        print("No student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:
        grade = calculate_grade(student["marks"])

        print(f"Student ID : {student['student_id']}")
        print(f"Name       : {student['name']}")
        print(f"Marks      : {student['marks']}")
        print(f"Grade      : {grade}")
        print("-------------------------------------")

# Main Menu
def main_menu():
    while True:
        print("\n========================================")
        print("   SMART STUDENT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Calculate Grade")
        print("6. Display All Students")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            search_student()
        elif choice == "5":
            show_grade()
        elif choice == "6":
            display_students()
        elif choice == "7":
            print("Thank you for using the Student Management System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Start Program
main_menu()