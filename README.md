# InternGrow Student Management System

A console-based Smart Student Management System developed in Python as part of the InternGrow Python Programming Internship.

## 📌 Project Overview

The Smart Student Management System is a Python-based application designed to manage student records efficiently. It allows users to add, update, delete, search, and display student information while automatically calculating student grades.

Student data is stored persistently in a JSON file, so records remain available even after the application is closed.

## ✨ Features

- Add new student records
- Update existing student records
- Delete student records
- Search students by ID or name
- Calculate student grades automatically
- Display all student records
- JSON-based data storage
- Input validation
- Exception handling
- Duplicate Student ID validation
- Menu-driven interface
- Object-Oriented Programming (OOP)

## 🛠️ Technologies Used

- Python
- JSON
- Object-Oriented Programming (OOP)
- File Handling
- Exception Handling

## 📂 Project Structure

```text
InternGrow_StudentManagementSystem/
│
├── student_management.py
├── students.json
└── README.md
```

### `student_management.py`

Contains the complete Python application, including student management functions, grade calculation, validation, and the menu-driven interface.

### `students.json`

Stores student records in JSON format for persistent data storage.

### `README.md`

Contains project documentation, features, technologies, and setup instructions.

## 📊 Grade System

| Marks | Grade |
|---|---|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your system.

### 2. Clone the Repository

```bash
git clone https://github.com/IrsaAttiqueCyber/InternGrow_StudentManagementSystem.git
```

### 3. Open the Project Folder

```bash
cd InternGrow_StudentManagementSystem
```

### 4. Run the Application

```bash
python student_management.py
```

## 🖥️ Application Menu

The application provides the following options:

```text
1. Add Student
2. Update Student
3. Delete Student
4. Search Student
5. Calculate Grade
6. Display All Students
7. Exit
```

## 🔐 Input Validation & Error Handling

The application validates:

- Student marks between 0 and 100
- Empty student names
- Duplicate Student IDs
- Invalid numeric input
- Missing or corrupted JSON files
- File read/write errors

## 💾 Data Storage

Student records are stored in `students.json`.

Example:

```json
[
    {
        "student_id": "101",
        "name": "Ali",
        "marks": 85.0
    }
]
```

## 🚀 Future Improvements

Possible future improvements include:

- Graphical User Interface (GUI)
- Database integration
- User authentication
- Advanced reporting
- Export to Excel/PDF
- Attendance management
- Enhanced search and filtering

## 🎓 Internship

This project was developed as **Task 1 — Smart Student Management System** for the **InternGrow Python Programming Internship**.

## 👩‍💻 Author

**Irsa Attique**

Cybersecurity Undergraduate
