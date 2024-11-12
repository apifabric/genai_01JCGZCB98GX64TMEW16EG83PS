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


class Student(db.Model):
    """description: Table to store student information."""

    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    address = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    service_activity_count = db.Column(db.Integer, nullable=False, default=0)  # For LogicBank Rule

class Course(db.Model):
    """description: Table to store course information."""

    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)

class Enrollment(db.Model):
    """description: Table to store enrollment information linking students and courses."""

    __tablename__ = 'enrollment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)

class Activity(db.Model):
    """description: Table to store student activities."""

    __tablename__ = 'activity'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

class Teacher(db.Model):
    """description: Table to store teacher information."""

    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    hire_date = db.Column(db.Date, nullable=True)
    expertise_area = db.Column(db.String, nullable=True)

class ClassSession(db.Model):
    """description: Table for each session of a class, linking courses and teachers."""

    __tablename__ = 'class_session'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)

class Evaluation(db.Model):
    """description: Table to store evaluations or grades for students enrolled in courses."""

    __tablename__ = 'evaluation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    enrollment_id = db.Column(db.Integer, db.ForeignKey('enrollment.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String, nullable=True)

class ExtracurricularActivity(db.Model):
    """description: Table to store information about extracurricular activities."""

    __tablename__ = 'extracurricular_activity'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)

class ActivityParticipation(db.Model):
    """description: Table linking students to extracurricular activities."""

    __tablename__ = 'activity_participation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('extracurricular_activity.id'), nullable=False)
    participation_date = db.Column(db.Date, nullable=False)

class Reward(db.Model):
    """description: Table to store information about rewards given to students."""

    __tablename__ = 'reward'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    reward_name = db.Column(db.String, nullable=False)
    issue_date = db.Column(db.Date, nullable=False)

class Department(db.Model):
    """description: Table to store department information."""

    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    head_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=True)

class Subject(db.Model):
    """description: Table to store subjects managed by each department."""

    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)



class Course(db.Model):
    """description: Table to store course information."""

    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)



class Enrollment(db.Model):
    """description: Table to store enrollment information linking students and courses."""

    __tablename__ = 'enrollment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)



class Activity(db.Model):
    """description: Table to store student activities."""

    __tablename__ = 'activity'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)



class Teacher(db.Model):
    """description: Table to store teacher information."""

    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    hire_date = db.Column(db.Date, nullable=True)
    expertise_area = db.Column(db.String, nullable=True)



class ClassSession(db.Model):
    """description: Table for each session of a class, linking courses and teachers."""

    __tablename__ = 'class_session'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)



class Evaluation(db.Model):
    """description: Table to store evaluations or grades for students enrolled in courses."""

    __tablename__ = 'evaluation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    enrollment_id = db.Column(db.Integer, db.ForeignKey('enrollment.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String, nullable=True)



class ExtracurricularActivity(db.Model):
    """description: Table to store information about extracurricular activities."""

    __tablename__ = 'extracurricular_activity'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)



class ActivityParticipation(db.Model):
    """description: Table linking students to extracurricular activities."""

    __tablename__ = 'activity_participation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('extracurricular_activity.id'), nullable=False)
    participation_date = db.Column(db.Date, nullable=False)



class Reward(db.Model):
    """description: Table to store information about rewards given to students."""

    __tablename__ = 'reward'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    reward_name = db.Column(db.String, nullable=False)
    issue_date = db.Column(db.Date, nullable=False)



class Department(db.Model):
    """description: Table to store department information."""

    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    head_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=True)



class Subject(db.Model):
    """description: Table to store subjects managed by each department."""

    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)



# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Test data creation
from datetime import date

# Students
student1 = Student(name='Alice Smith', date_of_birth=date(2005, 4, 15), address='123 Maple St', email='alice@example.com', service_activity_count=3)
student2 = Student(name='Bob Johnson', date_of_birth=date(2004, 11, 25), address='456 Oak Rd', email='bob@example.com', service_activity_count=1)
student3 = Student(name='Charlie Brown', date_of_birth=date(2006, 7, 30), address='789 Pine Ave', email='charlie@example.com', service_activity_count=4)
student4 = Student(name='Diana Green', date_of_birth=date(2005, 3, 12), address='246 Elm St', email='diana@example.com', service_activity_count=2)

# Courses
course1 = Course(title='Mathematics 101', description='Introduction to mathematics')
course2 = Course(title='Biology 101', description='Basic biology concepts')
course3 = Course(title='History 101', description='Survey of ancient civilizations')
course4 = Course(title='Chemistry 101', description='Fundamentals of chemistry')

# Enrollments
enrollment1 = Enrollment(student_id=1, course_id=1, enrollment_date=date(2023, 1, 15))
enrollment2 = Enrollment(student_id=1, course_id=2, enrollment_date=date(2023, 1, 16))
enrollment3 = Enrollment(student_id=2, course_id=3, enrollment_date=date(2023, 1, 17))
enrollment4 = Enrollment(student_id=3, course_id=4, enrollment_date=date(2023, 1, 18))

# Activities
activity1 = Activity(name='School Play', description='Annual school play', student_id=1)
activity2 = Activity(name='Math Club', description='Weekly math club meetings', student_id=2)
activity3 = Activity(name='Science Fair', description='Annual science fair competition', student_id=3)
activity4 = Activity(name='Basketball Team', description='School basketball team', student_id=4)

# Teachers
teacher1 = Teacher(name='Ms. Thompson', hire_date=date(2000, 5, 20), expertise_area='Mathematics')
teacher2 = Teacher(name='Mr. Wilson', hire_date=date(1998, 9, 10), expertise_area='Biology')
teacher3 = Teacher(name='Mrs. Lee', hire_date=date(2005, 3, 5), expertise_area='History')
teacher4 = Teacher(name='Dr. Patel', hire_date=date(2010, 1, 15), expertise_area='Chemistry')

# Class Sessions
class_session1 = ClassSession(course_id=1, teacher_id=1, start_date=date(2023, 2, 1), end_date=date(2023, 6, 1))
class_session2 = ClassSession(course_id=2, teacher_id=2, start_date=date(2023, 2, 5), end_date=date(2023, 6, 5))
class_session3 = ClassSession(course_id=3, teacher_id=3, start_date=date(2023, 2, 10), end_date=date(2023, 6, 10))
class_session4 = ClassSession(course_id=4, teacher_id=4, start_date=date(2023, 2, 15), end_date=date(2023, 6, 15))

# Evaluations
evaluation1 = Evaluation(enrollment_id=1, score=95, comments='Excellent performance')
evaluation2 = Evaluation(enrollment_id=2, score=88, comments='Very good performance')
evaluation3 = Evaluation(enrollment_id=3, score=76, comments='Satisfactory performance')
evaluation4 = Evaluation(enrollment_id=4, score=82, comments='Good performance')

# Extracurricular Activities
extracurricular1 = ExtracurricularActivity(name='Chess Club', description='School chess club')
extracurricular2 = ExtracurricularActivity(name='Debate Team', description='School debate team')
extracurricular3 = ExtracurricularActivity(name='Robotics Club', description='Robotics and engineering projects')
extracurricular4 = ExtracurricularActivity(name='Art Club', description='School art club activities')

# Activity Participation
participation1 = ActivityParticipation(student_id=1, activity_id=1, participation_date=date(2023, 3, 12))
participation2 = ActivityParticipation(student_id=2, activity_id=2, participation_date=date(2023, 3, 15))
participation3 = ActivityParticipation(student_id=3, activity_id=3, participation_date=date(2023, 3, 20))
participation4 = ActivityParticipation(student_id=4, activity_id=4, participation_date=date(2023, 3, 25))

# Rewards
reward1 = Reward(student_id=1, reward_name='Honor Roll', issue_date=date(2023, 5, 1))
reward2 = Reward(student_id=2, reward_name='Perfect Attendance', issue_date=date(2023, 5, 2))
reward3 = Reward(student_id=3, reward_name='Science Award', issue_date=date(2023, 5, 3))
reward4 = Reward(student_id=4, reward_name='Sportsmanship Award', issue_date=date(2023, 5, 4))

# Departments
department1 = Department(name='Mathematics Department', head_id=1)
department2 = Department(name='Biology Department', head_id=2)
department3 = Department(name='History Department', head_id=3)
department4 = Department(name='Chemistry Department', head_id=4)

# Subjects
subject1 = Subject(name='Algebra', department_id=1)
subject2 = Subject(name='Genetics', department_id=2)
subject3 = Subject(name='World History', department_id=3)
subject4 = Subject(name='Organic Chemistry', department_id=4)


session.add_all([student1, student2, student3, student4, course1, course2, course3, course4, enrollment1, enrollment2, enrollment3, enrollment4, activity1, activity2, activity3, activity4, teacher1, teacher2, teacher3, teacher4, evaluation1, evaluation2, evaluation3, evaluation4, extracurricular1, extracurricular2, extracurricular3, extracurricular4, participation1, participation2, participation3, participation4, reward1, reward2, reward3, reward4, department1, department2, department3, department4, subject1, subject2, subject3, subject4])
session.commit()
