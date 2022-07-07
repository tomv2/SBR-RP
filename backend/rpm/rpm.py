import time

import eel

def rpm():
   with open('dashboardout.txt', 'r') as f:
      while True:
         for line in f:
            n = line[33]+line[34]+line[35]+line[36]
            enginespeed = (int(n, 16))
            if enginespeed > 500:
               ff
            if enginespeed > 1000:
               ff
            if enginespeed > 1500:
               ff
            if enginespeed > 2000:
               ff
            if enginespeed > 2500:
               ff
            if enginespeed > 3000:
               ff
            if enginespeed > 3500:
               ff
            if enginespeed > 4000:
               ff
            if enginespeed > 4500:
               ff
            if enginespeed > 5000:
               ff
            if enginespeed > 5500:
               ff
            if enginespeed > 6000:
               ff
            if enginespeed > 6500:
               ff
            if enginespeed > 7000:
               ff
            if enginespeed > 7500:
               ff
            if enginespeed > 8000:
               ff
            if enginespeed > 8500:
               ff
            if enginespeed > 9000:
               enginespeed2 = enginespeed * 1.157895
            eel.updateRPM(enginespeed2)
            time.sleep(0.1)
