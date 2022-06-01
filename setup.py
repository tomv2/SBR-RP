import can
import os
import time

print('Initialising can bus...')
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000") #check ECU bitrate is 500000
print('System ready')
bus = can.interface.Bus(channel='can0', bustype='socketcan')
while true:
  notifier = can.Notifier(bus, [can.Printer()])
