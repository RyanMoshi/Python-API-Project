# Online Course Management

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, name, grade):
        self.assignments[name] = grade

    def show_grades(self):
        for a, g in self.assignments.items():
            print(f"{a}: {g}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student, assignment, grade):
        student.add_assignment(assignment, grade)

    def display_students(self):
        for s in self.students:
            print(f"{s.name} ({s.student_id}):")
            s.show_grades()

# Example interaction
inst = Instructor("Mr. Smith", "Python 101")
s1 = Student("Bob", 101)
s2 = Student("Amy", 102)
inst.add_student(s1)
inst.add_student(s2)

while True:
    print("\n1. Assign grade\n2. Show all grades\n3. Exit")
    ch = input("Choose: ")
    if ch == '1':
        sid = input("Student ID: ")
        name = input("Assignment: ")
        grade = int(input("Grade: "))
        for s in inst.students:
            if str(s.student_id) == sid:
                inst.assign_grade(s, name, grade)
    elif ch == '2':
        inst.display_students()
    elif ch == '3':
        break