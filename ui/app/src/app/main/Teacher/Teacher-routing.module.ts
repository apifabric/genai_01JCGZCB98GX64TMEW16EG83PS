import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TeacherHomeComponent } from './home/Teacher-home.component';
import { TeacherNewComponent } from './new/Teacher-new.component';
import { TeacherDetailComponent } from './detail/Teacher-detail.component';

const routes: Routes = [
  {path: '', component: TeacherHomeComponent},
  { path: 'new', component: TeacherNewComponent },
  { path: ':id', component: TeacherDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Teacher-detail-permissions'
      }
    }
  },{
    path: ':teacher_id/DepartmentFaculty', loadChildren: () => import('../DepartmentFaculty/DepartmentFaculty.module').then(m => m.DepartmentFacultyModule),
    data: {
        oPermission: {
            permissionId: 'DepartmentFaculty-detail-permissions'
        }
    }
},{
    path: ':teacher_id/TeacherCourseAssignment', loadChildren: () => import('../TeacherCourseAssignment/TeacherCourseAssignment.module').then(m => m.TeacherCourseAssignmentModule),
    data: {
        oPermission: {
            permissionId: 'TeacherCourseAssignment-detail-permissions'
        }
    }
}
];

export const TEACHER_MODULE_DECLARATIONS = [
    TeacherHomeComponent,
    TeacherNewComponent,
    TeacherDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TeacherRoutingModule { }