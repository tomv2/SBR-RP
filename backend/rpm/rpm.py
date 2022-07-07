import time

import eel

def rpm():
   with open('dashboardout.txt', 'r') as f:
      while True:
         for line in f:
            n = line[33]+line[34]+line[35]+line[36]
            enginespeed = (int(n, 16))
            if enginespeed > 2500:
               enginespeed2 = enginespeed * 1.0143541
            if enginespeed > 3000:
               enginespeed2 = enginespeed * 1.0287082
            if enginespeed > 3500:
               enginespeed2 = enginespeed * 1.0430623
            if enginespeed > 4000:
               enginespeed2 = enginespeed * 1.0574164
            if enginespeed > 4500:
               enginespeed2 = enginespeed * 1.0717705
            if enginespeed > 5000:
               enginespeed2 = enginespeed * 1.0861246
            if enginespeed > 5500:
               enginespeed2 = enginespeed * 1.1004787
            if enginespeed > 6000:
               enginespeed2 = enginespeed * 1.1148328
            if enginespeed > 7000:
               enginespeed2 = enginespeed * 1.1291869
            if enginespeed > 7500:
               enginespeed2 = enginespeed * 1.143541
            if enginespeed > 8000:
               enginespeed2 = enginespeed * 1.157895
            if enginespeed > 9000:
               enginespeed2 = enginespeed * 
            eel.updateRPM(enginespeed2)
            time.sleep(0.1)
