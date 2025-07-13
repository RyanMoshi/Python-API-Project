# 170439_q2.py
# This Is A Online Course Management System

class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.assignments = {
            "Intro Project": grade
        }
        
    def add_assignment(self, assignment_Name, grade):
        self.assignments[assignment_Name] = grade
        return f"{assignment_Name} graded {grade} added for {self.name}"
        
    def listAssignments(self):
        if self.assignments:
            return [f"{assignment}: {grade}" for assignment, grade in self.assignments.items()]
        else:
            return "No assignments yet"
            
class Instructor:
    def __init__(self, Name, courseName):
        self.Name = Name
        self.courseName = courseName
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        return f"{student.name} enrolled in {self.courseName}"
        
    def add_grade(self, student, assignment_Name, grade):
        if student in self.students:
            student.add_assignment(assignment_Name, grade)
            return f"{self.Name} gave {grade} in {assignment_Name} to {student.name}"
        else:
            return f"{student.name} is not registered in {self.courseName}"
            
    def display_studentsPerfomance(self):
        if self.students:
            return [f"{student.name} (ID: {student.student_id}) - Grades: {student.assignments}" for student in self.students]
        else:
            return "No students enrolled"

if __name__ == "__main__":
    student1 = Student("Terry Shakara", 301, 70)
    student2 = Student("Njoki Sebastian", 302, 82)
    student3 = Student("Mina Emmanuel", 303, 90)
    student4 = Student("Eurel Owatte", 304, 88)
    
    instructor = Instructor("Caleb Katumo", "Intro to Programming")
    
    print(instructor.add_student(student1))
    print(instructor.add_student(student2))
    print(instructor.add_student(student3))
    print(instructor.add_student(student4))
    
    print(instructor.add_grade(student1, "Assignment 1", 78))
    print(instructor.add_grade(student3, "Project 1", 91))
    print(instructor.add_grade(student4, "Assignment 2", 87))
    
    for student in instructor.students:
        print(f"{student.name} (ID: {student.student_id}) Assignments: {student.assignments}")
    
    print(student1.listAssignments())
