import time

import eel

def battery_voltage():
   with open('dashboardout.txt', 'r') as f:
      while True:
         for line in f:
            n = line[41]+line[42]+line[43]+line[44]
            batteryvoltage = (int(n, 16)*0.00030518)
            eel.updateBatteryVoltage(round(batteryvoltage,2))
            time.sleep(1)

