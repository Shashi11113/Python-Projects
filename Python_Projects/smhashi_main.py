# Sadam Hashi, CIS 345, 1:30pm to 2:45pm, A4

# Employee class
class Employee:
    def __init__(self, name='Unknown', eid='9999'):
        self.name = name    # Use the setter for validation
        self.eid = eid      # Use the setter for validation

    @property
    def name(self):
        return self._name.capitalize()

    @name.setter
    def name(self, emp):
        if emp and emp.isalpha():
            self._name = emp
        else:
            self._name = 'Unknown'

    @property
    def eid(self):
        return str(self._eid).zfill(4)

    @eid.setter
    def eid(self, number):
        if number.isdigit() and len(number) > 0:
            self._eid = number
        else:
            self._eid = '9999'

    def __str__(self):
        return f'{self.eid}: {self.name}'


# Manager class derives from employee class
class Manager(Employee):
    def __init__(self, name='Unknown', eid='9999'):
        super().__init__(name, eid)
        self.subordinates = []

    def add_subordinate(self):
        emp_name = input("Enter name: ")
        emp_id = input("Enter id: ")
        new = Employee(emp_name, emp_id)
        self.subordinates.append(new)

    def print_subordinates(self):
        print(f"\t{self.name}'s Employees")
        for emp in self.subordinates:
            print(f"\t{emp}")


# Main function
def main():
    employees = []
    print("{:^50}".format("Employee Management System\n"))
    print("Adding Employees...")
    while True:
        employee = add_employee()
        employees.append(employee)
        entry = input("Do you want to enter more? ").casefold()
        if entry != 'y':
            break
    print("\nPrinting Employee List")
    for emp in employees:
        print(emp)
        if isinstance(emp, Manager):
            emp.print_subordinates()


# Add employee function
def add_employee():
    emp_name = input("\nEnter name: ")
    emp_id = input("Enter id: ")
    entry = input("Is the employee a manager? (Y/N) ").casefold()
    if entry == 'y':
        manager = Manager(emp_name, emp_id)
        number = int(input("How many subordinates? "))
        i = 0
        while i < number:
            manager.add_subordinate()
            i += 1
        return manager
    else:
        return Employee(emp_name, emp_id)


if __name__ == "__main__":
    main()









