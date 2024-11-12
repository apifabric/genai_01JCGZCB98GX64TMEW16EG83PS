import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'DepartmentFaculty-new',
  templateUrl: './DepartmentFaculty-new.component.html',
  styleUrls: ['./DepartmentFaculty-new.component.scss']
})
export class DepartmentFacultyNewComponent {
  @ViewChild("DepartmentFacultyForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}