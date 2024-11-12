import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {DEGREEPROGRAM_MODULE_DECLARATIONS, DegreeProgramRoutingModule} from  './DegreeProgram-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    DegreeProgramRoutingModule
  ],
  declarations: DEGREEPROGRAM_MODULE_DECLARATIONS,
  exports: DEGREEPROGRAM_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DegreeProgramModule { }