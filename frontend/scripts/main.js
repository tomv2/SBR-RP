import updateRPMBar from './rpm/updateRPMBar.js';
import updateRPMValue from './rpm/updateRPMValue.js';
import CoolantTempValue from './coolantTemp/updateCoolantTempValue.js';
import updateCoolantTempValue from './coolantTemp/updateCoolantTempValue.js';
import BatteryVoltageValue from './batteryVoltage/updateBatteryVoltageValue.js';
import updateBatteryVoltageValue from './batteryVoltage/updateBatteryVoltageValue.js';
import OilPressureValue from './oilPressure/updateOilPressureValue.js';
import updateOilPressureValue from './oilPressure/updateOilPressureValue.js';
import FuelPressureValue from './fuelPressure/updateFuelPressureValue.js';
import updateFuelPressureValue from './fuelPressure/updateFuelPressureValue.js';

eel.expose(updateRPM);
function updateRPM(rpmValue) {
	updateRPMValue(rpmValue);
	updateRPMBar(rpmValue);
}

eel.expose(updateBatteryVoltage);
function updateBatteryVoltage(BatteryVoltageValue) {
	updateBatteryVoltageValue(BatteryVoltageValue);
}

eel.expose(updateCoolantTemp);
function updateCoolantTemp(CoolantTempValue) {
	updateCoolantTempValue(CoolantTempValue);
}

eel.expose(updateOilPressure);
function updateOilPressure(OilPressureValue) {
	updateOilPressureValue(OilPressureValue);
}

eel.expose(updateFuelPressure);
function updateFuelPressure(FuelPressureValue) {
	updateFuelPressureValue(FuelPressureValue);
}