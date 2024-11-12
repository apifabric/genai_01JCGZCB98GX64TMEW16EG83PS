import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProgramCourseHomeComponent } from './home/ProgramCourse-home.component';
import { ProgramCourseNewComponent } from './new/ProgramCourse-new.component';
import { ProgramCourseDetailComponent } from './detail/ProgramCourse-detail.component';

const routes: Routes = [
  {path: '', component: ProgramCourseHomeComponent},
  { path: 'new', component: ProgramCourseNewComponent },
  { path: ':id', component: ProgramCourseDetailComponent,
    data: {
      oPermission: {
        permissionId: 'ProgramCourse-detail-permissions'
      }
    }
  }
];

export const PROGRAMCOURSE_MODULE_DECLARATIONS = [
    ProgramCourseHomeComponent,
    ProgramCourseNewComponent,
    ProgramCourseDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProgramCourseRoutingModule { }