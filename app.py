from abc import ABC, abstractmethod

# Abstract class
class Student(ABC):
    def __init__(self, name: str, student_id: str, major: str, gpa: float):
        self.name = name
        self.student_id = student_id
        self.major = major
        self._gpa = gpa

    @abstractmethod
    def calculate_scholarship(self):
        pass

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"GPA: {self._gpa}")
        print("-" * 30)

# Undergraduate class inherit from Student class
class Undergraduate(Student):
    def __init__(self, name: str, student_id: str, major: str, gpa: float, year: int):
        super().__init__(name, student_id, major, gpa)
        self.year = year
    
    def calculate_scholarship(self) -> float:
        return (self._gpa * 1000) + (200 * self.year)

# Graduate class inherit from Student class
class Graduate(Student):
    def __init__(self, name: str, student_id: str, major: str, gpa: float, research_topic: bool):
        super().__init__(name, student_id, major, gpa)
        self.research_topic = research_topic
    
    def calculate_scholarship(self) -> float:
        return self._gpa * 2000 + (500 if self.research_topic else 0)

# Registrar class
class Registrar:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, student_id: str):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                break

    def find_student(self, student_id: str) -> Student | None:
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_all_students(self):
        for student in self.students:
            student.display_info()
            
# Test 
if __name__ == "__main__":
    registrar = Registrar()

    john = Undergraduate("John", "123", "Computer Science", 3.92, 4)
    jane = Undergraduate("Jane", "456", "Computer Science", 3.89, 2)
    jamie = Graduate("Jamie", "789", "Computer Science", 4.0, True)
    jake = Graduate("Jake", "012", "Computer Science", 3.5, False)

    print("Add students to registrar".upper())
    registrar.add_student(john)
    registrar.add_student(jane)
    registrar.add_student(jamie)
    registrar.add_student(jake)

    print("Remove student with ID 123".upper())
    registrar.remove_student("123")

    print("Find student with ID 456".upper())
    print("-" * 30)
    student = registrar.find_student("456")
    if student:
        student.display_info()

    print("Display all students".upper())
    print("-" * 30)
    registrar.display_all_students()

    print("Calculate scholarship".upper())
    print("-" * 30)
    for student in registrar.students:
        print(f"{student.name}: {student.calculate_scholarship()}")