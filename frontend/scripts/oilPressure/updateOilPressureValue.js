export default function (oilPressureValue) {
	const oilPressure = document.querySelector('.oil-pressure-value');

	oilPressure.textContent = `${oilPressureValue} Bar`;
}
