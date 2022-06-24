export default function (batteryVoltageValue) {
	const batteryVoltage = document.querySelector('.battery-voltage-value');

	batteryVoltage.textContent = `${batteryVoltageValue} V`;
}
