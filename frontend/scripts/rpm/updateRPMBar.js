import {
	circle1,
	circle2,
	circle3,
	circle4,
	circle5,
	circle6,
	circle7,
	circle8,
	circle9,
	circle10,
	circle11,
	circle12,
	circle13,
	circle14,
	circle15,
} from './circles.js';
import resetNextRPMBars from './resetNextRPMBars.js';

export default function (rpmValue) {
	if (rpmValue > 867) {
		circle1.style.background = '#198C19';
		resetNextRPMBars(1);
	}

	if (rpmValue > 1734) {
		circle2.style.background = '#198C19';
		resetNextRPMBars(2);
	}

	if (rpmValue > 2601) {
		circle3.style.background = '#198C19';
		resetNextRPMBars(3);
	}

	if (rpmValue > 3468) {
		circle4.style.background = '#198C19';
		resetNextRPMBars(4);
	}

	if (rpmValue > 4335) {
		circle5.style.background = '#198C19';
		resetNextRPMBars(5);
	}

	if (rpmValue > 5202) {
		circle6.style.background = '#FF0000';
		resetNextRPMBars(6);
	}

	if (rpmValue > 6069) {
		circle7.style.background = '#FF0000';
		resetNextRPMBars(7);
	}

	if (rpmValue > 6936) {
		circle8.style.background = '#FF0000';
		resetNextRPMBars(8);
	}

	if (rpmValue > 7803) {
		circle9.style.background = '#FF0000';
		resetNextRPMBars(9);
	}

	if (rpmValue > 8670) {
		circle10.style.background = '#FF0000';
		resetNextRPMBars(10);
	}

	if (rpmValue > 9537) {
		circle11.style.background = '#0000FF';
		resetNextRPMBars(11);
	}

	if (rpmValue > 10404) {
		circle12.style.background = '#0000FF';
		resetNextRPMBars(12);
	}

	if (rpmValue > 11271) {
		circle13.style.background = '#0000FF';
		resetNextRPMBars(13);
	}

	if (rpmValue > 12138) {
		circle14.style.background = '#0000FF';
		resetNextRPMBars(14);
	}

	if (rpmValue > 13000) {
		circle15.style.background = '#0000FF';
	}
}
