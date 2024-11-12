import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './TeacherCourseAssignment-card.component.html',
  styleUrls: ['./TeacherCourseAssignment-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.TeacherCourseAssignment-card]': 'true'
  }
})

export class TeacherCourseAssignmentCardComponent {


}