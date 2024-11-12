import { MenuRootItem } from 'ontimize-web-ngx';

import { ActivityCardComponent } from './Activity-card/Activity-card.component';

import { CourseCardComponent } from './Course-card/Course-card.component';

import { CourseRequirementCardComponent } from './CourseRequirement-card/CourseRequirement-card.component';

import { DegreeProgramCardComponent } from './DegreeProgram-card/DegreeProgram-card.component';

import { DepartmentCardComponent } from './Department-card/Department-card.component';

import { DepartmentFacultyCardComponent } from './DepartmentFaculty-card/DepartmentFaculty-card.component';

import { EnrollmentCardComponent } from './Enrollment-card/Enrollment-card.component';

import { ProgramCourseCardComponent } from './ProgramCourse-card/ProgramCourse-card.component';

import { StudentCardComponent } from './Student-card/Student-card.component';

import { StudentActivityCardComponent } from './StudentActivity-card/StudentActivity-card.component';

import { TeacherCardComponent } from './Teacher-card/Teacher-card.component';

import { TeacherCourseAssignmentCardComponent } from './TeacherCourseAssignment-card/TeacherCourseAssignment-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Activity', name: 'ACTIVITY', icon: 'view_list', route: '/main/Activity' }
    
        ,{ id: 'Course', name: 'COURSE', icon: 'view_list', route: '/main/Course' }
    
        ,{ id: 'CourseRequirement', name: 'COURSEREQUIREMENT', icon: 'view_list', route: '/main/CourseRequirement' }
    
        ,{ id: 'DegreeProgram', name: 'DEGREEPROGRAM', icon: 'view_list', route: '/main/DegreeProgram' }
    
        ,{ id: 'Department', name: 'DEPARTMENT', icon: 'view_list', route: '/main/Department' }
    
        ,{ id: 'DepartmentFaculty', name: 'DEPARTMENTFACULTY', icon: 'view_list', route: '/main/DepartmentFaculty' }
    
        ,{ id: 'Enrollment', name: 'ENROLLMENT', icon: 'view_list', route: '/main/Enrollment' }
    
        ,{ id: 'ProgramCourse', name: 'PROGRAMCOURSE', icon: 'view_list', route: '/main/ProgramCourse' }
    
        ,{ id: 'Student', name: 'STUDENT', icon: 'view_list', route: '/main/Student' }
    
        ,{ id: 'StudentActivity', name: 'STUDENTACTIVITY', icon: 'view_list', route: '/main/StudentActivity' }
    
        ,{ id: 'Teacher', name: 'TEACHER', icon: 'view_list', route: '/main/Teacher' }
    
        ,{ id: 'TeacherCourseAssignment', name: 'TEACHERCOURSEASSIGNMENT', icon: 'view_list', route: '/main/TeacherCourseAssignment' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    ActivityCardComponent

    ,CourseCardComponent

    ,CourseRequirementCardComponent

    ,DegreeProgramCardComponent

    ,DepartmentCardComponent

    ,DepartmentFacultyCardComponent

    ,EnrollmentCardComponent

    ,ProgramCourseCardComponent

    ,StudentCardComponent

    ,StudentActivityCardComponent

    ,TeacherCardComponent

    ,TeacherCourseAssignmentCardComponent

];