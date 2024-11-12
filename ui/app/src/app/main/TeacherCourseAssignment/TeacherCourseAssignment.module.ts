import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {TEACHERCOURSEASSIGNMENT_MODULE_DECLARATIONS, TeacherCourseAssignmentRoutingModule} from  './TeacherCourseAssignment-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    TeacherCourseAssignmentRoutingModule
  ],
  declarations: TEACHERCOURSEASSIGNMENT_MODULE_DECLARATIONS,
  exports: TEACHERCOURSEASSIGNMENT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class TeacherCourseAssignmentModule { }