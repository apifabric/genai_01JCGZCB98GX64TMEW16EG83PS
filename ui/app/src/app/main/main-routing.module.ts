import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Activity', loadChildren: () => import('./Activity/Activity.module').then(m => m.ActivityModule) },
    
        { path: 'Course', loadChildren: () => import('./Course/Course.module').then(m => m.CourseModule) },
    
        { path: 'CourseRequirement', loadChildren: () => import('./CourseRequirement/CourseRequirement.module').then(m => m.CourseRequirementModule) },
    
        { path: 'DegreeProgram', loadChildren: () => import('./DegreeProgram/DegreeProgram.module').then(m => m.DegreeProgramModule) },
    
        { path: 'Department', loadChildren: () => import('./Department/Department.module').then(m => m.DepartmentModule) },
    
        { path: 'DepartmentFaculty', loadChildren: () => import('./DepartmentFaculty/DepartmentFaculty.module').then(m => m.DepartmentFacultyModule) },
    
        { path: 'Enrollment', loadChildren: () => import('./Enrollment/Enrollment.module').then(m => m.EnrollmentModule) },
    
        { path: 'ProgramCourse', loadChildren: () => import('./ProgramCourse/ProgramCourse.module').then(m => m.ProgramCourseModule) },
    
        { path: 'Student', loadChildren: () => import('./Student/Student.module').then(m => m.StudentModule) },
    
        { path: 'StudentActivity', loadChildren: () => import('./StudentActivity/StudentActivity.module').then(m => m.StudentActivityModule) },
    
        { path: 'Teacher', loadChildren: () => import('./Teacher/Teacher.module').then(m => m.TeacherModule) },
    
        { path: 'TeacherCourseAssignment', loadChildren: () => import('./TeacherCourseAssignment/TeacherCourseAssignment.module').then(m => m.TeacherCourseAssignmentModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }