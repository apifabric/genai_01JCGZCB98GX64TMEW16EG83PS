import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './DepartmentFaculty-card.component.html',
  styleUrls: ['./DepartmentFaculty-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.DepartmentFaculty-card]': 'true'
  }
})

export class DepartmentFacultyCardComponent {


}