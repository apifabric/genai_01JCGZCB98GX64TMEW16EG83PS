import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'TeacherCourseAssignment-new',
  templateUrl: './TeacherCourseAssignment-new.component.html',
  styleUrls: ['./TeacherCourseAssignment-new.component.scss']
})
export class TeacherCourseAssignmentNewComponent {
  @ViewChild("TeacherCourseAssignmentForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}