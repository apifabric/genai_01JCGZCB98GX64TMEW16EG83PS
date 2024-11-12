import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './DegreeProgram-card.component.html',
  styleUrls: ['./DegreeProgram-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.DegreeProgram-card]': 'true'
  }
})

export class DegreeProgramCardComponent {


}