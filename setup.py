import can
import os
import time

print('Initialising can bus...')
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000") #check ECU bitrate is 500000
print('System ready')
python -m can.logger -c can0 -i socketcan -b 500000 -f log1.log
while True:
  time.sleep(0.1)
