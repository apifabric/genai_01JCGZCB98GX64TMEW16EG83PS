# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Student(Base):
    """
    description: Table for student information.
    """
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    enrollment_date = Column(Date)
    service_activity_count = Column(Integer, default=0)  # For LogicBank rule
    is_honor_student = Column(Boolean)










class Teacher(Base):
    """
    description: Table for teacher information.
    """
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    hire_date = Column(Date)











class Course(Base):
    """
    description: Table for courses offered by the school.
    """
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    credit_hours = Column(Integer)
    is_graduate = Column(Boolean)









class Enrollment(Base):
    """
    description: Junction table for student course enrollments.
    """
    __tablename__ = 'enrollment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    enrollment_date = Column(Date)







class DegreeProgram(Base):
    """
    description: Table for degree programs offered by the school.
    """
    __tablename__ = 'degree_program'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    level = Column(String)  # e.g., Undergraduate, Masters, PhD










class Department(Base):
    """
    description: Table for school departments.
    """
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    faculty_count = Column(Integer, default=0)  # For LogicBank rule









class TeacherCourseAssignment(Base):
    """
    description: Association table for teacher course assignments.
    """
    __tablename__ = 'teacher_course_assignment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    term = Column(String)







class Activity(Base):
    """
    description: Table for student activities.
    """
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    is_service = Column(Boolean)








class StudentActivity(Base):
    """
    description: Junction table for student involvement in activities.
    """
    __tablename__ = 'student_activity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    activity_id = Column(Integer, ForeignKey('activity.id'))







class CourseRequirement(Base):
    """
    description: Table for course prerequisites.
    """
    __tablename__ = 'course_requirement'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('course.id'))
    prerequisite_id = Column(Integer, ForeignKey('course.id'))  # Self-reference







class DepartmentFaculty(Base):
    """
    description: Association table for department faculty assignments.
    """
    __tablename__ = 'department_faculty'

    id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = Column(Integer, ForeignKey('department.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))







class ProgramCourse(Base):
    """
    description: Association table for courses required in degree programs.
    """
    __tablename__ = 'program_course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    program_id = Column(Integer, ForeignKey('degree_program.id'))
    course_id = Column(Integer, ForeignKey('course.id'))







# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date

# Create test data for Students
student1 = Student(first_name='Alex', last_name='Johnson', enrollment_date=date(2020, 1, 15), service_activity_count=3, is_honor_student=True)
student2 = Student(first_name='Beth', last_name='Smith', enrollment_date=date(2019, 5, 20), service_activity_count=1, is_honor_student=False)
student3 = Student(first_name='Cathy', last_name='Brown', enrollment_date=date(2021, 9, 5), service_activity_count=0, is_honor_student=False)
student4 = Student(first_name='David', last_name='White', enrollment_date=date(2018, 2, 22), service_activity_count=4, is_honor_student=True)

# Create test data for Teachers
teacher1 = Teacher(first_name='John', last_name='Doe', hire_date=date(2010, 8, 15))
teacher2 = Teacher(first_name='Jane', last_name='Smith', hire_date=date(2015, 3, 10))
teacher3 = Teacher(first_name='Emily', last_name='Davis', hire_date=date(2018, 11, 1))
teacher4 = Teacher(first_name='Michael', last_name='Brown', hire_date=date(2012, 6, 23))

# Create test data for Courses
course1 = Course(name='Math 101', credit_hours=3, is_graduate=False)
course2 = Course(name='History 201', credit_hours=4, is_graduate=False)
course3 = Course(name='Physics 301', credit_hours=3, is_graduate=True)
course4 = Course(name='Literature 101', credit_hours=2, is_graduate=False)

# Create test data for Enrollments
enrollment1 = Enrollment(student_id=1, course_id=1, enrollment_date=date(2020, 1, 16))
enrollment2 = Enrollment(student_id=2, course_id=2, enrollment_date=date(2019, 5, 21))
enrollment3 = Enrollment(student_id=3, course_id=3, enrollment_date=date(2021, 9, 6))
enrollment4 = Enrollment(student_id=4, course_id=4, enrollment_date=date(2018, 2, 23))

# Create test data for Degree Programs
degree_program1 = DegreeProgram(name='Bachelor of Science', level='Undergraduate')
degree_program2 = DegreeProgram(name='Master of Arts', level='Masters')
degree_program3 = DegreeProgram(name='Doctor of Philosophy', level='PhD')
degree_program4 = DegreeProgram(name='Bachelor of Arts', level='Undergraduate')

# Create test data for Departments
department1 = Department(name='Mathematics', faculty_count=0)
department2 = Department(name='History', faculty_count=0)
department3 = Department(name='Physics', faculty_count=0)
department4 = Department(name='English', faculty_count=0)

# Create test data for Teacher Course Assignments
teacher_course_assignment1 = TeacherCourseAssignment(teacher_id=1, course_id=1, term='Spring 2021')
teacher_course_assignment2 = TeacherCourseAssignment(teacher_id=2, course_id=2, term='Fall 2021')
teacher_course_assignment3 = TeacherCourseAssignment(teacher_id=3, course_id=3, term='Spring 2022')
teacher_course_assignment4 = TeacherCourseAssignment(teacher_id=4, course_id=4, term='Fall 2022')

# Create test data for Activities
activity1 = Activity(name='Community Service', is_service=True)
activity2 = Activity(name='Math Club', is_service=False)
activity3 = Activity(name='Volunteer Tutoring', is_service=True)
activity4 = Activity(name='Orchestra', is_service=False)

# Create test data for Student Activities
student_activity1 = StudentActivity(student_id=1, activity_id=1)
student_activity2 = StudentActivity(student_id=2, activity_id=2)
student_activity3 = StudentActivity(student_id=3, activity_id=3)
student_activity4 = StudentActivity(student_id=4, activity_id=4)

# Create test data for Course Requirements
course_requirement1 = CourseRequirement(course_id=2, prerequisite_id=1)
course_requirement2 = CourseRequirement(course_id=3, prerequisite_id=2)
course_requirement3 = CourseRequirement(course_id=4, prerequisite_id=3)
course_requirement4 = CourseRequirement(course_id=1, prerequisite_id=4)

# Create test data for Department Faculty
department_faculty1 = DepartmentFaculty(department_id=1, teacher_id=1)
department_faculty2 = DepartmentFaculty(department_id=2, teacher_id=2)
department_faculty3 = DepartmentFaculty(department_id=3, teacher_id=3)
department_faculty4 = DepartmentFaculty(department_id=4, teacher_id=4)

# Create test data for Program Courses
program_course1 = ProgramCourse(program_id=1, course_id=1)
program_course2 = ProgramCourse(program_id=2, course_id=2)
program_course3 = ProgramCourse(program_id=3, course_id=3)
program_course4 = ProgramCourse(program_id=4, course_id=4)


session.add_all([student1, student2, student3, student4, teacher1, teacher2, teacher3, teacher4, course1, course2, course3, course4, enrollment1, enrollment2, enrollment3, enrollment4, degree_program1, degree_program2, degree_program3, degree_program4, department1, department2, department3, department4, teacher_course_assignment1, teacher_course_assignment2, teacher_course_assignment3, teacher_course_assignment4, activity1, activity2, activity3, activity4, student_activity1, student_activity2, student_activity3, student_activity4, course_requirement1, course_requirement2, course_requirement3, course_requirement4, department_faculty1, department_faculty2, department_faculty3, department_faculty4, program_course1, program_course2, program_course3, program_course4])
session.commit()
