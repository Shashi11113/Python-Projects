# Sadam Hashi, CIS 345, 1:30pm to 2:45pm, A3

import random
import os
from unicodedata import category

courses = []


class Course:
    # class variables
    semester = 'Fall 2025'


    def __init__(self, name='', categories=None):
        """Create a course object. self refers to the object"""
        self.section = random.randint(10000, 100000)
        self.name = name
        self.student_count = 0
        self.class_roster = []
        # Instance variable categories will hold a description and total point value
        # TODO: Add decision for categories=None based on Requirements to avoid mutable trap
        if categories is None:
            self.categories = dict()
            self.enter_categories()
        else:
            self.categories = categories


    @classmethod
    def change_semester(cls, semester):
        """Modify the text of the semester that all courses are being added to"""
        cls.semester = semester


    # TODO: Add enter_categories method to accept all categories for a course
    def enter_categories(self):
        print(f"Enter grading categories for {self.name}")
        grading_category = input("5 letter max Category name: ")
        total_points = input(f"Enter total points for that {grading_category}: ")
        self.categories[grading_category] = total_points
        more_categories = input("Do you have more categories to enter (Y/N): ")
        os.system("clear")
        while more_categories.casefold() == 'y':
            print(f"Enter grading categories for {self.name}")
            grading_category = input("5 letter max Category name: ")
            total_points = int(input(f"Enter total points for {grading_category}: "))
            self.categories[grading_category] = total_points
            more_categories = input("Do you have more categories to enter (Y/N): ").casefold()


    # TODO: Add method to enroll_students in course
    def enroll_students(self, number):
        self.student_count += number
        for times in range(number):
            temp_student = Student(self.categories)
            temp_student.fullname = input("Enter student first and last name: ")
            temp_student.enter_scores()
            self.class_roster.append(temp_student)


    # TODO: Override __str__ method for course to print roster and scores
    def __str__(self):
        message = f"Course {self.section} – {self.name} has {self.student_count} students: \n"
        for student in self.class_roster:
            message += f'{student} - '
            for category in self.categories:
                message += f"{category}: {student.scores[category]}/{self.categories[category]}, "
            message += '\n'
        return message


# TODO: Create student class per UML Class Diagram
class Student:


    def __init__(self, categories, fname='Jane', lname='Doe'):
        """Create a student object"""
        self.first = fname
        self.last = lname
        self.scores = {}

        for category in categories:
            self.scores[category] = 0


    @property
    def fullname(self):
        return f'{self.last}, {self.first}'


    @fullname.setter
    def fullname(self, name):
        try:
            self.first, self.last = name.split(' ')
        except ValueError:
            pass


    def __str__(self):
        return self.fullname


    def enter_scores(self):
        for grading_category in self.scores:
            points = int(input(f"Enter earned points for {grading_category}: "))
            self.scores[grading_category] = points



# Main Logic
print(f"{'University System':*^30}")
Course.change_semester(input('Enter semester and year for which you are creating courses: '))

enter_courses = 'y'
print("\nEntering course information")
while enter_courses == 'y':
    course_name = input('Enter course name: ').upper()
    new_course = Course(course_name)
    courses.append(new_course)
    enter_courses = input("\nAdd another course (Y/N)? ").casefold()

# Add students to each course using enroll_students()
os.system('clear')
# TODO: Create logic to add students to each course using methods created within classes
for course in courses:
    print(f"\nAdd students to {course.name} course")
    add_students = int(input("How many students do you want to enroll? "))
    course.enroll_students(add_students)
# Print Course Roster using Override methods to quickly display necessary data
os.system('clear')
print(f'\nCourse Information for {Course.semester}')
# TODO: Create logic to print each courses student roster
for course in courses:
    print(course)