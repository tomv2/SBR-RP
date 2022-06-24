import time

import eel

def oil_pressure():
   with open('dashboardout.txt', 'r') as f:
      while True:
         for line in f:
            n= line[37]+line[38]+line[39]+line[40]
            oilpressure = (int(n, 16)*0.001)
            eel.updateRPM(oilpressure)
            time.sleep(0.1)
      
