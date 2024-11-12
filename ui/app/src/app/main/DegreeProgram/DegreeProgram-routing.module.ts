import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DegreeProgramHomeComponent } from './home/DegreeProgram-home.component';
import { DegreeProgramNewComponent } from './new/DegreeProgram-new.component';
import { DegreeProgramDetailComponent } from './detail/DegreeProgram-detail.component';

const routes: Routes = [
  {path: '', component: DegreeProgramHomeComponent},
  { path: 'new', component: DegreeProgramNewComponent },
  { path: ':id', component: DegreeProgramDetailComponent,
    data: {
      oPermission: {
        permissionId: 'DegreeProgram-detail-permissions'
      }
    }
  },{
    path: ':program_id/ProgramCourse', loadChildren: () => import('../ProgramCourse/ProgramCourse.module').then(m => m.ProgramCourseModule),
    data: {
        oPermission: {
            permissionId: 'ProgramCourse-detail-permissions'
        }
    }
}
];

export const DEGREEPROGRAM_MODULE_DECLARATIONS = [
    DegreeProgramHomeComponent,
    DegreeProgramNewComponent,
    DegreeProgramDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DegreeProgramRoutingModule { }