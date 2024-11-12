import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {COURSEREQUIREMENT_MODULE_DECLARATIONS, CourseRequirementRoutingModule} from  './CourseRequirement-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CourseRequirementRoutingModule
  ],
  declarations: COURSEREQUIREMENT_MODULE_DECLARATIONS,
  exports: COURSEREQUIREMENT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CourseRequirementModule { }