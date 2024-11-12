import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {PROGRAMCOURSE_MODULE_DECLARATIONS, ProgramCourseRoutingModule} from  './ProgramCourse-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    ProgramCourseRoutingModule
  ],
  declarations: PROGRAMCOURSE_MODULE_DECLARATIONS,
  exports: PROGRAMCOURSE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class ProgramCourseModule { }