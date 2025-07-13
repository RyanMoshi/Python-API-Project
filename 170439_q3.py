# 170439_q3.py
# This Is An Employee and Department Management

class Employee:
    def __init__(self, employeeName, employeeID, salary):
        self.employeeName = employeeName
        self.employeeID = employeeID
        self.salary = salary
        
    def display_employee_Details(self):
        return f"Name: {self.employeeName}, ID: {self.employeeID}, Salary: {self.salary}"
    
    def Update_salary(self, newSalary):
        self.salary = newSalary
        return f"{self.employeeName}'s salary updated to {self.salary}"
    
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
        return f"{employee.employeeName} added to {self.department_name} department"
    
    def display_total_expenditure(self):
        total = sum(employee.salary for employee in self.employees)
        return f"Total salary cost for {self.department_name}: {total}"
    
    def display_employees(self):
        if self.employees:
            return [employee.display_employee_Details() for employee in self.employees]
        else:
            return [f"No staff in {self.department_name} department"]

if __name__ == "__main__":
    employee1 = Employee("Samuel Githongori", 1, 50000)
    employee2 = Employee("Kuol Abraham", 2, 47000)
    employee3 = Employee("Eurel Owatte", 3, 43000)
    employee4 = Employee("Terry Shakara", 4, 39000)
    
    dept = Department("Software Engineering")
    
    print(dept.add_employee(employee1))
    print(dept.add_employee(employee2))
    print(dept.add_employee(employee3))
    print(dept.add_employee(employee4))
    
    print("Team members in Software Engineering:")
    for detail in dept.display_employees():
        print(detail)
    
    print(employee4.Update_salary(45000))
    print(employee1.Update_salary(55000))
    
    print(dept.display_total_expenditure())
