import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CourseRequirement-card.component.html',
  styleUrls: ['./CourseRequirement-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CourseRequirement-card]': 'true'
  }
})

export class CourseRequirementCardComponent {


}