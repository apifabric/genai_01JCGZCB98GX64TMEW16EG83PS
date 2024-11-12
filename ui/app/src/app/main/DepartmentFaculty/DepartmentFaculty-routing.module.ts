import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DepartmentFacultyHomeComponent } from './home/DepartmentFaculty-home.component';
import { DepartmentFacultyNewComponent } from './new/DepartmentFaculty-new.component';
import { DepartmentFacultyDetailComponent } from './detail/DepartmentFaculty-detail.component';

const routes: Routes = [
  {path: '', component: DepartmentFacultyHomeComponent},
  { path: 'new', component: DepartmentFacultyNewComponent },
  { path: ':id', component: DepartmentFacultyDetailComponent,
    data: {
      oPermission: {
        permissionId: 'DepartmentFaculty-detail-permissions'
      }
    }
  }
];

export const DEPARTMENTFACULTY_MODULE_DECLARATIONS = [
    DepartmentFacultyHomeComponent,
    DepartmentFacultyNewComponent,
    DepartmentFacultyDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DepartmentFacultyRoutingModule { }