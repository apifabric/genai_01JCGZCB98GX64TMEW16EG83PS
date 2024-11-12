import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TeacherCourseAssignmentHomeComponent } from './home/TeacherCourseAssignment-home.component';
import { TeacherCourseAssignmentNewComponent } from './new/TeacherCourseAssignment-new.component';
import { TeacherCourseAssignmentDetailComponent } from './detail/TeacherCourseAssignment-detail.component';

const routes: Routes = [
  {path: '', component: TeacherCourseAssignmentHomeComponent},
  { path: 'new', component: TeacherCourseAssignmentNewComponent },
  { path: ':id', component: TeacherCourseAssignmentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'TeacherCourseAssignment-detail-permissions'
      }
    }
  }
];

export const TEACHERCOURSEASSIGNMENT_MODULE_DECLARATIONS = [
    TeacherCourseAssignmentHomeComponent,
    TeacherCourseAssignmentNewComponent,
    TeacherCourseAssignmentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TeacherCourseAssignmentRoutingModule { }