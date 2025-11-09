# Student Management System (SMS)

A Python-based student management system demonstrating Object-Oriented Programming (OOP) principles including inheritance, polymorphism, encapsulation, and abstraction.

## Features

- **Student Management**: Add, remove, find, and display student records
- **Student Types**: Support for both undergraduate and graduate students
- **Scholarship Calculation**: Automatic scholarship calculation based on student type and performance
- **Type Safety**: Uses Python type hints for better code quality

## Project Structure

```
student-management-system/
├── app.py              # Main application with all classes and test code
├── requirement.md      # Project requirements (in Thai)
└── README.md          # This file
```

## Classes

### `Student` (Abstract Base Class)
Abstract class representing a student with common attributes and methods.

**Attributes:**
- `name`: Student's name
- `student_id`: Unique student identifier
- `major`: Academic major
- `_gpa`: Grade Point Average (encapsulated)

**Methods:**
- `calculate_scholarship()`: Abstract method for scholarship calculation
- `display_info()`: Display student information

### `Undergraduate`
Represents undergraduate students (Bachelor's degree).

**Additional Attributes:**
- `year`: Current year (1-4)

**Scholarship Formula:**
```
(GPA × 1000) + (200 × year)
```

### `Graduate`
Represents graduate students (Master's/PhD).

**Additional Attributes:**
- `research_topic`: Boolean indicating if student has a research topic

**Scholarship Formula:**
```
(GPA × 2000) + (500 if has research_topic else 0)
```

### `Registrar`
Manages the collection of students (registry office).

**Methods:**
- `add_student(student)`: Add a student to the registry
- `remove_student(student_id)`: Remove a student by ID
- `find_student(student_id)`: Find and return a student by ID
- `display_all_students()`: Display information for all students

## Requirements

- Python 3.10 or higher (uses union type syntax `|`)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd student-management-system
```

2. No additional dependencies required (uses only Python standard library)

## Usage

Run the application:
```bash
python app.py
```

### Example Output

```
ADD STUDENTS TO REGISTRAR
REMOVE STUDENT WITH ID 123
FIND STUDENT WITH ID 456
------------------------------
Name: Jane
Student ID: 456
Major: Computer Science
GPA: 3.89
------------------------------
DISPLAY ALL STUDENTS
------------------------------
Name: Jane
Student ID: 456
Major: Computer Science
GPA: 3.89
------------------------------
Name: Jamie
Student ID: 789
Major: Computer Science
GPA: 4.0
------------------------------
Name: Jake
Student ID: 012
Major: Computer Science
GPA: 3.5
------------------------------
CALCULATE SCHOLARSHIP
------------------------------
Jane: 4290.0
Jamie: 8500.0
Jake: 7000.0
```

### Example Code

```python
from app import Registrar, Undergraduate, Graduate

# Create registrar instance
registrar = Registrar()

# Create students
john = Undergraduate("John Doe", "001", "Computer Science", 3.8, 3)
jane = Graduate("Jane Smith", "002", "Data Science", 3.9, True)

# Add students
registrar.add_student(john)
registrar.add_student(jane)

# Display all students
registrar.display_all_students()

# Calculate scholarships
print(f"John's scholarship: ${john.calculate_scholarship()}")
print(f"Jane's scholarship: ${jane.calculate_scholarship()}")
```

## OOP Principles Demonstrated

### 1. **Abstraction**
- `Student` is an abstract base class with abstract method `calculate_scholarship()`

### 2. **Inheritance**
- `Undergraduate` and `Graduate` inherit from `Student`

### 3. **Polymorphism**
- `calculate_scholarship()` is implemented differently in each subclass

### 4. **Encapsulation**
- `_gpa` is a protected attribute (indicated by underscore prefix)

## Testing

The `app.py` file includes test code in the `if __name__ == "__main__"` block that demonstrates:
- Adding multiple students
- Removing a student
- Finding a specific student
- Displaying all students
- Calculating scholarships

## License

This project is created for educational purposes.

## Author

Created as a final lab project for Object-Oriented Programming course.
