import time

import eel

def rpm():
   with open('dashboardout.txt', 'r') as f:
      while True:
         for line in f:
            n = line[33]+line[34]+line[35]+line[36]
            enginespeed = (int(n, 16))+20000
            eel.updateRPM(enginespeed)
            time.sleep(0.1)
