import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CourseRequirementHomeComponent } from './home/CourseRequirement-home.component';
import { CourseRequirementNewComponent } from './new/CourseRequirement-new.component';
import { CourseRequirementDetailComponent } from './detail/CourseRequirement-detail.component';

const routes: Routes = [
  {path: '', component: CourseRequirementHomeComponent},
  { path: 'new', component: CourseRequirementNewComponent },
  { path: ':id', component: CourseRequirementDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CourseRequirement-detail-permissions'
      }
    }
  }
];

export const COURSEREQUIREMENT_MODULE_DECLARATIONS = [
    CourseRequirementHomeComponent,
    CourseRequirementNewComponent,
    CourseRequirementDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CourseRequirementRoutingModule { }