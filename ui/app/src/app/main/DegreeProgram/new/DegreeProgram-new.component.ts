import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'DegreeProgram-new',
  templateUrl: './DegreeProgram-new.component.html',
  styleUrls: ['./DegreeProgram-new.component.scss']
})
export class DegreeProgramNewComponent {
  @ViewChild("DegreeProgramForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}