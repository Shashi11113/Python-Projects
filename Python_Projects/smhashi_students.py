# Sadam Hashi, CIS 345, 1:30pm to 2:45pm, PE6

# TODO: Student class
class Student:

    def __init__(self, first=""):
        self.__fname = first
        self.__lname = ""

    @property
    def fname(self):
        return self.__fname.capitalize()

    @fname.setter
    def fname(self, new):
        if new.isalpha() and len(new) >= 1:
            self.__fname = new
        else:
            self.__fname = 'Unknown'

    @property
    def lname(self):
        return self.__lname.capitalize()

    @lname.setter
    def lname(self, new):
        if new.isalpha() and len(new) >= 1:
            self.__lname = new
        else:
            self.__lname = 'Unknown'

    def __str__(self):
        return f"{self.fname} {self.lname}"


# TODO: GradStudent class
class GraduateStudent(Student):

    def __init__(self, fname="", thesis=""):
        super().__init__(fname)
        self.__thesis = thesis

    @property
    def thesis(self):
        return self.__thesis.upper()

    @thesis.setter
    def thesis(self, title):
        if title.isalpha() and len(title) >= 1:
            self.__thesis = f"Thesis: {title.upper()}"
        else:
            self.__thesis = 'Invalid'

    def __str__(self):
        fullname = super().__str__()
        return f"{fullname}\n\t{self.thesis}"


# TODO: PhDStudent class
class PhDStudent(Student):
    def __init__(self, fname="", dissertation=""):
        super().__init__(fname)
        self.__dissertation = dissertation

    @property
    def dissertation(self):
        return self.__dissertation.upper()

    @dissertation.setter
    def dissertation(self, title):
        if title.isalpha() and len(title) >= 1:
            self.__dissertation= f"Thesis: {title.upper()}"
        else:
            self.__dissertation= 'Invalid'


def add_student(student_type):
    """Get student data and create an object to be returned"""
    student = None
    # Get first and last name here because all students need this data
    first = input('Enter first name: ')
    last = input('Enter last name: ')
    # TODO: Determine student type and construct an object and save in student
    if student_type == 'G':
        title = input("Enter thesis title: ")
        student = GraduateStudent(first, title)
    elif student_type == 'P':
        title = input("Enter dissertation title: ")
        student = PhDStudent(first, title)
    elif student_type == 'S':
        student = Student(first)
    # TODO: Assign last_name using our object's property then return student
    student.lname = last
    return student

# Main Function
def main():
    """Main program logic"""
    students = []
    entry = ''
    print("{:^50}".format('Student Management System'))
    while entry != 'X':
        student_types = ['S', 'G', 'P']
        # Get user entry and capitalize the entry
        entry = input(
            '\nEnter (S)tudent, (G)radStudent, (P)hDStudent or (X)exit: ')
        entry = entry.upper()
        # TODO: Is user entry one of studentTypes. Yes - add_student to list
        if entry in student_types:
            student = add_student(entry)
            students.append(student)
    # TODO: print students and dissertation if the student is a PhD type
    print("\nThe following students were added...")
    for stu in students:
        print(stu)
        if isinstance(stu, PhDStudent):
            print(f'\t{stu.dissertation}')

if __name__ == "__main__":
    # call and execute the main function
    main()



