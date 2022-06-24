export default function (coolantTempValue) {
	const coolantTemp = document.querySelector('.coolant-temp-value');

	coolantTemp.textContent = `${coolantTempValue}°C`;
}
