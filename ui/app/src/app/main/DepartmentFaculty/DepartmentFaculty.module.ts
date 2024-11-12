import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {DEPARTMENTFACULTY_MODULE_DECLARATIONS, DepartmentFacultyRoutingModule} from  './DepartmentFaculty-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    DepartmentFacultyRoutingModule
  ],
  declarations: DEPARTMENTFACULTY_MODULE_DECLARATIONS,
  exports: DEPARTMENTFACULTY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DepartmentFacultyModule { }