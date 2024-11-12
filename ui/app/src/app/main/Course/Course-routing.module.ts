import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CourseHomeComponent } from './home/Course-home.component';
import { CourseNewComponent } from './new/Course-new.component';
import { CourseDetailComponent } from './detail/Course-detail.component';

const routes: Routes = [
  {path: '', component: CourseHomeComponent},
  { path: 'new', component: CourseNewComponent },
  { path: ':id', component: CourseDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Course-detail-permissions'
      }
    }
  },{
    path: ':course_id/CourseRequirement', loadChildren: () => import('../CourseRequirement/CourseRequirement.module').then(m => m.CourseRequirementModule),
    data: {
        oPermission: {
            permissionId: 'CourseRequirement-detail-permissions'
        }
    }
},{
    path: ':prerequisite_id/CourseRequirement', loadChildren: () => import('../CourseRequirement/CourseRequirement.module').then(m => m.CourseRequirementModule),
    data: {
        oPermission: {
            permissionId: 'CourseRequirement-detail-permissions'
        }
    }
},{
    path: ':course_id/Enrollment', loadChildren: () => import('../Enrollment/Enrollment.module').then(m => m.EnrollmentModule),
    data: {
        oPermission: {
            permissionId: 'Enrollment-detail-permissions'
        }
    }
},{
    path: ':course_id/ProgramCourse', loadChildren: () => import('../ProgramCourse/ProgramCourse.module').then(m => m.ProgramCourseModule),
    data: {
        oPermission: {
            permissionId: 'ProgramCourse-detail-permissions'
        }
    }
},{
    path: ':course_id/TeacherCourseAssignment', loadChildren: () => import('../TeacherCourseAssignment/TeacherCourseAssignment.module').then(m => m.TeacherCourseAssignmentModule),
    data: {
        oPermission: {
            permissionId: 'TeacherCourseAssignment-detail-permissions'
        }
    }
}
];

export const COURSE_MODULE_DECLARATIONS = [
    CourseHomeComponent,
    CourseNewComponent,
    CourseDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CourseRoutingModule { }