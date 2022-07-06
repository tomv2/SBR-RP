import time
import threading

import eel

import backend.rpm.rpm as rpm
import backend.battery_voltage.battery_voltage as battery_voltage
import backend.coolant_temp.coolant_temp as coolant_temp
import backend.oil_pressure.oil_pressure as oil_pressure

eel.init('frontend')

# for RPM
rpm_thread = threading.Thread(target=rpm.rpm)
rpm_thread.start()

# battery voltage
battery_voltage_thread = threading.Thread(target=battery_voltage.battery_voltage)
battery_voltage_thread.start()

# for coolant temp
coolant_temp_thread = threading.Thread(target=coolant_temp.coolant_temp)
coolant_temp_thread.start()

#Oil pressure
oil_pressure_thread = threading.Thread(target=oil_pressure.oil_pressure)
oil_pressure_thread.start()

eel.start('index.html')
