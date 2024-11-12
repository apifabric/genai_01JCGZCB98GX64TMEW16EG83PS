import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CourseRequirement-new',
  templateUrl: './CourseRequirement-new.component.html',
  styleUrls: ['./CourseRequirement-new.component.scss']
})
export class CourseRequirementNewComponent {
  @ViewChild("CourseRequirementForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}