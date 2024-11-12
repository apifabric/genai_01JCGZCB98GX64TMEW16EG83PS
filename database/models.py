# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 12, 2024 20:02:57
# Database: sqlite:////tmp/tmp.w7jaLRcI8Q-01JCGZCB98GX64TMEW16EG83PS/school_mgmt/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Activity(SAFRSBaseX, Base):
    """
    description: Table for student activities.
    """
    __tablename__ = 'activity'
    _s_collection_name = 'Activity'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_service = Column(Boolean)

    # parent relationships (access parent)

    # child relationships (access children)
    StudentActivityList : Mapped[List["StudentActivity"]] = relationship(back_populates="activity")



class Course(SAFRSBaseX, Base):
    """
    description: Table for courses offered by the school.
    """
    __tablename__ = 'course'
    _s_collection_name = 'Course'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    credit_hours = Column(Integer)
    is_graduate = Column(Boolean)

    # parent relationships (access parent)

    # child relationships (access children)
    CourseRequirementList : Mapped[List["CourseRequirement"]] = relationship(foreign_keys='[CourseRequirement.course_id]', back_populates="course")
    prerequisiteCourseRequirementList : Mapped[List["CourseRequirement"]] = relationship(foreign_keys='[CourseRequirement.prerequisite_id]', back_populates="prerequisite")
    EnrollmentList : Mapped[List["Enrollment"]] = relationship(back_populates="course")
    ProgramCourseList : Mapped[List["ProgramCourse"]] = relationship(back_populates="course")
    TeacherCourseAssignmentList : Mapped[List["TeacherCourseAssignment"]] = relationship(back_populates="course")



class DegreeProgram(SAFRSBaseX, Base):
    """
    description: Table for degree programs offered by the school.
    """
    __tablename__ = 'degree_program'
    _s_collection_name = 'DegreeProgram'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ProgramCourseList : Mapped[List["ProgramCourse"]] = relationship(back_populates="program")



class Department(SAFRSBaseX, Base):
    """
    description: Table for school departments.
    """
    __tablename__ = 'department'
    _s_collection_name = 'Department'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    faculty_count = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    DepartmentFacultyList : Mapped[List["DepartmentFaculty"]] = relationship(back_populates="department")



class Student(SAFRSBaseX, Base):
    """
    description: Table for student information.
    """
    __tablename__ = 'student'
    _s_collection_name = 'Student'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    enrollment_date = Column(Date)
    service_activity_count = Column(Integer)
    is_honor_student = Column(Boolean)

    # parent relationships (access parent)

    # child relationships (access children)
    EnrollmentList : Mapped[List["Enrollment"]] = relationship(back_populates="student")
    StudentActivityList : Mapped[List["StudentActivity"]] = relationship(back_populates="student")



class Teacher(SAFRSBaseX, Base):
    """
    description: Table for teacher information.
    """
    __tablename__ = 'teacher'
    _s_collection_name = 'Teacher'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    hire_date = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)
    DepartmentFacultyList : Mapped[List["DepartmentFaculty"]] = relationship(back_populates="teacher")
    TeacherCourseAssignmentList : Mapped[List["TeacherCourseAssignment"]] = relationship(back_populates="teacher")



class CourseRequirement(SAFRSBaseX, Base):
    """
    description: Table for course prerequisites.
    """
    __tablename__ = 'course_requirement'
    _s_collection_name = 'CourseRequirement'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    course_id = Column(ForeignKey('course.id'))
    prerequisite_id = Column(ForeignKey('course.id'))

    # parent relationships (access parent)
    course : Mapped["Course"] = relationship(foreign_keys='[CourseRequirement.course_id]', back_populates=("CourseRequirementList"))
    prerequisite : Mapped["Course"] = relationship(foreign_keys='[CourseRequirement.prerequisite_id]', back_populates=("prerequisiteCourseRequirementList"))

    # child relationships (access children)



class DepartmentFaculty(SAFRSBaseX, Base):
    """
    description: Association table for department faculty assignments.
    """
    __tablename__ = 'department_faculty'
    _s_collection_name = 'DepartmentFaculty'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    department_id = Column(ForeignKey('department.id'))
    teacher_id = Column(ForeignKey('teacher.id'))

    # parent relationships (access parent)
    department : Mapped["Department"] = relationship(back_populates=("DepartmentFacultyList"))
    teacher : Mapped["Teacher"] = relationship(back_populates=("DepartmentFacultyList"))

    # child relationships (access children)



class Enrollment(SAFRSBaseX, Base):
    """
    description: Junction table for student course enrollments.
    """
    __tablename__ = 'enrollment'
    _s_collection_name = 'Enrollment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('student.id'))
    course_id = Column(ForeignKey('course.id'))
    enrollment_date = Column(Date)

    # parent relationships (access parent)
    course : Mapped["Course"] = relationship(back_populates=("EnrollmentList"))
    student : Mapped["Student"] = relationship(back_populates=("EnrollmentList"))

    # child relationships (access children)



class ProgramCourse(SAFRSBaseX, Base):
    """
    description: Association table for courses required in degree programs.
    """
    __tablename__ = 'program_course'
    _s_collection_name = 'ProgramCourse'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    program_id = Column(ForeignKey('degree_program.id'))
    course_id = Column(ForeignKey('course.id'))

    # parent relationships (access parent)
    course : Mapped["Course"] = relationship(back_populates=("ProgramCourseList"))
    program : Mapped["DegreeProgram"] = relationship(back_populates=("ProgramCourseList"))

    # child relationships (access children)



class StudentActivity(SAFRSBaseX, Base):
    """
    description: Junction table for student involvement in activities.
    """
    __tablename__ = 'student_activity'
    _s_collection_name = 'StudentActivity'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('student.id'))
    activity_id = Column(ForeignKey('activity.id'))

    # parent relationships (access parent)
    activity : Mapped["Activity"] = relationship(back_populates=("StudentActivityList"))
    student : Mapped["Student"] = relationship(back_populates=("StudentActivityList"))

    # child relationships (access children)



class TeacherCourseAssignment(SAFRSBaseX, Base):
    """
    description: Association table for teacher course assignments.
    """
    __tablename__ = 'teacher_course_assignment'
    _s_collection_name = 'TeacherCourseAssignment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(ForeignKey('teacher.id'))
    course_id = Column(ForeignKey('course.id'))
    term = Column(String)

    # parent relationships (access parent)
    course : Mapped["Course"] = relationship(back_populates=("TeacherCourseAssignmentList"))
    teacher : Mapped["Teacher"] = relationship(back_populates=("TeacherCourseAssignmentList"))

    # child relationships (access children)
