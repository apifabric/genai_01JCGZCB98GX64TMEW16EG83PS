import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './ProgramCourse-card.component.html',
  styleUrls: ['./ProgramCourse-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.ProgramCourse-card]': 'true'
  }
})

export class ProgramCourseCardComponent {


}