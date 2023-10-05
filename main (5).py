class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students

# List 1: Students with different CGPAs
students1 = [
    Student("Alice", "101", 3.8),
    Student("Bob", "102", 3.5),
    Student("Charlie", "103", 3.9),
]

sorted_students1 = sort_students(students1)
print("Sorted Students (List 1):")
for student in sorted_students1:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

# List 2: Students with the same CGPAs
students2 = [
    Student("David", "104", 3.7),
    Student("Eve", "105", 3.7),
    Student("Frank", "106", 3.7),
]

sorted_students2 = sort_students(students2)
print("\nSorted Students (List 2):")
for student in sorted_students2:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")