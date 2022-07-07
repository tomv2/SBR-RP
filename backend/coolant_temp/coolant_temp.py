import time
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT)

import eel

def coolant_temp():
   with open('dashboardout.txt', 'r') as f:
      while True:
         for line in f:
            n = line[31]+line[32]
            tempconv = (int(n, 16)-32)/1.8
            eel.updateCoolantTemp(round(tempconv,2))
            time.sleep(1)
            if tempconv > 85:
               GPIO.output(4, 1)
            if tempconv < 85:
               GPIO.output(4, 0)
